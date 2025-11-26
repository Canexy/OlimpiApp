from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

# No implementado aún.
# Formulario básico para obtener un nombre.