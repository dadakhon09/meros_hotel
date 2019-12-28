from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from adminka.tours.get_icons import Icons


class CarImage(models.Model):
    image = models.ImageField(upload_to='cars', null=True, blank=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)

    class Meta:
        db_table = 'car_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'


class Car(models.Model):
    title = JSONField()
    description = JSONField(null=True)
    slug = models.SlugField(max_length=255)
    price = models.PositiveIntegerField(null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'cars'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=Car)
def get_slug5(sender, instance,created,  **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
