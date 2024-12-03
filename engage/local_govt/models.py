from django.db import models
from django.utils.translation import gettext_lazy as _

from engage.common.models import TimestampModel
from engage.locations.models import Division, District, Upazila, Union


class Localgovt(TimestampModel):
    class TypeOfLocalGovt(models.TextChoices):
        union_parishad = "union parishad"
        upazila_parishad = "upazila parishad"
        zila_parishad = "zila parishad"
        city_corporation = "city corporation"

    type = models.CharField(
        max_length=20, choices=TypeOfLocalGovt.choices,verbose_name=_('Type of Local Govt')
        )

    division = models.ForeignKey(Division, on_delete=models.PROTECT, verbose_name=_('division'), related_name='+')
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name=_('district'), related_name='+')
    upazila = models.ForeignKey(Upazila, on_delete=models.PROTECT, verbose_name=_('upazila'), related_name='+', null=True, blank=True)
    union = models.ForeignKey(Union, on_delete=models.PROTECT, verbose_name=_('union'), related_name='+', null=True, blank=True)
    location = models.CharField(verbose_name=_('location'), max_length=200, null=True, blank=True)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)


    class Meta:
        verbose_name = _('localgovt')
        verbose_name_plural = _('localgovts')

    def __str__(self):
        return self.type
