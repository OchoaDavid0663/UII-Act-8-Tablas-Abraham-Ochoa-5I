from django.contrib import admin

# Register your models here.
from .models import Medicamento # Import your Medicamento model

# Register your models here.

# Simple registration: This makes the Medicamento model visible in the admin.
admin.site.register(Medicamento)