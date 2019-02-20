from django.db import models


class Comment(models.Model):

    comment = models.CharField(250)
    
    def __str__(self):
        return self.comment[:25]
    
    def __repr__(self):
        return '{id: {0}, comment: {1}}'.format(str(self.pk), str(self.comment))
