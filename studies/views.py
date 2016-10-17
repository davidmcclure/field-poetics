

from django.shortcuts import render

from .models import Study


def text(request, slug):

    """
    Mark the text.
    """

    study = Study.objects.get(slug=slug)

    cond, text = study.randomized_text()

    return render(request, 'studies/text.html', dict(text=text))
