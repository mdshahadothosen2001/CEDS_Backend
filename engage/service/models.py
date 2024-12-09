from django.db import models
from django.utils.translation import gettext_lazy as _


class Service(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('service')
        verbose_name_plural = _('services')

    def __str__(self):
        return self.title
