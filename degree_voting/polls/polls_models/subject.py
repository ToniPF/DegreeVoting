from django.db import models


class Subject(models.Model):
    #TODO code CAN'T BE < 0, now it can
    code = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    ects = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return '{} {}'.format(str(self.code), str(self.title))

