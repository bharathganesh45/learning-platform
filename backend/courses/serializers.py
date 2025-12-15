from rest_framework import serializers
from .models import Category, Course, Lesson, Enrollment, Progress
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'video_url', 'content', 'order', 'duration_minutes']


class CourseSerializer(serializers.ModelSerializer):
    instructor = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    lessons_count = serializers.IntegerField(source='lessons.count', read_only=True)
    enrolled_count = serializers.IntegerField(source='enrollments.count', read_only=True)
    is_enrolled = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'description', 'instructor', 'category',
            'thumbnail', 'price', 'is_free', 'duration_hours', 'level',
            'created_at', 'updated_at', 'is_published',
            'lessons_count', 'enrolled_count', 'is_enrolled'
        ]

    def get_is_enrolled(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return Enrollment.objects.filter(student=request.user, course=obj).exists()
        return False


class CourseDetailSerializer(CourseSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta(CourseSerializer.Meta):
        fields = CourseSerializer.Meta.fields + ['lessons']


class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    student = UserSerializer(read_only=True)
    progress_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'enrolled_at', 'completed_at', 'is_completed', 'progress_percentage']

    def get_progress_percentage(self, obj):
        total_lessons = obj.course.lessons.count()
        if total_lessons == 0:
            return 0
        completed_lessons = obj.progress.filter(completed=True).count()
        return int((completed_lessons / total_lessons) * 100)


class ProgressSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'lesson', 'completed', 'completed_at', 'last_position']

