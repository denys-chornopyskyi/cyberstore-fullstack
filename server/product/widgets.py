from django import forms
from ast import literal_eval

from django.http import QueryDict
from django.utils.termcolors import color_names


class JsonKeyValueWidget(forms.Widget):
    template_name = 'widgets/json_key_value_widget.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        if literal_eval(value):
            context['widget']['pairs'] = [{'key': k, 'value': v} for k, v in literal_eval(value).items()]
        else:
            context['widget']['pairs'] = [{'key': '', 'value': ''}]
        return context

    def value_from_datadict(self, data: QueryDict, files, name):
        keys = data.getlist(f'{name}_key')
        values = data.getlist(f'{name}_value')
        print(keys)
        print(values)
        result = dict(zip(keys, values))
        print(result)
        return result
