from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from adminka.tours.get_icons import Icons

obj = Icons()
my_tuple = obj.get_icons()


class TourFacility(models.Model):
    title = JSONField()
    tours = models.ManyToManyField('Tour', related_name='t_facilities', blank=True)
    icon = models.IntegerField(choices=my_tuple, null=True, blank=True)

    class Meta:
        db_table = 'facilities'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


class TourExpense(models.Model):
    title = JSONField()
    tours = models.ManyToManyField('Tour', related_name='t_expenses', blank=True)
    icon = models.IntegerField(choices=my_tuple, null=True, blank=True)

    class Meta:
        db_table = 'expenses'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


class TourImage(models.Model):
    image = models.ImageField(upload_to='tours', null=True, blank=True)
    tour = models.ForeignKey('Tour', on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'tour_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'


class Tour(models.Model):
    title = JSONField()
    description = JSONField(null=True)
    slug = models.SlugField(max_length=255)
    route = JSONField(null=True)  # ASK
    duration = models.PositiveIntegerField(null=True, blank=True)
    num_people = models.PositiveIntegerField(blank=True, null=True)
    guide = models.BooleanField(null=True, blank=True)
    price = models.PositiveIntegerField(null=True, blank=True)
    plan = JSONField(null=True)

    class Meta:
        db_table = 'tours'
        ordering = ['-id']

    def __str__(self):
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=Tour)
def get_slug(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
