from django.db import models
from django.utils import timezone


class Post(models.Model):
    creatUser = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    yaratilis_tarihi = models.DateTimeField(
            default=timezone.now)
    yayinlama_tarihi = models.DateTimeField(
            blank=True, null=True)

    def yayinla(self):
        self. yayinlama_tarihi = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.TextField()
    description = models.CharField(max_length=200)



# Create your models here.
