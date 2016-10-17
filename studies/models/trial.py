

from django.db import models


class Trial(models.Model):

    study = models.ForeignKey('Study')
