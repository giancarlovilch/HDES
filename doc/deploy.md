# 🚀 Despliegue

Este documento explica cómo desplegar el proyecto en producción.

---

## 1. Requisitos
- Python 3.10+
- PostgreSQL
- Servidor con Ubuntu/Debian o cPanel

## 2. Configuración de entorno
- Variables en `.env`
  - `DEBUG=False`
  - `SECRET_KEY=`
  - `DATABASE_URL=postgres://...`

## 3. Migraciones
```bash
python manage.py migrate
```

---

