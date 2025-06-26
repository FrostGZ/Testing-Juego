class Tablero:
    def __init__(self, filas=10, columnas=10):
        self.filas = filas
        self.columnas = columnas
        self.celdas = [[' ' for _ in range(columnas)] for _ in range(filas)]

    def colocar_barco(self, fila, columna, tamano=1, orientacion='H'):
        """
        Coloca un barco a partir de la celda (fila, columna)
        tamano: numero de celdas que ocupa el barco
        orientacion: 'H' para horizontal, 'V' para vertical
        """
        if orientacion not in ['H', 'V']:
            raise ValueError("Orientacion invalida. Use 'H' o 'V'.")

        # Verificar que la posicion inicial este dentro del tablero
        if fila < 0 or columna < 0 or fila >= self.filas or columna >= self.columnas:
            raise IndexError("Coordenadas fuera del tablero.")

        # Verificar que el barco no se salga del tablero
        if orientacion == 'H':
            if columna + tamano > self.columnas:
                raise IndexError("El barco se sale del tablero horizontalmente.")
            # Verificar superposicion
            for i in range(tamano):
                if self.celdas[fila][columna + i] == 'B':
                    raise ValueError("Ya hay un barco en esa posicion.")
            # Colocar el barco
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
        """Verifica si el tablero esta completamente vacio"""
        for fila in self.celdas:
            for celda in fila:
                if celda != ' ':
                    return False
        return True
