
#### Did - 03/12
**Blog Templates**
Creación de templates para el añadido *blog*, con la función de creación de nuevas entradas en el mismo.

- Modificado:
/cms/models.py

- Añadido:
/templates/blog/blog_index_page.html
/templates/blog/blog_page.html

**olimpi_app/urls.py**
Ahora se usan rutas absolutas de Wagtail mediante *wagtail_urls*. La nueva creación de páginas dentro del proyecto recaen sobre los nuevos templates creados.

http://127.0.0.1:8000/
http://127.0.0.1:8000/blog/
http://127.0.0.1:8000/blog/welcome/



**Cambios a realizar próximamente:**
- Añadir los .html de *register_par/* dentro de *templates/app/*.
- Creación e implementación de MySQL (AWS).

https://docs.wagtail.org/en/stable/getting_started/tutorial.html