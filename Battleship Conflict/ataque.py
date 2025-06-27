class Ataque:
    @staticmethod
    def ejecutar(tablero, fila, col):
        if not (0 <= fila < len(tablero.celdas)) or not (0 <= col < len(tablero.celdas[0])):
            raise IndexError("Ataque fuera de los límites del tablero")

        celda = tablero.celdas[fila][col]
        if celda in ['X', 'O']:
            return "Ya atacaste esta casilla."

        if celda == 'B':
            tablero.celdas[fila][col] = 'X'
            if not any('B' in fila_actual for fila_actual in tablero.celdas):
                return "¡Impacto! Has destruido el último barco."
            return "¡Impacto!"
        else:
            tablero.celdas[fila][col] = 'O'
            return "Agua."
