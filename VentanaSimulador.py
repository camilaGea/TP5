import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import Scrollbar
from Fila import Fila
from ResultadosMetodoNumerico import ResultadosMetodoNumerico
from ResultadosVentana import ResultadosVentana

class VentanaSimulador:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulación de Problemas de Colas")

        # Crear un marco para contener los widgets
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Crear y colocar los widgets de entrada
        self.create_widgets()

    def truncar(self, numero, decimales=3):
        factor = 10 ** decimales
        return int(numero * factor) / factor
    
    def create_widgets(self):
        labels_text = [
            "Cantidad de tiempo (X):", "Media de llegada de equipo de fútbol:(hs)",
            "Intervalo inferior de llegada de equipo de básquet:(hs)", "Intervalo superior de llegada de equipo de básquet:(hs)",
            "Intervalo inferior de llegada de equipo de handball:(hs)", "Intervalo superior de llegada de equipo de handball:(hs)",
            "Intervalo inferior de fin de ocupación de equipo de fútbol:(min)", "Intervalo superior de fin de ocupación de equipo de fútbol:(min)",
            "Intervalo inferior de fin de ocupación de equipo de básquet:(min)", "Intervalo superior de fin de ocupación de equipo de básquet:(min)",
            "Intervalo inferior de fin de ocupación de equipo de handball:(min)", "Intervalo superior de fin de ocupación de equipo de handball:(min)",
            "Cantidad de equipos en cola máxima:", "D para futbol: ", "D para Handball: ","D para Basquet: ", "h: ", 
            "Cantidad de filas a mostrar (I):", "Hora específica a mostrar (J):"
        ]
        default_values = [1000, 10, 6, 10, 10, 14, 80, 100, 70, 130, 60, 100, 5,100,200,300,0.1,100, 0]
        self.entries = []
        for i, (text, default) in enumerate(zip(labels_text, default_values)):
            ttk.Label(self.frame, text=text).grid(column=0, row=i, sticky=tk.W)
            entry = ttk.Entry(self.frame)
            entry.grid(column=1, row=i, sticky=(tk.W, tk.E))
            entry.insert(0, str(default))
            self.entries.append(entry)

        # Botón para iniciar la simulación
        ttk.Button(self.frame, text="Iniciar Simulación", command=self.iniciar_simulacion).grid(column=1, row=len(labels_text), sticky=tk.E)

        # Configuración para que los widgets se ajusten al tamaño de la ventana
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def iniciar_simulacion(self):
        # Obtener los valores de los campos de entrada
        params = [entry.get() for entry in self.entries]
        tiempo_total = int(params[0])
        #tiempo_demora_limpieza = self.truncar(float(params[1]) / 60)
        media_llegada_futbol = float(params[1])
        intervalo_llegada_basquet_inf = float(params[2])
        intervalo_llegada_basquet_sup = float(params[3])
        intervalo_llegada_handball_inf = float(params[4])
        intervalo_llegada_handball_sup = float(params[5])
        fin_ocupacion_futbol_inf = self.truncar(float(params[6]) / 60)
        fin_ocupacion_futbol_sup = self.truncar(float(params[7]) / 60)
        fin_ocupacion_basquet_inf = self.truncar(float(params[8]) / 60)
        fin_ocupacion_basquet_sup = self.truncar(float(params[9]) / 60)
        fin_ocupacion_handball_inf = self.truncar(float(params[10]) / 60)
        fin_ocupacion_handball_sup = self.truncar(float(params[11]) / 60)
        cantidad_equipos_max = int(params[12])
        D_futbol = int(params[13])
        D_Handball = int(params[14])
        D_Basquet = int(params[15])
        h_metodo_numerico = float(params[16])
        cantidad_filas = int(params[17])
        hora_especifica = int(params[18])
    
        datos = [tiempo_total, media_llegada_futbol, intervalo_llegada_basquet_inf, intervalo_llegada_basquet_sup, 
             intervalo_llegada_handball_inf, intervalo_llegada_handball_sup, fin_ocupacion_futbol_inf, fin_ocupacion_futbol_sup,
             fin_ocupacion_basquet_inf, fin_ocupacion_basquet_sup, fin_ocupacion_handball_inf, fin_ocupacion_handball_sup, 
             D_futbol, D_Handball, D_Basquet, h_metodo_numerico,cantidad_equipos_max]
        tabla  = []
        colas = []
        d = dict()
        estados = dict()
        for i in range(100000):
            if i == 0:
                fila = Fila(i+1)
                lista = fila.simular(datos)
                tabla.append(fila)
                colas.append([len(fila.colaB), len(fila.colaFyH)])
                d[fila.id] = fila.objetos
                estados[fila.id] = []
            else:
                if fila.reloj >= tiempo_total:
                    tabla.pop()
                    break
                else:
                    ob = []
                    metodoNumerico = []
                    fila = Fila(i+1, lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8], lista[9])
                    lista = fila.simular(datos)
                    for vec in fila.vectorMetodoNumerico:
                        metodoNumerico.append(vec)
                    tabla.append(fila)
                    colas.append([len(fila.colaB), len(fila.colaFyH)])
                    for obj in fila.objetos:
                        ob.append(obj.estado)
                    d[fila.id] = [*fila.objetos] if len(fila.objetos) > 0 else []
                    estados[fila.id] = [*ob] if len(fila.objetos) > 0 else []
                    
        root_resultados = tk.Tk()
        resultados_ventana = ResultadosVentana(root_resultados)
        resultados_ventana.mostrar_resultados(tabla, hora_especifica, cantidad_filas, colas, d, estados)
        resultados_metodoNumerico = ResultadosMetodoNumerico(root_resultados)
        resultados_metodoNumerico.mostrar_resultados(metodoNumerico)
        
if __name__ == "__main__":
    root = tk.Tk()
    ventana_simulador = VentanaSimulador(root)
    root.mainloop()
    