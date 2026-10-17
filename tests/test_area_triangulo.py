
import pytest
from area_triangulo import area_triangulo


def test_area_correcta():
    assert area_triangulo(10, 5) == 25


def test_area_limite():
    assert area_triangulo(0.1, 0.2) == pytest.approx(0.01)


def test_area_error():
    with pytest.raises(ValueError):
        area_triangulo(-5, 10)


def test_datos_invalidos():
    with pytest.raises(TypeError):
        area_triangulo("hola", 5)
