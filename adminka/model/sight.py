from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from adminka.tours.get_icons import Icons


class SightCategory(models.Model):
    title = JSONField(null=True)

    class Meta:
        db_table = 'sight_categories'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


class SightImage(models.Model):
    image = models.ImageField(upload_to='sights', null=True, blank=True)
    sight = models.ForeignKey('Sight', on_delete=models.CASCADE, related_name='s_images')

    class Meta:
        db_table = 'sight_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'


class Sight(models.Model):
    title = JSONField()
    description = JSONField(null=True)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(SightCategory, on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'sights'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=Sight)
def get_slug2(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
