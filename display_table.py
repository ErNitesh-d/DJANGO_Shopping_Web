#First command in terminal
#python manage.py shell 

#Then Run this code in that shell\
from django.db import connection
from django.apps import apps

# Get all installed models
installed_models = apps.get_models()

# List tables with their attributes
for model in installed_models:
    print(f"Table: {model._meta.db_table}")
    print("Attributes:")
    for field in model._meta.fields:
        print(f"- {field.name}: {field.get_internal_type()}")
    print()
