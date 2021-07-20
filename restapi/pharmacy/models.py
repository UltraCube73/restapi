from django.db import models

class Pharmacy(models.Model):
    p_name = models.CharField(max_length=20)
    p_city = models.CharField(max_length=20)

class Medication(models.Model):
    m_name = models.CharField(max_length=30)
    m_manufacuter_city = models.CharField(max_length=20)
    m_price = models.IntegerField()
    m_pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE, related_name='medication_set')