from django.db import models


class Subject(models.Model):

    code = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=64)
    ects = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return '{} {}'.format(str(self.code), str(self.title))
    
    def __repr__(self):
        return '{id: {0}, title: {1}, ects: {2}, description: {3}}'\
        .format(str(self.code), str(self.title), str(self.ects),\ str(self.description))
