

from django.db import models

from bs4 import BeautifulSoup


class Text(models.Model):

    title = models.CharField(
        max_length=200,
    )

    markup = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        """
        On create, write taggable entity ids into the markup.
        """

        if not self.pk:

            tree = BeautifulSoup(self.markup)

            # Add sequential ids.
            for i, tag in enumerate(tree.select('.taggable')):
                tag.attrs['data-id'] = i+1

            self.markup = str(tree)

        super().save(*args, **kwargs)
