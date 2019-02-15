from django.db import models
from . import degree, subject


class Course(models.Model):

    degree_id = models.ForeignKey(degree.Degree, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
    course = models.SmallIntegerField()
