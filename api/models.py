from __future__ import unicode_literals

from django.db import models


class Media(models.Model):
    file = models.FileField(upload_to="media/", default=None)
