

import pytest

from studies.tests.factories import StudyFactory


pytestmark = pytest.mark.django_db


def test_conditions():

    """
    When the text includes condition elements, provide one of the keys.
    """

    text = '''
    <h1 data-condition="cond1">Condition 1</h1>
    <h1 data-condition="cond2">Condition 2</h1>
    <h1 data-condition="cond3">Condition 3</h1>
    '''

    study = StudyFactory(text=text)

    assert study.random_condition() in set([
        'cond1',
        'cond2',
        'cond3',
    ])


def test_no_conditions():

    """
    When the text doesn't define conditions, return None.
    """

    text = '<h1>Text</h1>'

    study = StudyFactory(text=text)

    assert study.random_condition() == None
