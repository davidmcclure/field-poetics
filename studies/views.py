

from django.shortcuts import render

from .models import Study


def text(request, slug):

    """
    Mark the text.
    """

    study = Study.objects.get(slug=slug)

    return render(request, 'studies/text.html', dict(study=study))
