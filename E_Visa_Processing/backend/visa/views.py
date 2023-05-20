from django.shortcuts import render

# Create your views here.
"""
Views for the visa API.
"""
from visa import serializers
from rest_framework.response import Response
from core.models import Visa
from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class VisaViewSet(ViewSet):
    """View to Retrieve, Manage & Destroy visa."""
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.VisaSerializer

    def list(self,request):
        """Get list of visas."""
        try:
            visa_objs = Visa.objects.all()
            serializer = serializers.VisaSerializer(visa_objs, many=True)

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
        """Retrieve visa details."""
        try:
            id = pk
            if id is not None:
                visa_obj = serializers.Visa.objects.get(id=id)
                serializer = serializers.VisaSerializer(visa_obj)
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
        """Get request data & create visa."""
        try:
            serializer = serializers.VisaSerializer(data = request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_201_CREATED,
                'data':serializer.data,
                'message':'visa added successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })


    def update(self,request, pk):
        """Get request data & update visa."""
        try:
            id = pk
            visa_obj = Visa.objects.get(pk=id)
            serializer = serializers.VisaSerializer(visa_obj, data=request.data)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'visa updated successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def partial_update(self,request, pk):
        """Get request data & patch visa."""
        try:
            id = pk
            visa_obj = Visa.objects.get(pk=id)
            serializer = serializers.VisaSerializer(visa_obj, data=request.data, partial=True)

            if not serializer.is_valid():
                print(serializer.errors)
                return Response({
                    'status':status.HTTP_400_BAD_REQUEST,
                    'errors':serializer.errors,
                    'message':'Invalid data'
                })

            serializer.save()
            return Response({
                'status':status.HTTP_200_OK,
                'data':serializer.data,
                'message':'visa patched successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })

    def destroy(self,request, pk):
        """Remove visa."""
        try:
            id = pk
            visa_obj = Visa.objects.get(pk=id)

            visa_obj.delete()
            return Response({
                'status':status.HTTP_200_OK,
                'message':'visa deleted successfully'
            })

        except Exception as e:
            print(e)
            raise APIException({
                'message':APIException.default_detail,
                'status':APIException.status_code
            })
