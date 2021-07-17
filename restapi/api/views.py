from rest_framework.generics import get_object_or_404
from .serialisers import MedicationSerialiser, PharmacySerialiser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Pharmacy, Medication

class MedicationView(APIView):

    def get(self, request):
        if request.GET.get('id') != None:
            medications = Medication.objects.filter(id=request.GET.get('id')).first()
            serialiser = MedicationSerialiser(medications)
        elif request.GET.get('ph') != None:
            pharmacy = Pharmacy.objects.filter(id=request.GET.get('ph')).first()
            medications = pharmacy.medication_set.all()
            serialiser = MedicationSerialiser(medications, many=True)
        else:
            medications = Medication.objects.all()
            serialiser = MedicationSerialiser(medications, many=True)

        return Response({'medications': serialiser.data})

    def post(self, request):
        medication = request.data.get('medication')
        serialiser = MedicationSerialiser(data=medication)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
        return Response({'ok': 'Medication created successfully'})

    def put(self, request):
        medication_saved = get_object_or_404(Medication.objects.all(), pk=request.GET.get('id'))
        data = request.data.get('medication')
        serialiser = MedicationSerialiser(instance=medication_saved, data=data, partial=True)
        if serialiser.is_valid(raise_exception=True):
            serialiser.save()
        return Response({'ok': 'Medication updated successfully'})


class PharmacyView(APIView):

    def get(self, request):
        if request.GET.get('city') != None:
            pharmacies = Pharmacy.objects.filter(p_city=request.GET.get('city'))
        else:
            pharmacies = Pharmacy.objects.all()
        serialiser = PharmacySerialiser(pharmacies, many=True)

        return Response({"pharmacies": serialiser.data})

