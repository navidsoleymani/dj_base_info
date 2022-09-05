from django.urls import path

from .views import (
    CreateHeader as BaseInformationHeaderCreateAPIView,
    RetrieveHeader as BaseInformationHeaderRetrieveAPIView,
    ListHeader as BaseInformationHeaderListAPIView,
    UpdateHeader as BaseInformationHeaderUpdateAPIView,
    DestroyHeader as BaseInformationHeaderDestroyAPIView,

    CreateBaseInformation as BaseInformationCreateAPIView,
    RetrieveBaseInformation as BaseInformationRetrieveAPIView,
    ListBaseInformation as BaseInformationListAPIView,
    UpdateBaseInformation as BaseInformationUpdateAPIView,
    DestroyBaseInformation as BaseInformationDestroyAPIView,
)

app_name = 'base_information'
urlpatterns = [
    path('headers/create', BaseInformationHeaderCreateAPIView.as_view(), name='create_header'),
    path('headers/retrieve/<int:id>', BaseInformationHeaderRetrieveAPIView.as_view(), name='retrieve_header'),
    path('headers/list', BaseInformationHeaderListAPIView.as_view(), name='list_header'),
    path('headers/update/<int:id>', BaseInformationHeaderUpdateAPIView.as_view(), name='update_header'),
    path('headers/destroy/<int:id>', BaseInformationHeaderDestroyAPIView.as_view(), name='destroy_header'),

    path('create', BaseInformationCreateAPIView.as_view(), name='create'),
    path('retrieve/<int:id>', BaseInformationRetrieveAPIView.as_view(), name='retrieve'),
    path('list', BaseInformationListAPIView.as_view(), name='list'),
    path('update/<int:id>', BaseInformationUpdateAPIView.as_view(), name='update'),
    path('destroy/<int:id>', BaseInformationDestroyAPIView.as_view(), name='destroy'),
]
