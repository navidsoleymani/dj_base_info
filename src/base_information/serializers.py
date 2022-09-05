from rest_framework.serializers import ModelSerializer

from .models import (
    Header as BaseInformationHeaderModel,
    BaseInformation as BaseInformationModel,
)


class Header(ModelSerializer):
    class Meta:
        model = BaseInformationHeaderModel
        fields = '__all__'
        extra_kwargs = {
            'is_active': {
                'default': True,
                'read_only': True,
            },
        }


class CreateHeader(Header):
    pass


class ListHeader(Header):
    pass


class RetrieveHeader(Header):
    pass


class UpdateHeader(Header):
    pass


class DestroyHeader(Header):
    pass


class BaseInformation(ModelSerializer):
    class Meta:
        model = BaseInformationModel
        fields = '__all__'
        extra_kwargs = {
            'is_active': {
                'default': True,
                'read_only': True,
            },
        }


class CreateBaseInformation(BaseInformation):
    pass


class ListBaseInformation(BaseInformation):
    pass


class RetrieveBaseInformation(BaseInformation):
    pass


class UpdateBaseInformation(BaseInformation):
    pass


class DestroyBaseInformation(BaseInformation):
    pass
