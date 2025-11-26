
# (13/11)
## Hecho:
- Instalación de Wagtail mediante Pip.
- Añadido de Wagtail en INSTALLED_APPS y MIDDLEWARE en `/olimpi_app/settings.py`, además de configuración extra necesarias a pie de página.
- Modificación de `/olimpi_app/urls.py` para añadir ruta a **Administración de Wagtail** (*/wadmin*), `/documents` (aún sin implementar bien) y *recursive path* para `/register_par/urls.py`.
- Acción *makemigrations* y *migrate* sobre los cambios.

## Cosas que aún no sé del todo.
- Origen y/o uso de `/admin` por parte de Wagtail (no sé dónde crea el archivo o cómo lo crea).
- Uso del propio Wagtail en general.

---

# (19/11)
## Hecho:
- Añadido *WAGTAILADMIN_BASE_URL* a `olimpi_app/settings.py`, resolviendo así un aviso de Wagtail en la ejecución del servidor.


# (24/11) Horario fuera de clase.
## Hecho:

- Quise adelantar un poco trabajo y estuve investigando sobre el despliegue en AWS. Parecido a ello, había trabajado anteriormente con Render y probé a realizar un despliegue rápido sobre el mismo. Creé un repositorio espejo del actual, tocando x configuraciones y pasando todas las variables de entorno a Render, consiguiendo así un despliegue del mismo:

`https://rendolimpiapp.onrender.com/`
`https://rendolimpiapp.onrender.com/equipos/`
`https://rendolimpiapp.onrender.com/admin/`
`https://rendolimpiapp.onrender.com/wadmin/`

`https://github.com/Canexy/RendolimpiApp`

- Además, creé un repositorio de pruebas para empezar a investigar con AWS, de nuevo, espejo al original:

`https://github.com/Canexy/AWSolimpiApp`

# (26/11)
## Hecho:

Indagué en el hecho de crear páginas con Wagtail, resolviendo el problema de añadirlo a un proyecto Django ya existente.

- Añadí 'cms' a aplicaciones instaladas, así como la ruta estática al media existente.
- Creé la aplicación 'home' de Wagtail, creando así su modelo para poder crear nuevas páginas.
- Creé un template para que use el propio modelo (único por el momento, siendo la por defecto), pudiendo así ejecutarse en `127.0.0.1:8000/blog/`

`blog` hace referencia a `wagtail_urls`, en `urls.py` de mi proyecto.

- Añadí el template `base.html` para que se ejecute por defecto en la ruta `127.0.0.1:8000`, donde antes no aparecía nada.

## Observaciones:

Hoy entiendo mucho más cómo funciona Wagtail y he definido la estructura mental que tengo sobre la composición de mi página (donde estará cada cosa).