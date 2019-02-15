from django.db import models


class Teacher(models.Model):

    name = models.CharField(32)
    email = models.EmailField()
    image = models.FilePathField()
