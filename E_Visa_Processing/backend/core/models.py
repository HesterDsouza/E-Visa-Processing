"""
Database models.
"""
from django.db import models

class Visa(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    mob_no = models.IntegerField()
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    pincode = models.IntegerField()
    aadhar = models.FileField(upload_to="visa/",max_length=255)
    pancard = models.FileField(upload_to="visa/",max_length=255)
    gender = models.CharField(max_length=255)
    d_o_b = models.DateField()
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Visa_Details(models.Model):
    nationality = models.CharField(max_length=255)
    destination_country = models.CharField(max_length=255)
    stay_duration = models.IntegerField()
    photo = models.FileField(upload_to="visa_details/",max_length=255)
    sign = models.FileField(upload_to="visa_details/",max_length=255)
    visa = models.ForeignKey(Visa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nationality