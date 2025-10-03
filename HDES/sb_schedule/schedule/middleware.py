from django.shortcuts import redirect
from django.urls import reverse

class PHPAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user_php = request.session.get("user")

        # Rutas que no necesitan login
        allowed_paths = [reverse("php_login_form"), "/admin/"]
        
        if not request.user_php and not any(request.path.startswith(p) for p in allowed_paths):
            return redirect("php_login_form")

        return self.get_response(request)
