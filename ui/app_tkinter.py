import tkinter as tk
from tkinter import messagebox

class AppTkinter:
    def __init__(self, root, servicio):
        self.root = root
        self.servicio = servicio

        self.root.title("Lista de Tareas")

        # Entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)

        # Botones
        self.btn_agregar = tk.Button(root, text="Agregar", command=self.agregar_tarea)
        self.btn_agregar.pack()

        self.btn_completar = tk.Button(root, text="Completar", command=self.completar_tarea)
        self.btn_completar.pack()

        self.btn_eliminar = tk.Button(root, text="Eliminar", command=self.eliminar_tarea)
        self.btn_eliminar.pack()

        # Lista
        self.lista = tk.Listbox(root, width=50)
        self.lista.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<Return>", self.agregar_tarea_evento)
        self.root.bind("c", self.completar_tarea_evento)
        self.root.bind("d", self.eliminar_tarea_evento)
        self.root.bind("<Delete>", self.eliminar_tarea_evento)
        self.root.bind("<Escape>", self.cerrar_app)

    # -------- FUNCIONES --------

    def agregar_tarea(self):
        texto = self.entry.get()
        self.servicio.agregar_tarea(texto)
        self.entry.delete(0, tk.END)
        self.actualizar_lista()

    def completar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.servicio.completar_tarea(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def eliminar_tarea(self):
        seleccion = self.lista.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self.actualizar_lista()
        else:
            messagebox.showwarning("Aviso", "Selecciona una tarea")

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)
        for tarea in self.servicio.obtener_tareas():
            estado = "✔️" if tarea.completada else "❌"
            self.lista.insert(tk.END, f"{estado} {tarea.descripcion}")

    # -------- EVENTOS TECLADO --------

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def completar_tarea_evento(self, event):
        self.completar_tarea()

    def eliminar_tarea_evento(self, event):
        self.eliminar_tarea()

    def cerrar_app(self, event):
        self.root.destroy()