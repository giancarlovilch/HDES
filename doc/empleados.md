# 👩‍💼 Módulo de Empleados

El módulo de **Empleados** gestiona toda la información relacionada con los trabajadores de la empresa:  
registro, edición, eliminación, listado y asociación con **horarios, reportes y skills**.

---

## 📋 Funcionalidades

- 📑 **Listado de empleados** con paginación.
- ➕ **Agregar empleado** con nombre, cargo y salario.
- ✏️ **Editar información** de un empleado.
- 🗑️ **Eliminar empleado** de la base de datos.
- 🔗 Integración con:
  - **Horarios** → asignar trabajadores a turnos/días.
  - **Reportes** → generar reportes de desempeño y salario.
  - **Skills** → asignar habilidades con nivel.

---

## 🗂️ Modelos relacionados

- **Worker**
  - `name` → Nombre completo.
  - `position` → Cargo o puesto.
  - `salary` → Salario base.

---

## 🎨 Templates

- `schedule/worker_list.html` → listado de empleados.
- `schedule/worker_form.html` → formulario para crear/editar.
- `schedule/worker_confirm_delete.html` → confirmación antes de eliminar.

👉 Todos estos templates extienden de `base.html` y usan Bootstrap 5 para la apariencia.

---

## 🔑 Endpoints API

- `GET /api/employees/` → Listado de empleados.
- `POST /api/employees/` → Crear nuevo empleado.
- `GET /api/employees/{id}/` → Obtener detalles de un empleado.
- `PUT /api/employees/{id}/` → Editar empleado.
- `DELETE /api/employees/{id}/` → Eliminar empleado.

Ejemplo de creación:

```http
POST /api/employees/
Content-Type: application/json
Cookie: sessionid=<django_session>

{
  "name": "Carlos Pérez",
  "position": "Vendedor",
  "salary": 1200
}
```

Respuesta:

```
{
  "id": 5,
  "name": "Carlos Pérez",
  "position": "Vendedor",
  "salary": 1200
}
```

---

## 🖥️ Vistas Django

- **WorkerListView** → lista empleados (`worker_list.html`).
- **WorkerCreateView** → formulario para alta (`worker_form.html`).
- **WorkerUpdateView** → formulario para editar.
- **WorkerDeleteView** → confirmación y borrado (`worker_confirm_delete.html`).

👉 Todas integran `messages.success` para notificar al usuario.

---

## 📊 Ejemplo en Interfaz

1. Acceder al menú **Empleados → Lista de Empleados**.
2. Ver tabla con empleados registrados.
3. Botón ➕ → abre formulario para registrar uno nuevo.
4. Desde la lista, cada empleado tiene botones:
   - ✏️ Editar
   - 🗑️ Eliminar
   - 🔗 Asignar a horario
   - ⭐ Asignar skill

---