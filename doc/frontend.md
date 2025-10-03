# 🎨 Frontend - HDES Intranet

El **frontend** de HDES está basado en **Django Templates** con **Bootstrap 5** y estilos personalizados.  
Su objetivo es proveer una interfaz **simple, moderna y responsive** para la gestión empresarial.

---

## 📋 Plantillas principales

### 🏗️ `base.html`
- Layout principal que heredan todas las demás vistas.
- Contiene:
  - **Navbar** con módulos del sistema (Inventario, Ventas, Empleados, Reportes, etc.).
  - Botón de usuario (👤 Perfil, 🚪 Cerrar Sesión).
  - **Footer** con datos de contacto y enlaces legales.
- Extiende con bloques:
  - `{% block title %}` → título dinámico.
  - `{% block content %}` → contenido de cada página.
  - `{% block extra_css %}` y `{% block extra_js %}` → personalización.

👉 Punto clave: el botón de **Cerrar Sesión** está ligado a `{% url 'php_logout' %}`, que invalida la sesión en PHP y Django.

### 🖥️ `index.html`
- Dashboard principal.
- Muestra:
  - Bienvenida personalizada con nombre/rol del usuario.
  - Accesos directos (Inventario, Ventas, Empleados, Reportes).
  - Tarjetas de estadísticas:
    - Productos en stock.
    - Ventas del día.
    - Empleados activos.
    - Alertas de stock.

👉 Es la página que se abre tras el login exitoso.

### 🔑 `login.html`
- Formulario de acceso al sistema.
- Usa método `POST` a `/login/` que reenvía credenciales al **API PHP**.
- Campos:
  - Usuario.
  - Contraseña.
- Compatible con **CSRF Token** de Django.

### 📝 `placeholder.html`
- Plantilla de “en construcción”.
- Reutiliza `base.html` y sirve como página temporal para módulos futuros.

---

## 🎨 Estilos (CSS)

### 📄 `dashboard.css`
- Personaliza la apariencia del **dashboard**.
- Principales reglas:
  - **Tarjetas con colores gradientes** para diferenciar estadísticas.
  - Textos en **negrita** y tamaños ajustados en móvil.
  - Botón de **logout destacado en rojo** dentro del menú de usuario.

Ejemplo:
```css
.card:nth-child(1) .card-body { background: linear-gradient(135deg, #e3f2fd, #bbdefb); }
.card:nth-child(2) .card-body { background: linear-gradient(135deg, #e8f5e9, #c8e6c9); }
.card .card-text { font-size: 1.2rem; font-weight: bold; }
```

### 📄 `style.css`

- Contiene ajustes globales de apariencia.
- Define márgenes, tipografía y estilos compartidos entre vistas.
- Refuerza el diseño responsive.

------

## 📱 Responsive Design

- Basado en **Bootstrap 5 grid system**.
- Navbar colapsa en pantallas pequeñas → botón hamburguesa.
- Botones grandes (`btn-lg w-100`) para facilitar uso en móviles.
- Media queries en CSS ajustan tamaños de texto y márgenes.

------

## 🖼️ Flujo visual

```
graph TD
    A[login.html] -->|Acceso correcto| B[index.html Dashboard]
    B --> C[Inventario]
    B --> D[Ventas]
    B --> E[Empleados]
    B --> F[Reportes]
    B --> G[Legal]
    base.html --> A
    base.html --> B
    base.html --> Placeholder
```

---