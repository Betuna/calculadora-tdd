#test/test_operaciones.py
import pytest 
from calculadora.operaciones import suma
from calculadora.operaciones import resta
from calculadora.operaciones import multiplicacion

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

