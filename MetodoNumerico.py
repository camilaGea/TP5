import numpy as np

class MetodoNumerico:
    def __init__(self, h, D_objetivo, C):
        self.h = h
        self.D_objetivo = D_objetivo
        self.C = C

    # Función para el método numérico de Euler
    def metodo_euler(self):
        t = 0
        D = 0
        h = self.h  # tamaño del paso en t
        D_objetivo = self.D_objetivo
        C= self.C
        resultados = []
    
        while D < D_objetivo:
            dD_dt = (0.6 * C) + t
            t_next = round(t + h,10)
            D_next = D + (dD_dt * h)
            resultados.append((t, D, dD_dt, t_next, D_next))
            t = t_next
            D = D_next

        if D > D_objetivo:
            dD_dt = (0.6 * C) + t
            t_next = round(t + h,10)
            D_next = D + (dD_dt * h)
            resultados.append((t, D, dD_dt, t_next, D_next))

        return resultados


    # Definir la función de la ODE
    #def f(t, D, C):
    #    return 0.6 * C + t

    def metodo_euler2(self):
        h = self.h
        D_objetivo = self.D_objetivo
        C = self.C
        t = 0
        D = 0

        while D < D_objetivo:
            dD_dt = (0.6 * C) + t
            t_next = round(t + h,10)
            D_next = D + (dD_dt * h)
           
            t = t_next
            D = D_next

        return t_next
    
