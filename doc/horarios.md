# 🗓️ Módulo de Horarios

El módulo de **Horarios** gestiona la asignación de empleados a turnos en días específicos.  
Permite visualizar qué trabajadores están disponibles, asignarles posiciones y resetear las asignaciones cuando sea necesario.

---

## 📋 Funcionalidades

- 📑 **Ver horarios** → lista de días con los asientos (turnos) asignados.  
- ➕ **Asignar empleados** a un día/turno específico.  
- 🔄 **Resetear asignaciones** (limpia todos los horarios).  
- 👥 **Ver empleados disponibles** (no asignados).  

---

## 🗂️ Modelos relacionados

- **Day**
  - `name` → Nombre del día (ej. Lunes, Martes…).  

- **Seat**
  - `day` → FK a `Day`.  
  - `worker` → FK a `Worker`.  
  - `position` → Texto libre indicando puesto/turno.  

👉 Relación:  
Un **Day** puede tener muchos **Seat**, y cada **Seat** está ocupado por un `Worker`.

---

## 🎨 Templates

- `schedule/seat_list.html` → vista principal de horarios.  
  - Lista de días.  
  - Para cada día, muestra los trabajadores asignados.  
  - Permite asignar nuevos trabajadores mediante formulario.  

---

## 🔑 Endpoints API

- `GET /api/schedule/`  
  Lista de días con los asientos y empleados asignados.

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "name": "Lunes",
    "seats": [
      { "id": 10, "worker": { "id": 2, "name": "Carlos Pérez" }, "position": "Caja" },
      { "id": 11, "worker": { "id": 3, "name": "María López" }, "position": "Atención" }
    ]
  },
  {
    "id": 2,
    "name": "Martes",
    "seats": []
  }
]
```

---

## 🖥️ Vistas Django

- **SeatListView** (`seat_list.html`)
  - GET → muestra días y asignaciones actuales.
  - POST → permite asignar un trabajador a un día.
- **reset_assignments**
  - Limpia todas las asignaciones (`Seat.objects.all().delete()`).
  - Redirige con mensaje de éxito.

---

## 📊 Ejemplo en Interfaz

1. Entrar a **Empleados → Asignar Horarios**.
2. Ver lista de días de la semana.
3. Para cada día:
   - Si ya hay empleados asignados → aparecen listados.
   - Si no → se puede agregar uno.
4. Botón **Resetear** → elimina todas las asignaciones actuales.

---

## 📬 Ejemplo en Postman

### Listar horarios

```
GET http://127.0.0.1:8000/api/schedule/
Cookie: sessionid=<django_session>
```

### Asignar skill (turno)

```
POST http://127.0.0.1:8000/api/skills/assign/
Content-Type: application/json
Cookie: sessionid=<django_session>

{
  "worker_id": 2,
  "skill_id": 3,
  "level": 4
}
```

---
