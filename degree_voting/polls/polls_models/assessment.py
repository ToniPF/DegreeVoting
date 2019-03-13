from django.db import models
from . import subject


class Assessment(models.Model):

    mark = models.FloatField()
    difficulty = models.FloatField()
    amount = models.IntegerField()
    subject = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)

    def __str__(self):
        return 'Subject: {0}\t - Mark: {1}\t - Difficulty: {2}'.\
            format(str(self.subject), str(self.mark), str(self.difficulty))

