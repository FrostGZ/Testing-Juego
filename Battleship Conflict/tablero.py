from ataque import Ataque

class Tablero:
    def __init__(self, filas=10, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.celdas = [[' ' for _ in range(columnas)] for _ in range(filas)]

    def colocar_barco(self, fila, columna, tamano=1, orientacion='H'):
        if orientacion not in ['H', 'V']:
            raise ValueError("Orientacion invalida. Use 'H' o 'V'.")

        if fila < 0 or columna < 0 or fila >= self.filas or columna >= self.columnas:
            raise IndexError("Coordenadas fuera del tablero.")

        if orientacion == 'H':
            if columna + tamano > self.columnas:
                raise IndexError("El barco se sale del tablero horizontalmente.")
            for i in range(tamano):
                if self.celdas[fila][columna + i] == 'B':
                    raise ValueError("Ya hay un barco en esa posicion.")
            for i in range(tamano):
                self.celdas[fila][columna + i] = 'B'

        elif orientacion == 'V':
            if fila + tamano > self.filas:
                raise IndexError("El barco se sale del tablero verticalmente.")
            for i in range(tamano):
                if self.celdas[fila + i][columna] == 'B':
                    raise ValueError("Ya hay un barco en esa posicion.")
            for i in range(tamano):
                self.celdas[fila + i][columna] = 'B'

    def esta_vacio(self):
        for fila in self.celdas:
            for celda in fila:
                if celda != ' ':
                    return False
        return True

    def recibir_ataque(self, fila, columna):
        return Ataque.ejecutar(self, fila, columna)

    def todos_barcos_hundidos(self):
        for fila in self.celdas:
            if 'B' in fila:
                return False
        return True
