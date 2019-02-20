from django.db import models


class HomeDescription(models.Model):
    text = models.TextField(help_text="Contains the description of the web")
    display = models.BooleanField(default=False,
                                  help_text="Only the first marked will be displayed")
