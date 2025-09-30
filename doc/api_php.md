# 🌐 API PHP Externa - Sistema de Ventas

Este documento explica cómo se consumen los usuarios desde el sistema PHP.

---

## 🔄 Flujo
1. Usuario inicia sesión en el sistema PHP.
2. PHP genera un **token**.
3. Django consume `/api/user/{token}` para obtener datos del usuario.

---

## 📋 Ejemplo JSON de respuesta
```json
{
  "id": 12,
  "username": "jlopez",
  "nombre": "Juan Lopez",
  "rol": "Empleado",
  "skills": ["Caja", "Ventas"]
}
```

---

