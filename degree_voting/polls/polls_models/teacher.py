from django.db import models


class Teacher(models.Model):

    name = models.CharField(max_length=32)
    email = models.EmailField()
    # image = models.FilePathField(null=True, blank=True)
    
    def __str__(self):
        return str(self.name)
    
    def __repr__(self):
        return '{id: {0}, name: {1}, email: {2}, image: {3}}'.\
            format(str(self.pk), str(self.name), str(self.email), str(self.image))

