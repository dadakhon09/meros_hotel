from django.db import models


class Gallery(models.Model):
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'gallery'

    def __str__(self):
        return self.image.name
