from django.apps import apps
from django.contrib import admin

models = apps.get_models()
"""Model Register for Temporarily usage"""
for model in models:
    try:
        admin.site.register(model)
    except:
        pass