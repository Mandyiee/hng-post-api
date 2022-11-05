from django.urls import path
from .views import receive_operation

urlpatterns = [
    path('', receive_operation),
]
