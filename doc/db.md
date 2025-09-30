# 🗄️ Base de Datos

Este documento describe la **estructura de la base de datos** y su integración con Django ORM.

---

## 📋 Modelos principales
- Usuario
- Empleado
- Horario
- Reporte
- Contrato
- Skill

---

## 📊 Diagrama Entidad-Relación
```mermaid
erDiagram
    USUARIO ||--o{ EMPLEADO : "gestiona"
    EMPLEADO ||--o{ HORARIO : "tiene"
    EMPLEADO ||--o{ REPORTE : "genera"
    EMPLEADO ||--o{ CONTRATO : "firma"
    EMPLEADO ||--o{ SKILL : "posee"
```

---

## 🔐 Seguridad

- Contraseñas hasheadas (PBKDF2 / Argon2).
- Migraciones controladas con `makemigrations` y `migrate`.
- Posibles auditorías con señales de Django.

---
