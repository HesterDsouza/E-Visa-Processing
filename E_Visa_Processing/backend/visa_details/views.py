from django.shortcuts import render


# Create your views here.
"""
Views for the Visa_Details API.
"""
from visa_details import serializers
from rest_framework.response import Response
from core.models import Visa_Details
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class Visa_DetailsViewSet(ViewSet):
    """View to Retrieve, Manage & Destroy visa_details."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.Visa_DetailsSerializer

    def list(self,request):
        """Get list of visa_details."""
        try:
            visa_details_objs = Visa_Details.objects.all()
            serializer = serializers.Visa_DetailsSerializer(visa_details_objs, many=True)

            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def retrieve(self, request, pk=None):
        """Retrieve visa_details details."""
        try:
            id = pk
            if id is not None:
                visa_details_obj = serializers.Visa_Details.objects.get(id=id)
                serializer = serializers.Visa_DetailsSerializer(visa_details_obj)
                return Response({
                    'status':status.HTTP_200_OK,
                    'data':serializer.data
                })
        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def create(self, request):
        """Get request data & create visa_details."""
        try:
            serializer = serializers.Visa_DetailsSerializer(data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data.'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'visa_details added successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def update(self,request, pk):
        """Get request data & update visa_details."""
        try:
            id = pk
            visa_details_obj = Visa_Details.objects.get(pk=id)
            serializer = serializers.Visa_DetailsSerializer(visa_details_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data.'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'visa_details updated successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def partial_update(self,request, pk):
        """Get request data & patch visa_details."""
        try:
            id = pk
            visa_details_obj = Visa_Details.objects.get(pk=id)
            serializer = serializers.Visa_DetailsSerializer(visa_details_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data.'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'visa_details patched successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def destroy(self,request, pk):
        """Remove visa_details."""
        try:
            id = pk
            visa_details_obj = Visa_Details.objects.get(pk=id)

            visa_details_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'visa_details deleted successfully.'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
