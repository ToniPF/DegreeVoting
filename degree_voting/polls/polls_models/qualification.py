from django.db import models
from . import subject, teacher


class Qualification(models.Model):

    mark = models.FloatField()
    # TODO amount has to be auto computed
    amount = models.IntegerField()
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
    teacher_id = models.ForeignKey(teacher.Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return 'Subject: {0}\t - Teacher: {1}\t - Mark: {2}'.\
            format(str(self.subject_id), str(self.teacher_id), str(self.mark))
