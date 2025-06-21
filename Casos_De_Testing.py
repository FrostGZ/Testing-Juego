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

def test_colocar_barco_en_borde_inferior_derecho():
    tablero = Tablero()
    tablero.colocar_barco(9, 9)
    assert tablero.celdas[9][9] == 'B'

def test_colocar_multiples_barcos_en_fila():
    tablero = Tablero()
    for i in range(5):
        tablero.colocar_barco(0, i)
    for i in range(5):
        assert tablero.celdas[0][i] == 'B'

def test_no_colocar_barco_fuera_limites_negativo():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.colocar_barco(-1, 0)

def test_no_colocar_barco_fuera_limites_excedido():
    tablero = Tablero()
    with pytest.raises(IndexError):
        tablero.colocar_barco(10, 0)  # índice fuera de 0–9

def test_ataque_exitoso_y_fallido_mismo_juego():
    tablero = Tablero()
    tablero.colocar_barco(4, 4)
    resultado1 = tablero.recibir_ataque(4, 4)
    resultado2 = tablero.recibir_ataque(2, 2)
    assert resultado1 == "¡Impacto!"
    assert resultado2 == "Agua."

def test_colocar_y_destruir_barco_grande_horizontal():
    tablero = Tablero()
    for i in range(3, 6):  # barco de tamaño 3
        tablero.colocar_barco(5, i)
        assert tablero.celdas[5][i] == 'B'
        tablero.recibir_ataque(5, i)
        assert tablero.celdas[5][i] == 'X'

def test_poder_radar_simulado_detecta_barco():
    tablero = Tablero()
    tablero.colocar_barco(6, 6)
    # Simulación: radar solo “lee” la celda
    estado = tablero.celdas[6][6]
    assert estado == 'B'

def test_poder_radar_simulado_no_detecta_barco():
    tablero = Tablero()
    estado = tablero.celdas[2][3]
    assert estado == ' '

def test_colocar_barco_superpuesto():
    tablero = Tablero()
    tablero.colocar_barco(1, 1)
    tablero.colocar_barco(1, 1)  # Se permite; validación opcional
    assert tablero.celdas[1][1] == 'B'

def test_ataque_a_todas_las_celdas_vacias():
    tablero = Tablero()
    total_agua = 0
    for fila in range(10):
        for col in range(10):
            if tablero.celdas[fila][col] == ' ':
                resultado = tablero.recibir_ataque(fila, col)
                if resultado == "Agua.":
                    total_agua += 1
    assert total_agua == 100  # tablero vacío

def test_ataque_diagonal():
    tablero = Tablero()
    tablero.colocar_barco(3, 3)
    resultado = tablero.recibir_ataque(3, 3)
    assert resultado == "¡Impacto!"

def test_todo_tablero_vacio():
    tablero = Tablero()
    for fila in range(10):
        for col in range(10):
            assert tablero.celdas[fila][col] == ' '