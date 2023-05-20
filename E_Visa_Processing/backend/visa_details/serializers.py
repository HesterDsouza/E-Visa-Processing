"""
Serializers for the visa API View.
"""
from rest_framework import serializers

from core.models import Visa_Details
from visa.serializers import VisaSerializer

class Visa_DetailsSerializer(serializers.ModelSerializer):
    """Visa_DetailsSerializer to get visa details."""
    visa_id = serializers.IntegerField(write_only=True)
    visa = VisaSerializer(read_only=True)
    nationality = serializers.CharField(max_length=255,allow_blank=False)
    destination_country = serializers.CharField(max_length=255,allow_blank=False)
    stay_duration = serializers.IntegerField()
    photo = serializers.CharField(max_length=255,allow_blank=False)
    sign = serializers.CharField(max_length=255,allow_blank=False)

    class Meta:
        model = Visa_Details
        fields = ['id', 'nationality','destination_country','stay_duration','photo','sign','visa','visa_id']
        # exclude = ['id']
        #read_only_fields = ['id']