from django.db import models


class Subject(models.Model):

    title = models.IntegerField(64)
    description = models.TextField()
    credits = models.IntegerField()
