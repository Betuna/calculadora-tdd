#test/test_operaciones.py
import pytest 
from calculadora.operaciones import suma
from calculadora.operaciones import resta

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(2.5, 3.5) == 6.0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(3,5) == -2
    assert resta(2.5, 1.5) == 1.0