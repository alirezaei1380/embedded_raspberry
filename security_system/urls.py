from django.urls import path
from rest_framework import routers

from security_system.views import RaspberryView

router = routers.SimpleRouter()


urlpatterns = [
    path('password/', RaspberryView.as_view(
        {'post': 'create'}
    )),
]
