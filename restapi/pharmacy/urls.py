from django.urls import path
from .views import MedicationView, PharmacyView

app_name = 'medications'

urlpatterns = [
    path('medication', MedicationView.as_view()),
    path('pharmacy', PharmacyView.as_view())
]