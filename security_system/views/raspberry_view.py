from rest_framework.viewsets import ModelViewSet

from security_system.models import Raspberry
from security_system.serializers.raspberry_serializer import RaspberrySerializer


class RaspberryView(ModelViewSet):
    queryset = Raspberry.objects.all()
    serializer_class = RaspberrySerializer
