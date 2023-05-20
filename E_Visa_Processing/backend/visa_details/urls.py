"""
URL mappings for the visa_details API.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from visa_details import views

router = DefaultRouter()
router.register('', views.Visa_DetailsViewSet, basename='visa_details')

app_name = 'visa_details'

urlpatterns = [
    path('', include(router.urls)),
]
