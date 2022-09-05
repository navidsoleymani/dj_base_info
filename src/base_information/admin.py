from django.contrib.admin import ModelAdmin, register

from .models import (
    Header as BaseInformationHeaderModel,
    BaseInformation as BaseInformationModel,
)


@register(BaseInformationHeaderModel)
class BaseInformationHeader(ModelAdmin):
    list_display = ('pk', 'code', 'title', 'is_active',)
    list_display_links = ('pk', 'code', 'title', 'is_active',)
    fieldsets = [
        (None, {'fields': [('code', 'title',), 'is_active', ], },),
    ]


@register(BaseInformationModel)
class BaseInformation(ModelAdmin):
    list_display = ('pk', 'code', 'value', 'header', 'parent', 'is_active',)
    list_display_links = ('pk', 'code', 'value', 'header', 'parent', 'is_active',)
    search_fields = ('pk', 'code', 'value',)
    list_filter = ('parent', 'header',)
    fieldsets = [
        (None, {'fields': ['header', 'parent', ('code', 'value',), 'is_active', ], },),
    ]
