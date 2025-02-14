import tkinter as tk


def abrir_ventana_secundaria():
    root.withdraw()
    # v_sec = tk.Toplevel(root)
    # v_sec.title("Crear nuevo puesto")
    # v_sec.geometry("560x220")
    # v_sec.grab_set() # Bloquear la ventana principal
    ventana_secundaria.deiconify() # Mostrar ventana secundaria
    
    # label = tk.Label(v_sec, text="Agrega la informacion", font=("Verdana", 12))
    # label.pack(pady=20)
    
    # boton_cerrar = tk.Button(v_sec, text="Cerrar", command=v_sec.destroy)
    # boton_cerrar.pack(pady=10)

def regresar_a_principal():
    ventana_secundaria.withdraw()
    root.deiconify()



root = tk.Tk()
root.title("Subir nuevos colaboradores")
root.geometry("600x250+{}+{}".format(root.winfo_screenwidth()//2 - 300, root.winfo_screenheight()//2 - 125))

ventana_secundaria = tk.Toplevel(root)
ventana_secundaria.title("Agregar nuevo puesto")
ventana_secundaria.geometry("380x240")
ventana_secundaria.withdraw() # Ocultarla al inicio

label = tk.Label(root, text="Hola Mundo!", font=("Arial", 14))
label.pack(pady=10)

abrir_ventana = tk.Button(root, text="Agregar puesto nuevo", command=abrir_ventana_secundaria)
abrir_ventana.pack(pady=50)


boton_volver = tk.Button(ventana_secundaria, text="Regresar", command=regresar_a_principal)
boton_volver.pack(pady=50)

boton = tk.Button(root, text="Cerrar", command=root.quit)
boton.pack(pady=5)

root.mainloop()

