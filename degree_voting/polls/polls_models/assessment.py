from django.db import models
from . import subject


class Assessment(models.Model):

    mark = models.FloatField()
    difficulty = models.FloatField()
    amount = models.IntegerField()
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
