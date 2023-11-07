from rest_framework import serializers

from computer_tracking.models import Computer


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = (
            'id', 'mac_address', 'computer_name', 'ip_address',
            'employee', 'description'
        )

    def employee(self, obj):
        return obj.employee.abbreviation
