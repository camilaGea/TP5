import tkinter as tk
from tkinter import ttk

class ResultadosMetodoNumerico:
    def __init__(self, root, D_objetivo, C):
        self.root = root
        self.root.title("Resultados del Método Numérico")

        self.D_objetivo = D_objetivo
        self.C = C

        # Crear un Frame para contener el Treeview y los scrollbars
        self.frame = ttk.Frame(root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        # Crear etiquetas para mostrar D_objetivo y C
        ttk.Label(self.frame, text=f"D_objetivo: {self.D_objetivo}").pack()
        ttk.Label(self.frame, text=f"C: {self.C}").pack()

        # Crear el Treeview para mostrar los resultados del método numérico
        self.tree = ttk.Treeview(self.frame, columns=("ti", "D", "dD/dt", "t(i+1)", "D(i+1)"), show="headings")
    
        # Configurar encabezados y anchos de columna
        columns = [("ti", 100), ("D", 100), ("dD/dt", 100), ("t(i+1)", 100), ("D(i+1)", 100)]
        for col, width in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width)
    
        # Agregar Treeview y Scrollbars al Frame
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.config(yscrollcommand=scrollbar.set)
    
    def mostrar_resultados(self, resultados):
        # Limpiar el Treeview antes de insertar nuevos datos
        for row in self.tree.get_children():
            self.tree.delete(row)
    
        # Insertar los datos de resultados en el Treeview
        for row_data in resultados:
            self.tree.insert("", "end", values=row_data)

