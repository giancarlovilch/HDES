import datetime
import requests
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect

def index(request):
    user = request.session.get("user")
    if not user:
        return redirect("php_login_form")   # si no está logueado → login
    
    ctx = {"year": datetime.datetime.now().year, "user": user}
    return render(request, "index.html", ctx)

def php_login_form(request):
    if request.method == "POST":
        username = (request.POST.get("username") or "").strip()
        password = request.POST.get("password") or ""

        if not username or not password:
            messages.error(request, "Usuario y contraseña son obligatorios.")
            return render(request, "login.html")

        try:
            r = requests.post(
                f"{settings.PHP_API_BASE}/api_login.php",
                json={"username": username, "password": password},
                timeout=8,
            )
            data = r.json()
        except requests.RequestException:
            messages.error(request, "No se pudo contactar al servidor de autenticación.")
            return render(request, "login.html")
        except ValueError:
            messages.error(request, "Respuesta inválida del servidor de autenticación.")
            return render(request, "login.html")

        if data.get("success"):
            request.session["user"] = data.get("user")
            request.session["token"] = data.get("token")
            messages.success(request, "Inicio de sesión exitoso.")
            return redirect("index")
        else:
            messages.error(request, data.get("message", "Credenciales inválidas."))
            return render(request, "login.html")

    return render(request, "login.html")

def php_logout(request):
    token = request.session.get("token")
    if token:
        try:
            requests.post(
                f"{settings.PHP_API_BASE}/api_logout.php",
                json={"token": token},
                timeout=5,
            )
        except requests.RequestException:
            # Si no responde el PHP, de todas formas limpiamos sesión local
            pass

    request.session.flush()
    messages.success(request, "Has cerrado sesión.")
    return redirect("php_login_form")
