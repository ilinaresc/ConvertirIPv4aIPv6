import tkinter as tk
from tkinter import messagebox
import ipaddress

# Función para convertir IPv4 a IPv6
def convertir_ipv4_a_ipv6():
    ipv4 = entry_ipv4.get().strip()
    try:
        # Convierte la dirección IPv4 a IPv6
        ipv6 = ipaddress.IPv6Address("::ffff:" + ipv4)
        label_resultado.config(text=f"IPv6 Compressed: {ipv6}\nIPv6 Expanded: {ipv6.exploded}")
    except ipaddress.AddressValueError:
        messagebox.showerror("Error", "Dirección IPv4 no válida")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Conversor IPv4 a IPv6")
ventana.geometry("400x250")

# Etiqueta y cuadro de texto para ingresar la IPv4
label_ipv4 = tk.Label(ventana, text="Ingrese una Dirección IPv4:")
label_ipv4.pack(pady=10)
entry_ipv4 = tk.Entry(ventana, width=30)
entry_ipv4.pack(pady=5)

# Botón para convertir
boton_convertir = tk.Button(ventana, text="Convertir IPv4 a IPv6", command=convertir_ipv4_a_ipv6)
boton_convertir.pack(pady=10)

# Etiqueta para mostrar los resultados
label_resultado = tk.Label(ventana, text="Resultados aparecerán aquí", justify="left")
label_resultado.pack(pady=10)

# Ejecutar la ventana
ventana.mainloop()
