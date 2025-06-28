from tablero import Tablero
from juego import Juego
from poderes import Poderes
import datetime

LOG_ARCHIVO = "registro_juego.txt"

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tablero = Tablero()

def escribir_log(mensaje):
    with open(LOG_ARCHIVO, "a", encoding="utf-8") as f:
        f.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {mensaje}\n")

def mostrar_tablero(tablero):
    for fila in tablero.celdas:
        print(" ".join(fila))

def main():
    jugador1 = Jugador("Jugador 1")
    jugador2 = Jugador("Jugador 2")

    jugador1.tablero.colocar_barco(0, 0, 2, 'H')
    jugador2.tablero.colocar_barco(1, 1, 3, 'V')

    open(LOG_ARCHIVO, "w").close()  # Limpia log anterior
    escribir_log("🔄 Juego iniciado.")
    juego = Juego(jugador1, jugador2)
    juego.iniciar_temporizador()

    while not juego.juego_terminado:
        jugador = juego.obtener_jugador_actual()
        oponente = juego.jugadores[1 - juego.turno_actual]

        print(f"\n🎯 Turno de {jugador.nombre}")
        mostrar_tablero(oponente.tablero)
        escribir_log(f"🎯 Turno de {jugador.nombre}")

        print("\nElige una acción:")
        print("1. Atacar")
        print("2. Usar Radar")
        print("3. Usar Ráfaga")

        try:
            opcion = input("Opción: ").strip()

            if opcion == "1":
                fila = int(input("Fila para atacar: "))
                col = int(input("Columna para atacar: "))
                resultado = oponente.tablero.recibir_ataque(fila, col)
                print(f"🛠 Resultado: {resultado}")
                escribir_log(f"{jugador.nombre} atacó a ({fila}, {col}) -> {resultado}")
                juego.registrar_accion()

            elif opcion == "2":
                fila = int(input("Fila central del radar: "))
                col = int(input("Columna central del radar: "))
                resultados = Poderes.radar(oponente.tablero, fila, col)
                print("\n🔍 Resultados del Radar:")
                for (f, c), valor in resultados.items():
                    print(f"({f},{c}) -> {valor}")
                escribir_log(f"{jugador.nombre} usó Radar en ({fila}, {col}) -> {resultados}")
                juego.registrar_accion()

            elif opcion == "3":
                fila = int(input("Fila inicial: "))
                col = int(input("Columna inicial: "))
                direccion = input("Dirección (H/V): ").strip().upper()
                resultados = Poderes.rafaga(oponente.tablero, fila, col, direccion)
                print("\n💥 Resultados de la Ráfaga:")
                for (f, c), mensaje in resultados:
                    print(f"({f},{c}) -> {mensaje}")
                escribir_log(f"{jugador.nombre} usó Ráfaga desde ({fila}, {col}) dirección {direccion} -> {resultados}")
                juego.registrar_accion()

            else:
                print("⚠️ Opción inválida.")

            if not juego.verificar_fin_juego():
                escribir_log("🔁 Cambio de turno.")
                juego.cambiar_turno()

        except ValueError:
            print("⚠️ Entrada inválida. Usa números.")
        except IndexError as e:
            print(f"⚠️ {e}")
        except KeyboardInterrupt:
            juego.cancelar_temporizador()
            escribir_log("🛑 Juego interrumpido manualmente.")
            print("\nJuego interrumpido.")
            break

    # Al finalizar el juego
    if juego.juego_terminado:
        if juego.rondas_inactivas >= juego.MAX_INACTIVIDAD_CONSECUTIVA:
            print("❌ El juego terminó por inactividad prolongada. Resultado: EMPATE.")
            escribir_log("❌ Juego terminado por inactividad prolongada. Resultado: EMPATE.")
        else:
            ganador = juego.jugadores[1 - juego.turno_actual]
            barcos_restantes = juego.contar_barcos(ganador.tablero)
            print(f"🎉 ¡El ganador es {ganador.nombre} con {barcos_restantes} barcos restantes!")
            escribir_log(f"🏁 Juego terminado. Ganador: {ganador.nombre} con {barcos_restantes} barcos restantes.")

if __name__ == "__main__":
    main()
