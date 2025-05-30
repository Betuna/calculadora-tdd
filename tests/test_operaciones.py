#test/test_operaciones.py
import pytest 
from calculadora.operaciones import suma
from calculadora.operaciones import resta
from calculadora.operaciones import multiplicacion
from calculadora.operaciones import division
from calculadora.operaciones import raiz_cuadrada
from calculadora.operaciones import exponencial

def test_exponencial():
    assert exponencial(0) == pytest.approx(1, 0.001)
    assert exponencial(1) == pytest.approx(2.71828, 0.001)
    assert exponencial(2) == pytest.approx(7.389056, 0.001)

def test_raiz_cuadrada():
    assert raiz_cuadrada(9) == pytest.approx(3, 0.001)
    assert raiz_cuadrada(2) == pytest.approx(1.414, 0.001)
    assert raiz_cuadrada(0) == 0

def test_raiz_negativa():
    with pytest.raises(ValueError):
        raiz_cuadrada(-4) 

def test_division():
    assert division(10, 2) == 5.0
    assert division(7, 3) == pytest.approx(2.333333, 0.001)
    assert division(5,2) == 2.5

def test_division_por_cero():
    with pytest.raises(ValueError):
        division(5, 0)

def test_multiplicacion():
    assert multiplicacion(3, 4) == 12
    assert multiplicacion(-2, 3) == -6
    assert multiplicacion(2.5, 4) == 10.0

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(2.5, 3.5) == 6.0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(3,5) == -2
    assert resta(2.5, 1.5) == 1.0

