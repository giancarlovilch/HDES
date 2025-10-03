# 🗄️ Modelo de Datos - HDES Intranet

Este documento describe la estructura de base de datos utilizada en **HDES**, incluyendo los modelos principales, sus relaciones y un diagrama ER.

---

## 📋 Modelos

### 👩‍💼 Worker
Representa a un empleado.
- `name` → Nombre completo.
- `position` → Cargo/puesto.
- `salary` → Salario base.

### ⭐ Skill
Representa una habilidad.
- `name` → Nombre de la habilidad (ej: "Ventas", "Atención al cliente").

### 🔗 WorkerSkill
Relación **muchos a muchos** entre `Worker` y `Skill`.
- `worker` → FK a `Worker`.
- `skill` → FK a `Skill`.
- `level` → Nivel de habilidad (1–5).

### 📅 Day
Representa un día de la semana.
- `name` → Nombre (Lunes, Martes, …).

### 🪑 Seat
Representa la asignación de un trabajador en un día y turno.
- `day` → FK a `Day`.
- `worker` → FK a `Worker`.
- `position` → Posición o puesto en el día.

### 📊 Report
Reporte de desempeño de un trabajador.
- `worker` → FK a `Worker`.
- `performance` → Calificación (1–10).
- `salary` → Salario registrado en ese reporte.
- `date` → Fecha del reporte.

---

## 🗺️ Diagrama ER (Mermaid)

```mermaid
erDiagram
    Worker ||--o{ WorkerSkill : "tiene"
    Skill  ||--o{ WorkerSkill : "asignada"

    Worker ||--o{ Report : "genera"
    Worker ||--o{ Seat   : "ocupa"

    Day    ||--o{ Seat   : "contiene"

    Worker {
        int id PK
        string name
        string position
        decimal salary
    }

    Skill {
        int id PK
        string name
    }

    WorkerSkill {
        int id PK
        int worker_id FK
        int skill_id FK
        int level
    }

    Report {
        int id PK
        int worker_id FK
        int performance
        decimal salary
        date date
    }

    Day {
        int id PK
        string name
    }

    Seat {
        int id PK
        int day_id FK
        int worker_id FK
        string position
    }
```

---

