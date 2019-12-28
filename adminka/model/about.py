from django.contrib.postgres.fields import JSONField
from django.db import models


class About(models.Model):
    text = JSONField()

    class Meta:
        db_table = 'about'
        ordering = ['-id']

    def __str__(self):
        return self.text['text_en'][:100] or 'asd'


class AboutImage(models.Model):
    image = models.ImageField(upload_to='about', null=True, blank=True)
    about = models.ForeignKey(About, on_delete=models.CASCADE)

    class Meta:
        db_table = 'about-images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'
