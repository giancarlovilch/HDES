## 🗄️ Base de Datos

El sistema está respaldado por una **base de datos MySQL**, diseñada bajo el patrón **MVC** para mantener los datos organizados, seguros y accesibles.

------

### 📋 Tablas principales

1. **usuarios**
   - id_usuario (PK, autoincremental)
   - nombre_completo (VARCHAR)
   - username (VARCHAR, único)
   - password (VARCHAR, encriptada con hash)
   - rol (ENUM: 'admin', 'empleado', 'gerente')
   - fecha_registro (TIMESTAMP)

2. **productos**
   - id_producto (PK)
   - nombre_producto (VARCHAR)
   - precio (DECIMAL)
   - stock (INT)
   - categoria (VARCHAR)

3. **ventas**
   - id_venta (PK)
   - id_usuario (FK → usuarios)
   - id_producto (FK → productos)
   - cantidad (INT)
   - fecha_venta (TIMESTAMP)

4. **arqueo_caja**
   - id_arqueo (PK)
   - id_usuario (FK → usuarios)
   - monto_inicial (DECIMAL)
   - monto_final (DECIMAL)
   - fecha (DATE)

---

### 📊 Diagrama Entidad-Relación

```mermaid
erDiagram
    USUARIOS {
        int id_usuario PK
        string nombre_completo
        string username
        string password
        string rol
        timestamp fecha_registro
    }

    PRODUCTOS {
        int id_producto PK
        string nombre_producto
        decimal precio
        int stock
        string categoria
    }

    VENTAS {
        int id_venta PK
        int id_usuario FK
        int id_producto FK
        int cantidad
        timestamp fecha_venta
    }

    ARQUEO_CAJA {
        int id_arqueo PK
        int id_usuario FK
        decimal monto_inicial
        decimal monto_final
        date fecha
    }

    USUARIOS ||--o{ VENTAS : "realiza"
    PRODUCTOS ||--o{ VENTAS : "se venden"
    USUARIOS ||--o{ ARQUEO_CAJA : "controla"
```

------

### 🔐 Seguridad en la BD

- Contraseñas guardadas con **hash (SHA-256/BCrypt)**.
- Usuarios identificados por **username único** (no correo).
- Logs de auditoría para controlar actividades sensibles.
- Restricciones de **FK** para mantener integridad referencial.

------

### 🚀 Próximos pasos en la BD

- Agregar tabla de **asistencias** para el control de personal.
- Implementar **backups automáticos.
- Optimizar con **índices** en campos más usados (username, fecha_venta).