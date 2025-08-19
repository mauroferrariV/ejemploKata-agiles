import pytest
from kata import suma   # Importamos la función desde kata.py

def test_suma_cadena_vacia():
    assert suma("") == 0

def test_suma_un_numero():
    assert suma("5") == 5

def test_suma_dos_numeros():
    assert suma("2,3") == 5