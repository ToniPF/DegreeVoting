from django.db import models
from . import subject


class Assessment(models.Model):

    mark = models.SmallIntegerField()
    difficulty = models.SmallIntegerField()
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
