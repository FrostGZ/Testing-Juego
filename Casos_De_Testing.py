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

def test_colocar_barco_sobre_barco():
    tablero = Tablero()
    tablero.colocar_barco(1, 1)
    tablero.colocar_barco(1, 1)  # Se permite sin error, pero deberías validar si es deseable
    assert tablero.celdas[1][1] == 'B'

def test_ataque_fuera_de_rango():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.recibir_ataque(20, 20)  # fuera de rango

def test_colocar_barco_fuera_de_rango():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.colocar_barco(15, -1)

def test_todos_los_barcos_hundidos():
    tablero = Tablero()
    tablero.colocar_barco(0, 0)
    tablero.colocar_barco(0, 1)
    tablero.recibir_ataque(0, 0)
    tablero.recibir_ataque(0, 1)
    assert tablero.celdas[0][0] == 'X'
    assert tablero.celdas[0][1] == 'X'

def test_activar_poder_simulado():
    tablero = Tablero()
    tablero.colocar_barco(4, 4)
    # Simulación: poder de radar revela la celda sin atacar
    estado = tablero.celdas[4][4]
    assert estado == 'B'  # El radar ve que hay un barco

def test_colocar_barco_en_borde_superior_izquierdo():
    tablero = Tablero()
    tablero.colocar_barco(0, 0)
    assert tablero.celdas[0][0] == 'B'