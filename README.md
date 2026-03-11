# Proyecto Final - Barbería del Oeste

Sistema de gestión de turnos para barbería desarrollado con Python y Django. Incluye autenticación de usuarios, gestión de servicios, reserva de turnos, panel de administración y diseño moderno con Bootstrap.

## 🚀 Características

- **Autenticación de Usuarios**
  - Registro e inicio de sesión de usuarios
  - Reserva de turnos según disponibilidad
  - Visualización de turnos del usuario
  - Cancelación de turnos
  - CRUD de servicios
  - Panel de administración de turnos
  - Cambio de estado de turnos (Atendido, Cancelado, Ausente)
  - Filtro de turnos por fecha
  - Página About

## 🛠️ Instalación

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Martiherenu1/ProyectoFinalCoderHousePythonDjango.git
   cd ProyectoFinalCoderHousePythonDjango
   ```

2. **Crear y activar entorno virtual**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar base de datos**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario (opcional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Ejecutar el servidor**
   ```bash
   python manage.py runserver
   ```

## 👨‍💻 Autor

**Martiniano Hereñu**
- GitHub: [github.com/Martiherenu1](https://github.com/Martiherenu1)
- Email: [martinianoherenu@gmail.com]
---
