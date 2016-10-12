

from django.db import models


class Text(models.Model):

    title = models.CharField(
        max_length=200,
    )

    markup = models.TextField()

    def __str__(self):
        return self.title
