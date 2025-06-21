# test_tablero.py
import pytest

def test_impacto():
    tablero = Tablero()
    tablero.colocar_barco(3, 5)
    resultado = tablero.recibir_ataque(3, 5)
    assert resultado == "¡Impacto!"
    assert tablero.celdas[3][5] == 'X'

def test_agua():
    tablero = Tablero()
    resultado = tablero.recibir_ataque(2, 2)
    assert resultado == "Agua."
    assert tablero.celdas[2][2] == 'O'

def test_ataque_repetido():
    tablero = Tablero()
    tablero.recibir_ataque(2, 2)  # Agua
    resultado = tablero.recibir_ataque(2, 2)
    assert resultado == "Ya atacaste esta casilla."