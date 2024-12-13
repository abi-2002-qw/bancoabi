##vanessa abigail alvarado elizalde ##
#hacer un banco con usuario y contraceña  para cada persona
#nombre apellido cedula eleguir entre ahorros y coriiente #
#bienvenido a banco abibi
import tkinter as tk
from tkinter import messagebox

class Usuario:
    def __init__(self, nombre, apellido, cedula, tipo_cuenta):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.tipo_cuenta = tipo_cuenta

    def __str__(self):
        return f"Usuario: {self.nombre} {self.apellido}, Cédula: {self.cedula}, Tipo de Cuenta: {self.tipo_cuenta}"

class BancoAbibi:
    def __init__(self):
        self.usuarios = []

    def anadir_usuario(self, nombre, apellido, cedula, tipo_cuenta):
        if tipo_cuenta not in ['ahorros', 'corriente']:
            messagebox.showerror("Error", "Tipo de cuenta no válido. Debe ser 'ahorros' o 'corriente'.")
            return
        
        nuevo_usuario = Usuario(nombre, apellido, cedula, tipo_cuenta)
        self.usuarios.append(nuevo_usuario)
        messagebox.showinfo("Éxito", f"Usuario {nombre} {apellido} añadido exitosamente.")

    def mostrar_usuarios(self):
        if not self.usuarios:
            messagebox.showinfo("Usuarios", "No hay usuarios registrados.")
            return
        
        usuarios_info = "\n".join(str(usuario) for usuario in self.usuarios)
        messagebox.showinfo("Usuarios Registrados", usuarios_info)

class AplicacionBanco:
    def __init__(self, root):
        self.banco = BancoAbibi()
        self.root = root
        self.root.title("BANCO ABIBI")
        self.root.configure(bg='pink')

        # entradass
        tk.Label(root, text="Nombre:", bg='pink').grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(root, text="Apellido:", bg='pink').grid(row=1, column=0, padx=10, pady=10)
        self.entry_apellido = tk.Entry(root)
        self.entry_apellido.grid(row=1, column=1)

        tk.Label(root, text="Cédula:", bg='pink').grid(row=2, column=0, padx=10, pady=10)
        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.grid(row=2, column=1)

        tk.Label(root, text="Tipo de Cuenta:", bg='pink').grid(row=3, column=0, padx=10, pady=10)
        self.entry_tipo_cuenta = tk.Entry(root)
        self.entry_tipo_cuenta.grid(row=3, column=1)

        #####botones principales #anadir usuario # #mostrar usuario #
        tk.Button(root, text="Añadir Usuario", command=self.añadir_usuario).grid(row=4, column=0, columnspan=2, pady=10)
        tk.Button(root, text="Mostrar Usuarios", command=self.mostrar_usuarios).grid(row=5, column=0, columnspan=2, pady=10)

    def añadir_usuario(self): ##botones visuales disponibles ##
        nombre = self.entry_nombre.get()
        apellido = self.entry_apellido.get()
        cedula = self.entry_cedula.get()
        tipo_cuenta = self.entry_tipo_cuenta.get().lower()
        self.banco.anadir_usuario(nombre, apellido, cedula, tipo_cuenta)

    def mostrar_usuarios(self):
        self.banco.mostrar_usuarios()

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionBanco(root)
    root.mainloop()
 

