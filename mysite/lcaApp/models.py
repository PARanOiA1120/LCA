from django.db import models

# Create your models here.
import datetime
from django.utils import timezone


class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name


class Classification(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    classification = models.CharField(max_length=1000)
    def __str__(self):
        return self.classification


# class Activity(models.Model):
#     classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
#     activity = models.CharField(max_length=1000)
#     def __str__(self):
#         return self.activity




