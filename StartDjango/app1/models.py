from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from faker import Faker
import random


# Create your models here.
f = Faker()

class Uinfo(models.Model):
    name = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    address = models.TextField()
