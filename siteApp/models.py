# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unicodedata
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    parent = models.ForeignKey("self",  verbose_name="Родительская категория", on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Advertisement(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)
    title = models.CharField(max_length=200, verbose_name="Заголовок объявления", null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=False)
    price = models.PositiveIntegerField(null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = (
        (1, "Продам"),
        (2, "Куплю"),
        (3, "Сдам"),
        (4, "Сниму")
    )

    def __str__(self):
        return self.title


class Photo(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    image = models.ImageField()
    ad = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
