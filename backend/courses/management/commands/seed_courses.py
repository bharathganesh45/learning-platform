from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from courses.models import Category, Course, Lesson

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed the database with course categories, courses, and lessons'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting to seed courses...'))

        # Create or get categories
        categories = self.create_categories()

        # Create or get default instructor
        instructor = self.create_instructor()

        # Create courses
        courses_data = [
            {
                'title': 'Python Development',
                'description': 'Learn Python from basics to advanced topics. This comprehensive course covers everything from fundamental programming concepts to object-oriented programming, data structures, and real-world applications.',
                'category': 'Programming Languages',
                'level': 'beginner',
                'duration_hours': 40,
                'lessons': [
                    {'title': 'Introduction to Python', 'description': 'Get started with Python programming language, its history, and setting up your development environment.', 'order': 1, 'duration_minutes': 30},
                    {'title': 'Variables & Data Types', 'description': 'Learn about Python variables, data types (int, float, string, list, dict), and type conversion.', 'order': 2, 'duration_minutes': 45},
                    {'title': 'Control Flow', 'description': 'Master if/else statements, loops (for and while), and control flow structures in Python.', 'order': 3, 'duration_minutes': 50},
                    {'title': 'Functions', 'description': 'Understand how to create and use functions, parameters, return values, and scope in Python.', 'order': 4, 'duration_minutes': 55},
                    {'title': 'OOP in Python', 'description': 'Learn Object-Oriented Programming concepts including classes, objects, inheritance, and polymorphism.', 'order': 5, 'duration_minutes': 60},
                ]
            },
            {
                'title': 'Fullstack Development',
                'description': 'Master both frontend and backend development. Learn to build complete web applications from user interface to server-side logic, databases, and deployment.',
                'category': 'Web Development',
                'level': 'intermediate',
                'duration_hours': 60,
                'lessons': [
                    {'title': 'Frontend Fundamentals', 'description': 'Introduction to HTML, CSS, and JavaScript for building modern web interfaces.', 'order': 1, 'duration_minutes': 60},
                    {'title': 'Backend APIs', 'description': 'Learn to build RESTful APIs, handle HTTP requests, and implement server-side logic.', 'order': 2, 'duration_minutes': 70},
                    {'title': 'Database Design', 'description': 'Understand database concepts, SQL queries, and database relationships for web applications.', 'order': 3, 'duration_minutes': 65},
                    {'title': 'Authentication', 'description': 'Implement user authentication, authorization, and security best practices in web applications.', 'order': 4, 'duration_minutes': 75},
                    {'title': 'Deployment', 'description': 'Learn how to deploy fullstack applications to production environments and cloud platforms.', 'order': 5, 'duration_minutes': 80},
                ]
            },
            {
                'title': 'Java',
                'description': 'Comprehensive Java programming course covering from basic syntax to advanced topics like multithreading, collections, and the Spring framework.',
                'category': 'Programming Languages',
                'level': 'beginner',
                'duration_hours': 50,
                'lessons': [
                    {'title': 'Java Basics', 'description': 'Introduction to Java programming, syntax, variables, and basic programming concepts.', 'order': 1, 'duration_minutes': 40},
                    {'title': 'Object-Oriented Programming', 'description': 'Deep dive into OOP concepts in Java: classes, objects, inheritance, encapsulation, and polymorphism.', 'order': 2, 'duration_minutes': 70},
                    {'title': 'Collections Framework', 'description': 'Learn about Java collections: ArrayList, HashMap, Set, and other data structures.', 'order': 3, 'duration_minutes': 60},
                    {'title': 'Multithreading', 'description': 'Understand concurrent programming in Java, threads, synchronization, and thread safety.', 'order': 4, 'duration_minutes': 75},
                    {'title': 'Spring Framework', 'description': 'Introduction to Spring Framework for building enterprise Java applications.', 'order': 5, 'duration_minutes': 80},
                ]
            },
            {
                'title': 'AI/ML',
                'description': 'Introduction to Artificial Intelligence and Machine Learning. Learn the fundamentals of AI, data preprocessing, supervised and unsupervised learning, neural networks, and deep learning.',
                'category': 'Data Science',
                'level': 'intermediate',
                'duration_hours': 70,
                'lessons': [
                    {'title': 'Introduction to AI/ML', 'description': 'Overview of artificial intelligence and machine learning, their history, and applications.', 'order': 1, 'duration_minutes': 50},
                    {'title': 'Data Preprocessing', 'description': 'Learn to clean, transform, and prepare data for machine learning models.', 'order': 2, 'duration_minutes': 60},
                    {'title': 'Supervised Learning', 'description': 'Understand supervised learning algorithms: regression, classification, and model evaluation.', 'order': 3, 'duration_minutes': 70},
                    {'title': 'Neural Networks', 'description': 'Introduction to neural networks, their architecture, and how they learn from data.', 'order': 4, 'duration_minutes': 80},
                    {'title': 'Deep Learning', 'description': 'Explore deep learning concepts, convolutional neural networks, and advanced architectures.', 'order': 5, 'duration_minutes': 90},
                ]
            },
            {
                'title': 'C/C++',
                'description': 'Learn system programming with C and C++. Master low-level programming, memory management, pointers, and advanced C++ features including the Standard Template Library.',
                'category': 'Programming Languages',
                'level': 'beginner',
                'duration_hours': 55,
                'lessons': [
                    {'title': 'C Basics', 'description': 'Introduction to C programming language, syntax, variables, and basic programming constructs.', 'order': 1, 'duration_minutes': 45},
                    {'title': 'Pointers & Memory', 'description': 'Master pointers, memory management, dynamic allocation, and memory safety in C.', 'order': 2, 'duration_minutes': 70},
                    {'title': 'C++ Fundamentals', 'description': 'Introduction to C++ programming, differences from C, and C++ specific features.', 'order': 3, 'duration_minutes': 60},
                    {'title': 'STL', 'description': 'Learn the Standard Template Library: containers, iterators, algorithms, and generic programming.', 'order': 4, 'duration_minutes': 75},
                    {'title': 'Advanced C++ Features', 'description': 'Explore advanced C++ features: templates, lambda expressions, smart pointers, and modern C++ practices.', 'order': 5, 'duration_minutes': 80},
                ]
            },
        ]

        created_count = 0
        for course_data in courses_data:
            category = categories[course_data['category']]
            lessons_data = course_data.pop('lessons')
            
            course, created = Course.objects.get_or_create(
                title=course_data['title'],
                defaults={
                    'description': course_data['description'],
                    'instructor': instructor,
                    'category': category,
                    'level': course_data['level'],
                    'duration_hours': course_data['duration_hours'],
                    'is_free': True,
                    'is_published': True,
                }
            )
            
            if created:
                created_count += 1
                self.stdout.write(self.style.SUCCESS(f'Created course: {course.title}'))
                
                # Create lessons for this course
                for lesson_data in lessons_data:
                    Lesson.objects.get_or_create(
                        course=course,
                        title=lesson_data['title'],
                        defaults={
                            'description': lesson_data['description'],
                            'order': lesson_data['order'],
                            'duration_minutes': lesson_data['duration_minutes'],
                            'content': f"This lesson covers {lesson_data['title']}. {lesson_data['description']}",
                        }
                    )
                self.stdout.write(self.style.SUCCESS(f'  Created {len(lessons_data)} lessons for {course.title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Course already exists: {course.title}'))

        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully seeded {created_count} new courses!'))

    def create_categories(self):
        """Create or get course categories"""
        categories_data = {
            'Programming Languages': 'Courses covering various programming languages',
            'Web Development': 'Full-stack web development courses',
            'Data Science': 'Data science, AI, and machine learning courses',
        }
        
        categories = {}
        for name, description in categories_data.items():
            category, created = Category.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created category: {name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Category already exists: {name}'))
            categories[name] = category
        
        return categories

    def create_instructor(self):
        """Create or get default instructor user"""
        username = 'default_instructor'
        email = 'instructor@learningplatform.com'
        
        instructor, created = User.objects.get_or_create(
            username=username,
            defaults={
                'email': email,
                'is_instructor': True,
                'is_staff': True,
            }
        )
        
        if created:
            instructor.set_password('instructor123')  # Default password, should be changed
            instructor.save()
            self.stdout.write(self.style.SUCCESS(f'Created instructor: {username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Instructor already exists: {username}'))
        
        return instructor

