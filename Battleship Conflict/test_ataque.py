import pytest
from tablero import Tablero

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
    tablero.recibir_ataque(2, 2)
    resultado = tablero.recibir_ataque(2, 2)
    assert resultado == "Ya atacaste esta casilla."

def test_ataque_fuera_de_rango():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.recibir_ataque(20, 20)

def test_todos_los_barcos_hundidos():
    tablero = Tablero()
    tablero.colocar_barco(0, 0)
    tablero.colocar_barco(0, 1)
    tablero.recibir_ataque(0, 0)
    tablero.recibir_ataque(0, 1)
    assert tablero.todos_barcos_hundidos()

def test_ataque_exitoso_y_fallido_mismo_juego():
    tablero = Tablero()
    tablero.colocar_barco(4, 4)
    resultado1 = tablero.recibir_ataque(4, 4)
    resultado2 = tablero.recibir_ataque(2, 2)
    assert resultado1 == "¡Impacto!"
    assert resultado2 == "Agua."

def test_estado_despues_de_ataques():
    tablero = Tablero()
    tablero.colocar_barco(7, 7)
    tablero.recibir_ataque(7, 7)
    tablero.recibir_ataque(1, 1)
    assert tablero.celdas[7][7] == 'X'
    assert tablero.celdas[1][1] == 'O'

def test_ataque_diagonal():
    tablero = Tablero()
    tablero.colocar_barco(3, 3)
    resultado = tablero.recibir_ataque(3, 3)
    assert resultado == "¡Impacto!"

def test_ataque_a_todas_las_celdas_vacias():
    tablero = Tablero()
    total_agua = 0
    for fila in range(10):
        for col in range(10):
            if tablero.celdas[fila][col] == ' ':
                resultado = tablero.recibir_ataque(fila, col)
                if resultado == "Agua.":
                    total_agua += 1
    assert total_agua == 100

def test_ataque_en_celda_ya_atacada_con_barco():
    tablero = Tablero()
    tablero.colocar_barco(4, 4)
    tablero.recibir_ataque(4, 4)
    resultado = tablero.recibir_ataque(4, 4)
    assert resultado == "Ya atacaste esta casilla."

def test_ataque_en_celda_ya_atacada_con_agua():
    tablero = Tablero()
    tablero.recibir_ataque(2, 2)
    resultado = tablero.recibir_ataque(2, 2)
    assert resultado == "Ya atacaste esta casilla."
