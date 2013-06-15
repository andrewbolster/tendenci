from django.db import models

from tendenci.apps.dashboard.managers import DashboardStatManager
from tendenci.libs.abstracts.models import OrderingBaseModel


class DashboardStatType(OrderingBaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    displayed = models.BooleanField(default=True)


class DashboardStat(models.Model):
    key = models.ForeignKey(DashboardStatType)
    value = models.TextField()
    create_dt = models.DateTimeField(auto_now_add=True)

    objects = DashboardStatManager()

    class Meta:
        ordering = ('-create_dt',)
