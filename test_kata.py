import pytest
from kata import suma   # Importamos la función desde kata.py

def test_suma_cadena_vacia():
    assert suma("") == 0