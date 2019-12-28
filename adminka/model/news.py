from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from adminka.tours.get_icons import Icons


class News(models.Model):
    title = JSONField()
    description = JSONField(null=True)
    slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='news', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'news'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=News)
def get_slug4(sender, instance,created,  **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
