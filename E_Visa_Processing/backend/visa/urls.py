"""
URL mappings for the visa API.
"""
from django.urls import (
    path,
    include,
)
from rest_framework.routers import DefaultRouter

from visa import views

router = DefaultRouter()
router.register('', views.VisaViewSet, basename='visa')

app_name = 'visa'

urlpatterns = [
    path('', include(router.urls)),
]