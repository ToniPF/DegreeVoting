from django.db import models


class Degree(models.Model):
    title = models.CharField(max_length=64)
    ects = models.IntegerField()
    description = models.TextField()
    university = models.CharField(max_length=64)

    def __str__(self):
        return self.title

