class Poderes:
    @staticmethod
    def radar(tablero, fila, columna):
        resultados = {}
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < tablero.filas and 0 <= j < tablero.columnas:
                    resultados[(i, j)] = tablero.celdas[i][j]
        return resultados

    @staticmethod
    def rafaga(tablero, fila, columna, direccion):
        resultados = []
        for k in range(3):
            if direccion == 'H':
                i, j = fila, columna + k
            elif direccion == 'V':
                i, j = fila + k, columna
            else:
                raise ValueError("Dirección inválida. Usa 'H' o 'V'.")

            if 0 <= i < tablero.filas and 0 <= j < tablero.columnas:
                celda = tablero.celdas[i][j]
                if celda == 'B':
                    resultados.append(((i, j), "¡Impacto simulado!"))
                elif celda == ' ':
                    resultados.append(((i, j), "Simulación: Agua."))
                else:
                    resultados.append(((i, j), "Ya atacado."))
            else:
                resultados.append(((i, j), "Fuera del tablero."))
        return resultados