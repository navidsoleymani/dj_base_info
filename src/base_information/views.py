from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from .models import (
    Header as BaseInformationHeaderModel,
    BaseInformation as BaseInformationModel,
)
from .serializers import (
    CreateHeader as BaseInformationHeaderCreateModelSerializer,
    RetrieveHeader as BaseInformationHeaderRetrieveModelSerializer,
    ListHeader as BaseInformationHeaderListModelSerializer,
    UpdateHeader as BaseInformationHeaderUpdateModelSerializer,
    DestroyHeader as BaseInformationHeaderDestroyModelSerializer,

    CreateBaseInformation as BaseInformationCreateModelSerializer,
    RetrieveBaseInformation as BaseInformationRetrieveModelSerializer,
    ListBaseInformation as BaseInformationListModelSerializer,
    UpdateBaseInformation as BaseInformationUpdateModelSerializer,
    DestroyBaseInformation as BaseInformationDestroyModelSerializer,
)


class Header:
    queryset = BaseInformationHeaderModel.objects.filter(is_active=True).all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('is_active',)
    search_fields = ('pk', 'title', 'code',)
    ordering_fields = ('pk', 'title', 'code',)
    lookup_field = 'id'


class CreateHeader(Header, CreateAPIView):
    serializer_class = BaseInformationHeaderCreateModelSerializer


class ListHeader(Header, ListAPIView):
    serializer_class = BaseInformationHeaderListModelSerializer


class RetrieveHeader(Header, RetrieveAPIView):
    serializer_class = BaseInformationHeaderRetrieveModelSerializer


class UpdateHeader(Header, UpdateAPIView):
    serializer_class = BaseInformationHeaderUpdateModelSerializer


class DestroyHeader(Header, DestroyAPIView):
    serializer_class = BaseInformationHeaderDestroyModelSerializer


class BaseInformation:
    queryset = BaseInformationModel.objects.filter(is_active=True).all()
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ('header', 'parent', 'is_active',)
    search_fields = ('pk', 'value', 'code',)
    ordering_fields = ('pk', 'value', 'header', 'parent', 'code',)
    lookup_field = 'id'


class CreateBaseInformation(BaseInformation, CreateAPIView):
    serializer_class = BaseInformationCreateModelSerializer


class ListBaseInformation(BaseInformation, ListAPIView):
    serializer_class = BaseInformationListModelSerializer


class RetrieveBaseInformation(BaseInformation, RetrieveAPIView):
    serializer_class = BaseInformationRetrieveModelSerializer


class UpdateBaseInformation(BaseInformation, UpdateAPIView):
    serializer_class = BaseInformationUpdateModelSerializer


class DestroyBaseInformation(BaseInformation, DestroyAPIView):
    serializer_class = BaseInformationDestroyModelSerializer
