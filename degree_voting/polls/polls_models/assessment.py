from django.db import models
from . import subject


class Assessment(models.Model):

    mark = models.FloatField()
    difficulty = models.FloatField()
    amount = models.IntegerField()
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)

    def __str__(self):
        return 'Subject: {0}\t - Mark: {1}\t - Difficulty: {2}'.\
            format(str(self.subject_id), str(self.mark), str(self.difficulty))

    def __repr__(self):
        return '{Subject: {0}, Mark: {1}, Difficulty: {2} , Amount: {3}}'. \
            format(str(self.subject_id), str(self.mark), str(self.difficulty), str(self.amount))
