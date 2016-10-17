

from django.db import models


class Study(models.Model):

    name = models.CharField(
        max_length=200,
    )

    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'studies'

    def __str__(self):
        return self.name
