from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def root_view(request):
    """
    Root API endpoint that provides information about the API.
    """
    return JsonResponse({
        'message': 'Learning Platform API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'api_documentation': {
                'authentication': '/api/auth/',
                'courses': '/api/courses/',
                'categories': '/api/categories/',
                'enrollments': '/api/enrollments/',
                'progress': '/api/progress/',
            }
        },
        'frontend': 'http://localhost:3000',
        'documentation': 'See README.md for API documentation'
    })

