# 🔑 API en Django

Este documento describe los **endpoints del sistema Django**.

---

## 📋 Endpoints principales

### Empleados
- `GET /api/employees/`
- `POST /api/employees/`
- `GET /api/employees/{id}/`
- `PUT /api/employees/{id}/`
- `DELETE /api/employees/{id}/`

### Horarios
- `GET /api/schedule/`
- `POST /api/schedule/assign/`

### Reportes
- `GET /api/reports/employee/{id}/`

### Legal
- `GET /api/contracts/`
- `POST /api/contracts/`

### Skills
- `GET /api/skills/`
- `POST /api/skills/assign/`

---

## 🛠 Autenticación
- Token proporcionado por **API PHP**.
- Django solo consume datos → el login ocurre en PHP.

---

