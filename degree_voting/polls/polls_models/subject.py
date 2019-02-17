from django.db import models


class Subject(models.Model):

    title = models.CharField(max_length=64)
    ects = models.IntegerField()
    description = models.TextField()
