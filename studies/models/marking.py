

from django.db import models


class Marking(models.Model):

    trial = models.ForeignKey('Trial')

    element_id = models.IntegerField()
