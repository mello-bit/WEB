import pytest
from yandex_testing_lesson import Rectangle


def test_ri():
    with pytest.raises(TypeError):
        Rectangle("d", 5)
    with pytest.raises(TypeError):
        Rectangle(3, "a")
    with pytest.raises(ValueError):
        Rectangle(-12, 5)
    with pytest.raises(ValueError):
        Rectangle(3, -54)


def test_rga():
    r = Rectangle(7, 4)
    assert r.get_area() == 28


def test_rgp():
    r = Rectangle(5, 9)
    assert r.get_perimeter() == 28
