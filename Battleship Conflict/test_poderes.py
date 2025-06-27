import pytest
from tablero import Tablero
from poderes import Poderes

def test_activar_poder_simulado():
    tablero = Tablero()
    tablero.colocar_barco(4, 4)
    resultados = Poderes.radar(tablero, 4, 4)
    assert resultados[(4, 4)] == 'B'

def test_poder_radar_simulado_detecta_barco():
    tablero = Tablero()
    tablero.colocar_barco(6, 6)
    resultados = Poderes.radar(tablero, 6, 6)
    assert resultados[(6, 6)] == 'B'
    assert len(resultados) <= 9 

def test_poder_radar_simulado_no_detecta_barco():
    tablero = Tablero()
    resultados = Poderes.radar(tablero, 2, 3)
    assert resultados[(2, 3)] == ' '

def test_rafaga_horizontal_simulada():
    tablero = Tablero()
    tablero.colocar_barco(5, 5, tamano=3, orientacion='H')
    resultados = Poderes.rafaga(tablero, 5, 5, 'H')
    for coord, mensaje in resultados:
        assert "Impacto" in mensaje

def test_rafaga_vertical_simulada_con_agua():
    tablero = Tablero()
    resultados = Poderes.rafaga(tablero, 1, 1, 'V')
    for coord, mensaje in resultados:
        assert "Simulación" in mensaje or "Fuera" not in mensaje

def test_rafaga_direccion_invalida():
    tablero = Tablero()
    with pytest.raises(ValueError):
        Poderes.rafaga(tablero, 0, 0, 'Z')  