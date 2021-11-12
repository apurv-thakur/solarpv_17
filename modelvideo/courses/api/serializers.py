from rest_framework import serializers
from ..models import organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = ["OrgCe", "OrgName", "datejoined", "address", "city", "state", "phone"]
