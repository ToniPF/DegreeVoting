from django.db import models
from . import subject, teacher


class Qualification(models.Model):

    mark = models.SmallIntegerField()
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(teacher.Teacher, on_delete=models.CASCADE)
