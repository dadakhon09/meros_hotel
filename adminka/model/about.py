from django.contrib.postgres.fields import JSONField
from django.db import models


class About(models.Model):
    text = JSONField()
    image = models.ImageField(upload_to='about', null=True, blank=True)

    class Meta:
        db_table = 'about'
        ordering = ['-id']

    def __str__(self):
        return self.text['text_en'][:100] or 'asd'


