from django.contrib import admin
# .models tells python to look from models.py in the same directory as this file (admin.py)
from .models import Entry, Topic

# Register your models here.
# Registering models allows an admin user to add, update and delete records for these model types
admin.site.register(Topic)
admin.site.register(Entry)