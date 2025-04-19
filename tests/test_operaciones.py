#test/test_operaciones.py
import pytest 
from calculadora.operaciones import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0
    assert suma(2.5, 3.5) == 6.0

