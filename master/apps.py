from django.apps import AppConfig
from django.apps import apps


models = apps.get_models()

for model in models:
    admin.site.register(model)

