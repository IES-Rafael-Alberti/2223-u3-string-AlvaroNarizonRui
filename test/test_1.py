from src.ejercicio1 import reverso
import pytest

def test_palabra_reversa():
    assert reverso("pepe") == "e\np\ne\np\n"
    assert reverso("jorge") == "e\ng\nr\no\nj\n"

if __name__ == "__main__":
    pytest.main()