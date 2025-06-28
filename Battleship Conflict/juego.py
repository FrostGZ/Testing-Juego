import threading

class Juego:
    TIEMPO_POR_TURNO = 30  # segundos
    MAX_INACTIVIDAD_CONSECUTIVA = 2

    def __init__(self, jugador1, jugador2):
        self.jugadores = [jugador1, jugador2]
        self.turno_actual = 0
        self.juego_terminado = False
        self.temporizador = None
        self.rondas_inactivas = 0

    def iniciar_temporizador(self):
        self.cancelar_temporizador()
        self.temporizador = threading.Timer(self.TIEMPO_POR_TURNO, self.tiempo_agotado)
        self.temporizador.start()

    def cancelar_temporizador(self):
        if self.temporizador:
            self.temporizador.cancel()

    def tiempo_agotado(self):
        print(f"\n⏰ Tiempo agotado para el jugador {self.turno_actual + 1}. Se pasa el turno.")
        self.rondas_inactivas += 1
        if self.rondas_inactivas >= self.MAX_INACTIVIDAD_CONSECUTIVA:
            self.terminar_por_inactividad()
            return
        self.cambiar_turno()

    def cambiar_turno(self):
        self.turno_actual = 1 - self.turno_actual
        self.iniciar_temporizador()

    def obtener_jugador_actual(self):
        return self.jugadores[self.turno_actual]

    def verificar_fin_juego(self):
        for i, jugador in enumerate(self.jugadores):
            if jugador.tablero.todos_barcos_hundidos():
                self.cancelar_temporizador()
                print("\n🎉 ¡Juego terminado!")
                print(f"🏆 El ganador es el jugador {2 if i == 0 else 1}")
                print(f"Barcos restantes del ganador: {self.contar_barcos(self.jugadores[1 - i].tablero)}")
                self.juego_terminado = True
                return True
        return False

    def registrar_accion(self):
        self.rondas_inactivas = 0

    def terminar_por_inactividad(self):
        self.cancelar_temporizador()
        self.juego_terminado = True
        print("\n❌ Juego terminado por inactividad prolongada.")

    @staticmethod
    def contar_barcos(tablero):
        return sum(fila.count('B') for fila in tablero.celdas)
