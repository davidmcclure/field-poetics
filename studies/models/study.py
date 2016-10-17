

from django.db import models

from bs4 import BeautifulSoup


class Study(models.Model):

    name = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        unique=True,
    )

    text = models.TextField()

    class Meta:
        verbose_name_plural = 'studies'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        """
        On create, write taggable entity ids into the markup.
        """

        if not self.pk:

            tree = BeautifulSoup(self.text)

            # Add sequential ids.
            for i, tag in enumerate(tree.select('.taggable')):
                tag.attrs['data-id'] = i+1

            self.text = str(tree)

        super().save(*args, **kwargs)
