from django.db import models
from . import degree, subject


class Course(models.Model):

    # Weird python things, enums are too difficult.
    ###############################################
    PRIMER = 1
    SEGON = 2
    TERCER = 3
    QUART = 4
    CINQUE = 5
    COURSE_LIST = (
        (PRIMER, 'Primer'),
        (SEGON, 'Segon'),
        (TERCER, 'Tercer'),
        (QUART, 'Quart'),
        (CINQUE, 'Cinquè'),
    )
    ###############################################
    #

    degree_id = models.ForeignKey(degree.Degree, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(subject.Subject, on_delete=models.CASCADE)
    course = models.SmallIntegerField(choices=COURSE_LIST)
    
    def __str__(self):
        return '{} {}'.format(str(self.degree_id), str(self.subject_id))
    
    def __repr__(self):
        return '{id: {0}, degree_id: {1}, subject_id: {2}, course: {3}}'.\
            format(str(self.pk), str(self.degree_id), str(self.subject_id),
                   str(self.course))
