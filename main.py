import tkinter as tk
from tkinter import messagebox
from models import producto  # Asegúrate de que esto sea correcto

class TiendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tienda en Línea")

        # Crear un frame
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Etiquetas y entradas
        tk.Label(self.frame, text="Nombre del Producto:").grid(row=0, column=0, sticky="w")
        self.nombre_entry = tk.Entry(self.frame)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Precio del Producto:").grid(row=1, column=0, sticky="w")
        self.precio_entry = tk.Entry(self.frame)
        self.precio_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Cantidad del Producto:").grid(row=2, column=0, sticky="w")
        self.cantidad_entry = tk.Entry(self.frame)
        self.cantidad_entry.grid(row=2, column=1)

        # Botón para agregar producto
        self.agregar_btn = tk.Button(self.frame, text="Agregar Producto", command=self.agregar_producto)
        self.agregar_btn.grid(row=3, columnspan=2)

        # Lista de productos
        self.lista_productos = tk.Listbox(self.frame, width=50)
        self.lista_productos.grid(row=4, columnspan=2, pady=10)

    def agregar_producto(self):
        # Obtener datos de las entradas
        nombre = self.nombre_entry.get()
        try:
            precio = float(self.precio_entry.get())
            cantidad = int(self.cantidad_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores válidos para precio y cantidad.")
            return

        # Crear una instancia del producto usando el módulo 'producto'
        productoUno = producto.productos(nombre, precio, cantidad)  

        # Mostrar información del producto en la lista
        self.lista_productos.insert(tk.END, f"{productoUno.nombre} - ${productoUno.precio:.2f} - cantidad: {productoUno.cantidad}")

        # Limpiar entradas
        self.nombre_entry.delete(0, tk.END)
        self.precio_entry.delete(0, tk.END)
        self.cantidad_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TiendaApp(root)
    root.mainloop()
