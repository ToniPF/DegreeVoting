from django.db import models


class Comment(models.Model):

    comment = models.CharField(250)
