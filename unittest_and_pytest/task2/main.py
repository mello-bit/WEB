import pytest
from yandex_testing_lesson import reverse


def test_es():
    assert reverse('') == ''


def test_oneCharS():
    assert reverse('t') == 't'


def test_goodS():
    assert reverse('goog') == 'goog'


def test_noGoodS():
    assert reverse('ell') == 'lle'


def test_noS():
    with pytest.raises(TypeError):
        reverse(905)


def test_otherNoS():
    with pytest.raises(TypeError):
        reverse([11, 32, 60])
