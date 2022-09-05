from django.db import models
from django.utils.translation import gettext_lazy as _


class Header(models.Model):
    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
        blank=False,
        null=False,
    )
    code = models.CharField(
        verbose_name=_('code'),
        max_length=255,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )

    class Meta:
        ordering = ('pk', 'title', 'code', 'is_active',)
        verbose_name = _('Base Information Header'),
        verbose_name_plural = _('Base Information Headers')

    def __str__(self):
        return f'{self.title}'


class BaseInformation(models.Model):
    header = models.ForeignKey(
        verbose_name=_('header'),
        to=Header,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )
    parent = models.ForeignKey(
        verbose_name=_('parent'),
        to='BaseInformation',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    value = models.CharField(
        verbose_name=_('value'),
        max_length=255,
        blank=False,
        null=False,
    )
    code = models.CharField(
        verbose_name=_('code'),
        max_length=255,
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('active'),
        default=True,
    )

    class Meta:
        ordering = ('pk', 'header', 'value', 'code', 'is_active',)
        verbose_name = _('Base Information')
        verbose_name_plural = _('Base Information')

    def __str__(self):
        return f'{self.value}'
