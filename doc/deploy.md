# 🚀 Despliegue de HDES Intranet

Este documento explica cómo desplegar el proyecto en producción, teniendo en cuenta que el **login y autenticación ocurren en PHP**, y la **intranet corre en Django**.

---

## 1. Requisitos

- **Backend PHP** (ya desplegado en Apache/cPanel o VPS)
  - Debe exponer `api_login.php` y `api_logout.php`
  - Configurar correctamente `CORS` y HTTPS si se accede desde otro dominio
- **Django 5+**
- **Python 3.11+**
- **Base de datos**
  - Desarrollo: SQLite
  - Producción: PostgreSQL recomendado
- **Servidor**
  - Opción A: VPS (Ubuntu/Debian)
  - Opción B: Hosting con soporte a **cPanel + Passenger**

---

## 2. Variables de entorno (`.env`)

Ejemplo:

```
DEBUG=False
SECRET_KEY=super-secret-key
DATABASE_URL=postgres://user:pass@localhost:5432/hdes
ALLOWED_HOSTS=midominio.com, www.midominio.com

PHP_API_BASE=https://midominio.com/myphp
```

👉 Importante: `PHP_API_BASE` debe apuntar al sistema PHP ya desplegado.

---

## 3. Instalación y migraciones

```bash
git clone https://github.com/mi-org/hdes.git
cd hdes

python -m venv venv
source venv/bin/activate   # Windows: .\venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput
```

---

## 4. Despliegue en cPanel (opcional)

Si tu hosting soporta **Python Apps (Passenger)**:

1. Entra a cPanel → **Setup Python App**

2. Selecciona Python 3.11

3. Configura la ruta de tu proyecto

4. Agrega dependencias en `requirements.txt`

5. Configura la app WSGI:

   ```
   from sb_schedule.wsgi import application
   ```

6. Asegúrate de configurar `PHP_API_BASE` en `.env` con la URL de tu backend PHP.

---

## 5. Integración con PHP

- Django nunca pide credenciales directamente a la DB.
- Toda autenticación ocurre vía `api_login.php`.
- En producción, asegúrate de que:
  - PHP y Django usen **HTTPS**
  - El dominio de PHP sea accesible desde Django (`PHP_API_BASE`)
  - El token de PHP tenga tiempo de expiración seguro

---

## 7. Comprobación con Postman

1. **Login**
   - `POST https://midominio.com/login/`
   - Django reenvía credenciales a PHP
   - Devuelve cookie de sesión (`sessionid`)
2. **Acceder a API**
   - `GET https://midominio.com/api/employees/`
   - Enviar cookie `sessionid`
   - Si la sesión es válida, responde con datos
3. **Logout**
   - `POST https://midominio.com/logout/`
   - Django borra sesión + avisa a PHP

---

