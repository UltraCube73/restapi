from django.contrib import admin

from .models import Pharmacy, Medication

admin.site.register(Pharmacy)
admin.site.register(Medication)