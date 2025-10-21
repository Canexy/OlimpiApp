# Django OlimpiApp

Sistema de gestión para competiciones deportivas desarrollado con Django.

## Características Implementadas

### Modelos
- **Equipos**: Con opción olímpico o no
- **Participantes**: Relacionados con equipos, con validación de eliminación
- **Disciplinas**: Configuración de límites de equipos y participantes por equipo
- **Pistas**: Con opción de cubierta o no
- **Árbitros**: Datos de contacto
- **Encuentros**: Gestión de eventos con estados automáticos y validaciones

### Funcionalidades
- Validaciones de integridad de datos en modelos
- Panel de administración Django personalizado
- Gestión de relaciones muchos-a-muchos entre encuentros y equipos
- Estados automáticos de encuentros basados en fechas
- Prevención de eliminación de equipos con encuentros asociados

### Configuración
1. Instalar dependencias: `pip install django django-extensions python-dotenv`
2. Configurar variables de entorno en `.env`
3. Ejecutar migraciones: `python manage.py migrate`
4. Crear superusuario: `python manage.py createsuperuser`
5. Ejecutar servidor: `python manage.py runserver`

Accede al panel de administración en `/admin` para gestionar los datos.