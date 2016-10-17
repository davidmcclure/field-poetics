

import pytest

from bs4 import BeautifulSoup

from studies.models import Study


pytestmark = pytest.mark.django_db


def test_write_ids():

    """
    When a text is saved, ids should be written onto the taggable elements.
    """

    text = '''
    <span class="taggable">w1</span>
    <span class="taggable">w2</span>
    <span class="taggable">w3</span>
    '''

    # TODO: FactoryBoy
    study = Study.objects.create(name='Study', text=text)

    study.refresh_from_db()

    tree = BeautifulSoup(study.text)

    assert tree.find(text='w1').parent.attrs['data-id'] == '1'
    assert tree.find(text='w2').parent.attrs['data-id'] == '2'
    assert tree.find(text='w3').parent.attrs['data-id'] == '3'
