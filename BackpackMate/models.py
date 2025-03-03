from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from datetime import datetime
from django.utils.timezone import now
# Create your models here.


class User(AbstractUser):
    pass

class District(models.Model):
    name = models.CharField(max_length=75)
    # saved = models.ManyToManyField(User, null=True, blank=True, related_name = "saved_districts")

    def __str__(self):
        return f"{self.name}"


class Temple(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    architecture = models.CharField(max_length = 1200)
    major_high = models.CharField(max_length = 1200)
    venue_img = models.ImageField(upload_to = "images/")
    zip_code = models.CharField(max_length=10)
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name = "district")
    # bookmark = models.ManyToManyField(User, null = True, blank = True, related_name = "saved_temples")
    mapUrl = models.CharField(max_length=1200, blank = True)

    def __str__(self):
        return f"{self.name} from {self.district}"

class Heritage_centers(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name = "heritage_district")
    venue_img = models.ImageField(upload_to = "images/")
    mapUrl = models.CharField(max_length=1200, blank = True)

    def __str__(self):
        return f"{self.name} at {self.district}"


class Tourism_place(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name = "tourist_place_district")
    venue_img = models.ImageField(upload_to = "images/")
    mapUrl = models.CharField(max_length=1200, blank = True)

    def __str__(self):
        return f"{self.name} at {self.district}"


class Tourist_spots(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    place = models.ForeignKey(Tourism_place, on_delete=models.CASCADE, related_name="tourist_spots_places")
    venue_img = models.ImageField(upload_to = "images/")

    def __str__(self):
        return f"{self.name} at {self.place}"

class Beach(models.Model):
    name=models.CharField(max_length=250)
    description = models.TextField()
    venue_img = models.ImageField(upload_to = "images/")
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name = "beach_district")
    mapUrl = models.CharField(max_length=1200, blank = True)

    def __str__(self):
        return f"{self.name} from {self.district}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    rating = models.IntegerField(default=1, choices=[(i, str(i)) for i in range(1, 6)])
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f"Comment by {self.user} on {self.content_object}"