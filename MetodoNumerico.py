import numpy as np

class MetodoNumerico:
    def __init__(self, h, D_objetivo, C):
        self.h = h
        self.D_objetivo = D_objetivo
        self.C = C

    def metodo_euler(self, f, t0, D0):
        t_values = [t0]
        D_values = [D0]
        h = self.h
        D_objetivo = self.D_objetivo
        C = self.C

        while D0 <= D_objetivo:
            D0 = D0 + h * f(t0, D0, C)
            t0 = t0 + h
            t_values.append(t0)
            D_values.append(D0)
    
        return t_values, D_values, t0, D0
    
    # Definir la función de la ODE
    def f(t, D, C):
        return 0.6 * C + t

