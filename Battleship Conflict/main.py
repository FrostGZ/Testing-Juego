from tablero import Tablero
from juego import Juego

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()

def mostrar_tablero(tablero):
    for fila in tablero.celdas:
        print(" ".join(fila))

def main():
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")

    # Colocación básica de barcos (puedes mejorarla)
    jugador1.tablero.colocar_barco(0, 0, 2, 'H')
    jugador2.tablero.colocar_barco(1, 1, 2, 'V')

    juego = Juego(jugador1, jugador2)
    juego.iniciar_temporizador()

    while not juego.juego_terminado:
        jugador = juego.obtener_jugador_actual()
        print(f"\nTurno de {jugador.nombre}")
        mostrar_tablero(jugador.tablero)

        try:
            fila = int(input("Ingresa la fila del ataque: "))
            col = int(input("Ingresa la columna del ataque: "))
            oponente = juego.jugadores[1 - juego.turno_actual]
            resultado = oponente.tablero.recibir_ataque(fila, col)
            print(resultado)

            if not juego.verificar_fin_juego():
                juego.cambiar_turno()

        except ValueError:
            print("⚠️ Entrada inválida. Usa números.")
        except IndexError as e:
            print(f"⚠️ {e}")
        except KeyboardInterrupt:
            juego.cancelar_temporizador()
            print("\nJuego interrumpido.")
            break

if __name__ == "__main__":
    main()
