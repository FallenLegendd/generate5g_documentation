from django.shortcuts import render

from django.shortcuts import render
from django.apps import apps

def database_docs(request):
    models = apps.get_models()
    model_docs = []
    for model in models:
        model_docs.append({
            'name': model.__name__,
            'fields': [field.name for field in model._meta.get_fields()],
        })
    return render(request, 'docs/database_docs.html', {'models': model_docs})