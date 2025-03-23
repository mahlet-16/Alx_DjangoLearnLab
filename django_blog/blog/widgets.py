# blog/widgets.py
from django import forms
from django.forms.widgets import SelectMultiple

class TagWidget(SelectMultiple):
    def __init__(self, *args, **kwargs):
        # Optionally pass additional arguments if needed
        super().__init__(*args, **kwargs)

    def render(self, name, value, attrs=None, renderer=None):
        """
        Render the widget in HTML. This will render a <select> element
        with multiple options, as a list of tags for selecting.
        """
        output = super().render(name, value, attrs, renderer)
        # You can add custom attributes, JavaScript, or any additional 
        # processing here for your custom behavior, such as autocomplete
        return f'<div class="tags-widget">{output}</div>'
