

import pytest

from studies.tests.factories import StudyFactory


pytestmark = pytest.mark.django_db


def test_conditions():

    """
    Provide a list of condition keys.
    """

    text = '''
    <h1 data-condition="cond1">Condition 1</h1>
    <h1 data-condition="cond2">Condition 2</h1>
    <h1 data-condition="cond3">Condition 3</h1>
    '''

    study = StudyFactory(text=text)

    assert study.conditions() == [
        'cond1',
        'cond2',
        'cond3',
    ]
