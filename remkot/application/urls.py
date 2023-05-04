from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('application/', AddClient.as_view(), name='add_client'),
    # path('client/add/',),
    # path('client/edit/',),
]
