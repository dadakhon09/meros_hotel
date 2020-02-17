from django.contrib.postgres.fields import JSONField
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone
from django.dispatch import receiver
from django.utils.text import slugify


class RoomImage(models.Model):
    image = models.ImageField(null=True, blank=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='images')

    class Meta:
        db_table = 'room_images'
        ordering = ['-id']

    def __str__(self):
        return self.image.name or 'asd'


class Reservation(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    reservation_time = models.DateTimeField(default=timezone.now)
    customer_name = models.CharField(max_length=255)
    customer_email = models.CharField(max_length=255)
    no_of_children = models.PositiveSmallIntegerField(default=0)
    no_of_adults = models.PositiveSmallIntegerField(default=1)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)

    # def save(self, *args, **kwargs):
    #     if self.room.availability(self.start_date, self.end_date):
    #        super().save(*args, **kwargs)
    #     else:
    #         return -1

    class Meta:
        db_table = 'reservations'

    def __str__(self):
        return f'{self.id}-reservation + {self.customer_name}'


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

    @property
    def availability(self, start_date, end_date= timezone.now()):
        resves = Reservation.objects.filter(room=self.id)
        for res in resves:
            if res.start_date <= start_date < res.end_date or res.start_date < end_date <= res.end_date:
                return False
        return True

    class Meta:
        db_table = 'rooms'
        ordering = ['-id']
    #
    # def save(self, *args, **kwargs):  # Overriding default behaviour of save
    #     if self.reservation:  # If it is reserved, than it should not be available
    #         self.availability = 0
    #     else:
    #         self.availability = 1
    #
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.title['title_en'] or 'asd'


@receiver(post_save, sender=Room)
def get_slug(sender, instance, created, **kwargs):
    if created:
        slug = slugify(instance.title['title_en'])
        instance.slug = slug
        instance.save()
