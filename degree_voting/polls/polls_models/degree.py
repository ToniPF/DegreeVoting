from django.db import models


class Degree(models.Model):

    title = models.CharField(max_length=64)
    ects = models.IntegerField()
    description = models.TextField()
    university = models.CharField(max_length=64)
    
    def __str__(self):
        return self.title
    
    def __repr__(self):
        return '{id: {0}, title: {1}, ects: {2}, description: {3},\
         university: {4}}'
        .format(str(self.pk), str(self.title), str(self.ects),\
        str(self.description), str(self.university))
