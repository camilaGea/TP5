import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import Scrollbar

class ResultadosMetodoNumerico:
    def __init__(self, root ):
        self.root = root
        #self.frame = frame
        self.root.title("Resultados del metodo numerico")

         # Crear un Frame para contener el Treeview y los scrollbars
        self.frame = ttk.Frame(root)
        self.frame.pack(expand=True, fill=tk.BOTH)

    # Crear el Treeview para mostrar los resultados de la simulación
        self.tree = ttk.Treeview(self.frame, columns=("ID", "ti", "tvector","Di"), show="headings")
    
    # Configurar encabezados y anchos de columna
        columns = [
            ("ID", 50), ("ti", 50), ("tvector", 50),("Di", 50) 
        ]
    
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)

        # Agregar Treeview y Scrollbars al Frame
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)


    def mostrar_resultados(self, metodoNumerico):
        # Limpiar el Treeview antes de insertar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Insertar los datos de tabla_resultados en el Treeview
        for vector in metodoNumerico:
                values = (vector[0], vector[1], vector[2], vector[3])
                self.tree.insert("", "end", values=values)