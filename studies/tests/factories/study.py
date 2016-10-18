

import factory

from studies.models import Study


class StudyFactory(factory.DjangoModelFactory):

    class Meta:
        model = Study

    name = 'Study'

    slug = factory.Sequence(
        lambda n: 'study-{0}'.format(n)
    )

    text = '<span>text</span>'
