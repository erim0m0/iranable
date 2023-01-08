from typing import List, Dict

from rest_framework.generics import (
    UpdateAPIView, CreateAPIView, RetrieveDestroyAPIView, ListAPIView,
)

from django.shortcuts import get_object_or_404

from accounts.api.serializers import (
    CompanyProfileSerializer, CompanyProfileCreateSerializer,
    CompaniesListSerializer
)
from accounts.models.company import CompanyProfile
from permissions import IsOperatorOrStaff, IsOperatorOrNot


class CompaniesList(ListAPIView):
    serializer_class = CompaniesListSerializer

    def get_queryset(self):
        return CompanyProfile.objects.only(
            "id", "name", "logo"
        )


class CompanyProfileDetailDestroy(RetrieveDestroyAPIView):
    serializer_class = CompanyProfileSerializer
    permission_classes = [
        IsOperatorOrStaff
    ]

    def get_object(self):
        obj = get_object_or_404(
            CompanyProfile.objects.defer(
                "created_at",
                "number_of_ad"
            ).select_related(
                "operator"
            ), pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class CompanyProfileUpdate(UpdateAPIView):
    serializer_class = CompanyProfileCreateSerializer
    permission_classes = [
        IsOperatorOrStaff
    ]

    def get_object(self):
        obj = get_object_or_404(
            CompanyProfile.objects.defer(
                "created_at",
                "operator",
                "number_of_ad"
            ), pk=self.kwargs.get("pk")
        )
        # May raise a permission denied
        self.check_object_permissions(self.request, obj)
        return obj


class CompanyProfileCreate(CreateAPIView):
    serializer_class = CompanyProfileCreateSerializer
    queryset = CompanyProfile.objects.all()
    permission_classes = [
        IsOperatorOrNot
    ]

    def perform_create(self, serializer):
        serializer.save(
            organizational_interface=self.request.user
        )
