"""
Serializers for the visa API View.
"""
from rest_framework import serializers

from core.models import Visa

class VisaSerializer(serializers.ModelSerializer):
    """VisaSerializer to get personal details."""
    name = serializers.CharField(max_length=255,allow_blank=True)
    email = serializers.EmailField(max_length=255,allow_blank=True)
    mob_no = serializers.IntegerField()
    address = serializers.CharField(max_length=255,allow_blank=True)
    state = serializers.CharField(max_length=255,allow_blank=True)
    city = serializers.CharField(max_length=255,allow_blank=True)
    pincode = serializers.IntegerField()
    aadhar = serializers.CharField(max_length=255,allow_blank=True)
    pancard = serializers.CharField(max_length=255,allow_blank=True)
    gender = serializers.CharField(max_length=255,allow_blank=True)
    d_o_b = serializers.DateField()
    age = serializers.IntegerField()


    class Meta:
        model = Visa
        # fields = ['id','name','email','mob_no','address','state','city','pincode','aadhar','pancard','gender','d_o_b','age']
        # exclude = ['id']
        fields = '__all__'
        read_only_fields = ['id']

    def validate(self, data):

        if len(data['name']) == 0:
            raise serializers.ValidationError({'error':'name required'})
        
        return data