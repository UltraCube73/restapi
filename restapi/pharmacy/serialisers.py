from rest_framework import serializers

from .models import Medication

class MedicationSerialiser(serializers.Serializer):
    m_name = serializers.CharField(max_length=30)
    m_manufacuter_city = serializers.CharField(max_length=20)
    m_price = serializers.IntegerField()
    m_pharmacy_id = serializers.IntegerField()
    def create(self, validated_data):
        return Medication.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.m_name = validated_data.get('m_name', instance.m_name)
        instance.m_manufacuter_city = validated_data.get('m_manufacuter_city', instance.m_manufacuter_city)
        instance.m_price = validated_data.get('m_price', instance.m_price)
        instance.m_pharmacy_id = validated_data.get('m_pharmacy_id', instance.m_pharmacy_id)
        instance.save()
        return instance


class PharmacySerialiser(serializers.Serializer):
    p_name = serializers.CharField(max_length=20)
    p_city = serializers.CharField(max_length=20)