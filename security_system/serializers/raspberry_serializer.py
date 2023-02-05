from rest_framework.serializers import ModelSerializer

from security_system.models import Raspberry


class RaspberrySerializer(ModelSerializer):

    class Meta:
        model = Raspberry
        fields = ('admin_code', 'user_code')
