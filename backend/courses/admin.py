from django.contrib import admin
from .models import Category, Course, Lesson, Enrollment, Progress


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'instructor', 'category', 'price', 'is_published', 'created_at']
    list_filter = ['is_published', 'level', 'category', 'created_at']
    search_fields = ['title', 'description']
    filter_horizontal = []


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'order', 'duration_minutes']
    list_filter = ['course', 'created_at']
    search_fields = ['title', 'description']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'enrolled_at', 'is_completed']
    list_filter = ['is_completed', 'enrolled_at']
    search_fields = ['student__username', 'course__title']


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ['enrollment', 'lesson', 'completed', 'completed_at']
    list_filter = ['completed', 'completed_at']

