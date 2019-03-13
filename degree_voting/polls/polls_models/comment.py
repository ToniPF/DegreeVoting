from django.db import models


class Comment(models.Model):

    comment = models.CharField(max_length=250)
    
    def __str__(self):
        return self.comment[:25]
