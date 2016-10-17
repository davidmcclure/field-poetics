

from django.shortcuts import render

from .models import Study


def text(request, slug):

    """
    Mark the text.
    """

    return render(request, 'studies/text.html')
