import pytest
from yandex_testing_lesson import count_chars


def test_es():
    assert count_chars('') == {}


def test_oneCharS():
    assert count_chars('t') == {'t': 1}


def test_severalCharsS():
    assert count_chars('ell') == {'e': 1, 'l': 2}


def test_noS():
    with pytest.raises(TypeError):
        count_chars(905)


def test_otherNoS():
    with pytest.raises(TypeError):
        count_chars([11, 32, 60])
