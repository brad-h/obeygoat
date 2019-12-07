from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
# pylint: disable=no-member

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)
    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])

class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None)

    class Meta:
        unique_together = ("list", "text")
        ordering = ("id",)