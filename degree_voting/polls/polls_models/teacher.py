from django.db import models


class Teacher(models.Model):

    name = models.CharField(max_length=32)
    email = models.EmailField()
    # image = models.FilePathField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)


