# 🔑 API en Django (Intranet)

Este documento describe los **endpoints del sistema Django**, la forma en que se integran con el **login PHP** y ejemplos de uso.

---

## 📋 Arquitectura de Autenticación

- 🔐 **Login principal** ocurre en **PHP** (`api_login.php`).  
- Django actúa como **consumidor de esa API**.  
- Si las credenciales son válidas:
  - PHP devuelve `user` + `token`.
  - Django guarda ambos en `request.session`.
- Logout (`php_logout`) → invalida el token en PHP y limpia la sesión en Django.

👉 Esto significa que **todas las llamadas a la API Django requieren que el usuario ya haya iniciado sesión vía PHP**.

---

## 📂 Endpoints principales

### 👩‍💼 Empleados
- `GET /api/employees/` → Lista todos los empleados.
- `POST /api/employees/` → Crea un empleado.
- `GET /api/employees/{id}/` → Obtiene un empleado específico.
- `PUT /api/employees/{id}/` → Actualiza un empleado.
- `DELETE /api/employees/{id}/` → Elimina un empleado.

### 🗓 Horarios
- `GET /api/schedule/` → Lista días con sus asientos y trabajadores asignados.
- `POST /api/skills/assign/` → Asigna un trabajador a un día/turno (ejemplo: mañana, tarde).

### 📊 Reportes
- `GET /api/reports/` → Lista de reportes de desempeño/salario.
- `POST /api/reports/` → Crear un nuevo reporte.
- `GET /api/reports/{id}/` → Ver reporte específico.
- `PUT /api/reports/{id}/` → Actualizar un reporte.
- `DELETE /api/reports/{id}/` → Eliminar reporte.

### ⭐ Skills
- `GET /api/skills/` → Lista todas las habilidades disponibles.
- `POST /api/skills/assign/` → Asigna una habilidad a un empleado con nivel (1–5).

### ⚖️ Legal
- `GET /api/contracts/` → Lista contratos registrados.
- `POST /api/contracts/` → Crear nuevo contrato.

---

## 🛠 Autenticación

### Login (PHP)
- Endpoint: `POST http://localhost:3000/myphp/api_login.php`
- Body (JSON):
```json
{
  "username": "admin",
  "password": "12345"
}
```

- Respuesta:

```
{
  "success": true,
  "user": {
    "id": 1,
    "username": "admin",
    "nombre_completo": "Administrador General",
    "rol": "Administrador",
    "nickname": "admin"
  },
  "token": "abc123xyz"
}
```

### Logout (PHP)

- Endpoint: `POST /logout/`
- Acción: invalida token en PHP y limpia sesión en Django.

---

## 📬 Ejemplos de Requests (Postman)

### Obtener lista de empleados

```
GET http://127.0.0.1:8000/api/employees/
Cookie: sessionid=<django_session_id>
```

### Crear nuevo empleado

```
POST http://127.0.0.1:8000/api/employees/
Content-Type: application/json
Cookie: sessionid=<django_session_id>

{
  "name": "Carlos Pérez",
  "position": "Vendedor",
  "salary": 1200
}
```

### Asignar skill a trabajador

```
POST http://127.0.0.1:8000/api/skills/assign/
Content-Type: application/json
Cookie: sessionid=<django_session_id>

{
  "worker_id": 1,
  "skill_id": 2,
  "level": 4
}
```

Respuesta:

```
{
  "message": "Skill Ventas asignada a Carlos Pérez con nivel 4",
  "created": true
}
```

---
