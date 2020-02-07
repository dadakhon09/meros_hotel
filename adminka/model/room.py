from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from adminka.model.reservation import Reservation


class RoomImage(models.Model):
    image = models.ImageField(upload_to='rooms', null=True, blank=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'


ROOM_TYPE = (
    (0, 'Double/Twin room '),
    (1, 'Triple room ')
)


class Room(models.Model):
    title = JSONField()
    description = JSONField(null=True, blank=True)
    slug = models.SlugField(max_length=255)
    price = models.PositiveIntegerField(null=True, blank=True)
    square_meter = models.FloatField(null=True, blank=True)
    room_type = models.IntegerField(choices=ROOM_TYPE, null=True, blank=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.SET_NULL, null=True)
    availability = models.BooleanField(default=True, null=True, blank=True)

    class Meta:
        db_table = 'rooms'
        ordering = ['-id']

    def save(self, *args, **kwargs):  # Overriding default behaviour of save
        if self.reservation:  # If it is reserved, than it should not be available
            self.availability = 0
        else:
            self.availability = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=Room)
def get_slug(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
