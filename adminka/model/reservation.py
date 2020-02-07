from django.db import models
from django.utils import timezone


class Reservation(models.Model):
    reservation_time = models.DateTimeField(default=timezone.now)
    customer = models.CharField(max_length=255)
    no_of_children = models.PositiveSmallIntegerField(default=0)
    no_of_adults = models.PositiveSmallIntegerField(default=1)
    expected_arrival_date_time = models.DateTimeField(default=timezone.now)
    expected_departure_date_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'reservations'

    def __str__(self):
        return f'{self.id}-reservation + {self.customer}'
