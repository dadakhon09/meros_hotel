from django.contrib.postgres.fields import JSONField
from django.db import models


class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', null=True, blank=True)

    class Meta:
        db_table = 'gallery'

    def __str__(self):
        return self.image.name
