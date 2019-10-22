from rest_framework  import serializers
from .models import Device

class WarningDevices(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('id', 'name', 'type', 'address', 'latitude','longitude','radius')
