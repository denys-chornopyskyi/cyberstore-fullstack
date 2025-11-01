from django import forms

class JsonKeyValueWidget(forms.Widget):
    template_name = 'widgets/json_key_value_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        print(isinstance(value, dict))
        return context

