from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category, Course, Lesson, Enrollment, Progress
from .serializers import (
    CategorySerializer, CourseSerializer, CourseDetailSerializer,
    LessonSerializer, EnrollmentSerializer, ProgressSerializer
)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(is_published=True)
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseDetailSerializer
        return CourseSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = Course.objects.filter(is_published=True)
        category = self.request.query_params.get('category', None)
        level = self.request.query_params.get('level', None)
        search = self.request.query_params.get('search', None)

        if category:
            queryset = queryset.filter(category__name__icontains=category)
        if level:
            queryset = queryset.filter(level=level)
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(description__icontains=search)

        return queryset.select_related('instructor', 'category').prefetch_related('lessons', 'enrollments')

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def enroll(self, request, pk=None):
        course = self.get_object()
        student = request.user

        enrollment, created = Enrollment.objects.get_or_create(
            student=student,
            course=course
        )

        if not created:
            return Response(
                {'message': 'Already enrolled in this course'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def my_enrollment(self, request, pk=None):
        course = self.get_object()
        try:
            enrollment = Enrollment.objects.get(student=request.user, course=course)
            serializer = EnrollmentSerializer(enrollment)
            return Response(serializer.data)
        except Enrollment.DoesNotExist:
            return Response(
                {'message': 'Not enrolled in this course'},
                status=status.HTTP_404_NOT_FOUND
            )


class EnrollmentViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(student=self.request.user)


class ProgressViewSet(viewsets.ModelViewSet):
    serializer_class = ProgressSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        enrollment_id = self.request.query_params.get('enrollment', None)
        if enrollment_id:
            enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=self.request.user)
            return Progress.objects.filter(enrollment=enrollment)
        return Progress.objects.filter(enrollment__student=self.request.user)

    def create(self, request, *args, **kwargs):
        enrollment_id = request.data.get('enrollment')
        lesson_id = request.data.get('lesson')
        completed = request.data.get('completed', False)

        enrollment = get_object_or_404(Enrollment, id=enrollment_id, student=request.user)
        lesson = get_object_or_404(Lesson, id=lesson_id, course=enrollment.course)

        progress, created = Progress.objects.get_or_create(
            enrollment=enrollment,
            lesson=lesson
        )

        progress.completed = completed
        if completed:
            from django.utils import timezone
            progress.completed_at = timezone.now()
        progress.save()

        serializer = self.get_serializer(progress)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

