import pytest

def test_count_a():
    palabra = "banana"
    letra = "a"
    assert palabra.count(letra) == 3
def test_count_b():
    palabra = "banana"
    letra = "b"
    assert palabra.count(letra) == 1
def test_count_n():
    palabra = "banana"
    letra = "n"
    assert palabra.count(letra) == 2
def test_count_otra_letra():
    palabra = "banana"
    letra = "h"
    assert palabra.count(letra) == 0

if __name__ == "__main__":
    pytest.main()
