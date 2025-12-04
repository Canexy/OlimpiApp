from django.db import models
from wagtail.models import Page
# from wagtail.models import Orderable
# from modelcluster.models import ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    template = "cms/home_page.html"
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]

class BlogIndexPage(Page):
    template = "blog/blog_index_page.html"
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]

class BlogPage(Page):
    template = "blog/blog_page.html"
    date = models.DateField("Date")
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('date'),
    ]

