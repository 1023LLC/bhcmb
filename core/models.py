from django.db import models





class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    image_url = models.URLField()
    directions_url = models.URLField()
    date_time = models.DateTimeField()
    description = models.TextField()
    booking_url = models.URLField()

    def __str__(self):
        return self.title