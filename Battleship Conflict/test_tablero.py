import pytest
from tablero import Tablero

def test_colocar_barco_sobre_barco():
    tablero = Tablero()
    tablero.colocar_barco(0, 0, 3, 'H')  # Coloca un barco horizontal
    with pytest.raises(ValueError):
        tablero.colocar_barco(0, 0, 3, 'H')  # Intentamos colocar otro barco en la misma posicion

def test_colocar_barco_en_borde_superior_izquierdo():
    tablero = Tablero()
    tablero.colocar_barco(0, 0, 2, 'H')  # Coloca un barco en la esquina superior izquierda
    assert tablero.celdas[0][0] == 'B'
    assert tablero.celdas[0][1] == 'B'

def test_colocar_barco_en_borde_inferior_derecho():
    tablero = Tablero()
    tablero.colocar_barco(9, 8, 2, 'H')  # Coloca un barco en la esquina inferior derecha
    assert tablero.celdas[9][8] == 'B'
    assert tablero.celdas[9][9] == 'B'

def test_colocar_multiples_barcos_en_fila():
    tablero = Tablero()
    for i in range(5):
        tablero.colocar_barco(0, i, 1, 'H')  # Coloca 5 barcos de tamano 1 en la primera fila
    for i in range(5):
        assert tablero.celdas[0][i] == 'B'

def test_colocar_barco_grande_horizontal():
    tablero = Tablero()
    for i in range(3, 6):  # Coloca un barco de tamano 3 en la fila 5
        tablero.colocar_barco(5, i, 1, 'H')
    for i in range(3, 6):
        assert tablero.celdas[5][i] == 'B'

def test_colocar_barco_superpuesto():
    tablero = Tablero()
    tablero.colocar_barco(1, 1, 3, 'H')  # Coloca un barco de tamano 3
    with pytest.raises(ValueError):
        tablero.colocar_barco(1, 1, 3, 'H')  # Intentamos colocar otro barco en la misma posicion

def test_colocar_barco_fuera_de_rango():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.colocar_barco(15, 0, 3, 'H')  # Intentamos colocar un barco fuera de los limites

def test_no_colocar_barco_fuera_limites_negativo():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.colocar_barco(-1, 0, 3, 'H')  # Intentamos colocar un barco fuera de los limites negativos

def test_no_colocar_barco_fuera_limites_excedido():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.colocar_barco(10, 0, 3, 'H')  # Intentamos colocar un barco fuera del limite superior

def test_todo_tablero_vacio():
    tablero = Tablero()
    for fila in range(10):
        for col in range(10):
            assert tablero.celdas[fila][col] == ' '  # Verifica que el tablero este vacio al principio
