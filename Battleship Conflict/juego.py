import threading

class Juego:
    TIEMPO_POR_TURNO = 30  # segundos
    MAX_INACTIVIDAD_CONSECUTIVA = 2  # turnos sin acción

    def __init__(self, jugador1, jugador2):
        self.jugadores = [jugador1, jugador2]
        self.turno_actual = 0
        self.juego_terminado = False
        self.temporizador = None
        self.rondas_inactivas = 0  # 👈 NUEVO: contador de inactividad

    def iniciar_temporizador(self):
        self.cancelar_temporizador()
        self.temporizador = threading.Timer(self.TIEMPO_POR_TURNO, self.tiempo_agotado)
        self.temporizador.start()

    def tiempo_agotado(self):
        print(f"\n⏰ Tiempo agotado para el jugador {self.turno_actual + 1}. Se pasa el turno.")
        self.rondas_inactivas += 1  # 👈 aumentar inactividad
        if self.rondas_inactivas >= self.MAX_INACTIVIDAD_CONSECUTIVA:
            self.terminar_por_inactividad()
            return
        self.cambiar_turno()

    def registrar_accion(self):
        self.rondas_inactivas = 0  # 👈 reset cuando hay acción

    def terminar_por_inactividad(self):
        self.cancelar_temporizador()
        self.juego_terminado = True
        print("\n❌ Juego terminado por inactividad prolongada.")
