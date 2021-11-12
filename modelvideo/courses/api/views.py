from rest_framework import generics
from ..models import organization
from .serializers import OrganizationSerializer


class OrganizationListView(generics.ListAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationDetailView(generics.RetrieveAPIView):
    queryset = organization.objects.all()
    serializer_class = OrganizationSerializer
