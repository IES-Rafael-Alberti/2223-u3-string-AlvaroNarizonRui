import pytest
from src.ejercicio3 import cuenta

def test_cuenta_p():
    cadena = "pepe"
    letra = "p"
    assert cuenta(cadena,letra) == 2
def test_cuenta_e():
    cadena = "pepe"
    letra = "e"
    assert cuenta(cadena,letra) == 2

if __name__ == "__main__":
    pytest.main()