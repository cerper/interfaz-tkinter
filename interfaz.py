from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
from tkinter import PhotoImage

#creando la root
root = Tk()
root.title("Registro Civil - David Lovera")
root.geometry("900x680")
root.configure(bg="#e3eaf2")

#utilizando ttk para dar estilo
style = ttk.Style()
style.theme_use('clam')

#estilo para el boton de agregar
style.configure("Add.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="#00b894",
                borderwidth=0,
                focusthickness=3,
                focuscolor='none',
                padding=10)
style.map("Add.TButton", 
          background=[('active', '#00cec9')],
          foreground=[('active', 'black')])

#estilo para el boton de ver datos
style.configure("View.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="#0984e3",
                borderwidth=0,
                focusthickness=3,
                focuscolor='none',
                padding=10)
style.map("View.TButton", 
          background=[('active', '#74b9ff')],
          foreground=[('active', 'black')])

#estilo para el boton de actualizar datos
style.configure("Update.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",                
                background="#bfa100",              
                borderwidth=0,
                focusthickness=3,
                focuscolor='none',
                padding=10)
style.map("Update.TButton", 
          background=[('active', "#dbc16d")],
          foreground=[('active', 'black')])

#estilo para el boton de borrar datos
style.configure("Delete.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="#ee5253",
                borderwidth=0,
                focusthickness=3,
                focuscolor='none',
                padding=10)
style.map("Delete.TButton", 
          background=[('active', '#ff7675')],
          foreground=[('active', 'black')])

style.configure("Search.TButton",
                font=("Arial", 12, "bold"),
                foreground="white",
                background="#6c5ce7",
                borderwidth=0,
                focusthickness=3,
                focuscolor='none',
                padding=10)

#estilo para el boton de buscar
style.map("Search.TButton", 
          background=[('active', '#a29bfe')],
          foreground=[('active', 'black')])

style.configure("Rounded.TEntry",
                font=("Arial", 12),
                fieldbackground="#fffbe7",
                borderwidth=0,
                relief="flat",
                padding=8)


# Estilo personalizado para Combobox 
style.configure("CustomCombobox.TCombobox",
                fieldbackground="#eaeaea",  
                background="#eaeaea",       
                foreground="#222f3e",      
                bordercolor="#eaeaea",
                lightcolor="#eaeaea",
                darkcolor="#eaeaea",
                arrowcolor="#00b894",
                selectbackground="#eaeaea",  
                selectforeground="#222f3e",  
                padding=8)

style.map("CustomCombobox.TCombobox",
          fieldbackground=[('readonly', '#eaeaea')],
          background=[('readonly', '#eaeaea')],
          selectbackground=[('readonly', '#eaeaea')],
          selectforeground=[('readonly', '#222f3e')])



#titulo del frame
Label(root, text="Registro Civil", font=("Arial", 22, "bold"), bg="#e3eaf2", fg="#1e3799").pack(pady=(15, 0))
Label(root, text="Agrega, busca, actualiza o elimina usuarios fácilmente.", font=("Arial", 13), bg="#e3eaf2", fg="#222f3e").pack()

frame = Frame(root, bg="#f9fafc", bd=3, relief="ridge")
frame.pack(padx=30, pady=20, fill="both", expand=True)
#posicionando contenido en el frame
frame.columnconfigure(0, weight=0)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

name = StringVar()
apell = StringVar()
cedula = StringVar()
radio_var = StringVar()
estado_civil = StringVar()
direccion = StringVar()



#creando funcion para agregar datos
def insertar_datos(nombre, apellido, cedula_val, radio_var_val, estado_civil_val, direccion_val):
    campos_faltantes = []
    # Limpiar bordes previos
    name_entry.configure(style="Rounded.TEntry")
    apell_entry.configure(style="Rounded.TEntry")
    cedula_entry.configure(style="Rounded.TEntry")
    estado_civil_combo.configure(style="CustomCombobox.TCombobox")
    direccion_entry.configure(style="Rounded.TEntry")
    # Validar campos y marcar en rojo los vacíos
    if not nombre or nombre.strip() == "" or nombre == "Ej: Juan":
        campos_faltantes.append("Nombre")
        name_entry.configure(style="Error.TEntry")
    if not apellido or apellido.strip() == "" or apellido == "Ej: Pérez":
        campos_faltantes.append("Apellido")
        apell_entry.configure(style="Error.TEntry")
    if not cedula_val or cedula_val.strip() == "" or cedula_val == "Ej: 12345678":
        campos_faltantes.append("Cédula")
        cedula_entry.configure(style="Error.TEntry")
    if not radio_var_val:
        campos_faltantes.append("Género")
    if not estado_civil_val:
        campos_faltantes.append("Estado Civil")
        estado_civil_combo.configure(style="Error.TCombobox")
    if not direccion_val or direccion_val.strip() == "" or direccion_val == "Ej: Av. Principal #123, Ciudad":
        campos_faltantes.append("Dirección")
        direccion_entry.configure(style="Error.TEntry")

    if campos_faltantes:
        mensaje = "Por favor, complete todos los campos.\nFaltan por llenar: " + ", ".join(campos_faltantes)
        messagebox.showwarning("Advertencia", mensaje)
        return

    conexion = sqlite3.connect('tarea.db')
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tarea (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre varchar(50), apellido varchar(100), cedula varchar(20), genero varchar(20), estado_civil varchar(20), direccion varchar(200))")
    cursor.execute("INSERT INTO tarea (nombre, apellido, cedula, genero, estado_civil, direccion) VALUES (?, ?, ?, ?, ?, ?)", (nombre, apellido, cedula_val, radio_var_val, estado_civil_val, direccion_val))
    conexion.commit()
    conexion.close()
    messagebox.showinfo("Éxito", "Datos insertados correctamente.")
    name.set("")
    apell.set("")
    cedula.set("")  # Aquí cedula es el StringVar global
    radio_var.set("")
    estado_civil.set("")
    direccion.set("")
    # Restaurar estilos normales
    name_entry.configure(style="Rounded.TEntry")
    apell_entry.configure(style="Rounded.TEntry")
    cedula_entry.configure(style="Rounded.TEntry")
    estado_civil_combo.configure(style="CustomCombobox.TCombobox")
    direccion_entry.configure(style="Rounded.TEntry")
    cedula_entry.delete(0, "end")
    set_placeholder(cedula_entry, "Ej: 12345678")
    direccion_entry.delete(0, "end")
    set_placeholder(direccion_entry, "Ej: Av. Principal #123, Ciudad")

# Agrega estos estilos al inicio, después de tus otros estilos:
style.configure("Error.TEntry",
                font=("Arial", 12),
                fieldbackground="#fffbe7",
                borderwidth=2,
                relief="flat",
                padding=8,
                bordercolor="#e74c3c",
                highlightthickness=2,
                highlightbackground="#e74c3c")

style.configure("Error.TCombobox",
                fieldbackground="#fffbe7",
                background="#fffbe7",
                foreground="#222f3e",
                bordercolor="#e74c3c",
                lightcolor="#e74c3c",
                darkcolor="#e74c3c",
                arrowcolor="#e74c3c",
                selectbackground="#fffbe7",
                selectforeground="#222f3e",
                padding=8)

#creando funcion para ver datos
def ver_datos():
    conexion = None
    try:
        conexion = sqlite3.connect('tarea.db')
        cursor = conexion.cursor()
        
       
        cursor.execute("SELECT COUNT(*) FROM tarea")
        cantidad = cursor.fetchone()[0]
        
        if cantidad == 0:
            messagebox.showinfo("Sin datos", "No hay datos en la base de datos.")
        else:
            root2 = Toplevel()
            root2.title("Viendo datos")
            root2.geometry("800x500")
            root2.configure(bg="#e3eaf2")
            
            frame2 = Frame(root2, bg="#f9fafc", bd=3, relief="ridge")
            frame2.pack(padx=20, pady=20, fill="both", expand=True)

            # Estilo para el Treeview
            style.configure("Treeview", 
                            background="#f0f0f0", 
                            foreground="#222f3e", 
                            rowheight=25, 
                            fieldbackground="#f9fafc")
            style.map('Treeview', background=[('selected', '#5a90e3')])
            style.configure("Treeview.Heading", font=("Arial", 11, "bold"), background="#1e3799", foreground="white")

            # Crear el Treeview
            tree = ttk.Treeview(frame2, style="Treeview")
            tree["columns"] = ("id", "nombre", "apellido", "cedula", "genero", "estado_civil", "direccion")
            
            # Configurar las columnas
            tree.column("#0", width=0, stretch=NO)  # Columna fantasma
            tree.column("id", anchor=CENTER, width=50)
            tree.column("nombre", anchor=W, width=100)
            tree.column("apellido", anchor=W, width=120)
            tree.column("cedula", anchor=CENTER, width=100)
            tree.column("genero", anchor=CENTER, width=80)
            tree.column("estado_civil", anchor=CENTER, width=100)
            tree.column("direccion", anchor=W, width=200)

            # Crear los encabezados
            tree.heading("#0", text="", anchor=CENTER)
            tree.heading("id", text="ID", anchor=CENTER)
            tree.heading("nombre", text="Nombre", anchor=CENTER)
            tree.heading("apellido", text="Apellido", anchor=CENTER)
            tree.heading("cedula", text="Cédula", anchor=CENTER)
            tree.heading("genero", text="Género", anchor=CENTER)
            tree.heading("estado_civil", text="E. Civil", anchor=CENTER)
            tree.heading("direccion", text="Dirección", anchor=CENTER)

            # Obtener datos de la base de datos
            cursor.execute("SELECT * FROM tarea")
            datos = cursor.fetchall()

            # Insertar datos en el Treeview
            for dato in datos:
                tree.insert(parent='', index='end', iid=dato[0], values=dato)

            # Scrollbars
            scrollbar_y = ttk.Scrollbar(frame2, orient="vertical", command=tree.yview)
            scrollbar_x = ttk.Scrollbar(frame2, orient="horizontal", command=tree.xview)
            tree.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)

            # Posicionar el Treeview y los scrollbars
            tree.grid(row=0, column=0, sticky='nsew')
            scrollbar_y.grid(row=0, column=1, sticky='ns')
            scrollbar_x.grid(row=1, column=0, sticky='ew')
            
            # Configurar el grid para que el Treeview se expanda
            frame2.grid_rowconfigure(0, weight=1)
            frame2.grid_columnconfigure(0, weight=1)

    except sqlite3.OperationalError:
        messagebox.showinfo("Sin datos", "¡La base de datos no se ha creado!\nNo hay información para mostrar.")
        
    finally:
        if conexion:
            conexion.close()
# Función para verificar si hay datos antes de abrir la ventana
def check_db_and_open_window(action_function):
    try:
        conexion = sqlite3.connect('tarea.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM tarea")
        cantidad = cursor.fetchone()[0]
        conexion.close()
        
        if cantidad == 0:
            messagebox.showinfo("Sin datos", "No hay datos en la base de datos para realizar esta acción.")
        else:
            action_function()
            
    except sqlite3.OperationalError:
        messagebox.showinfo("Sin datos", "¡La base de datos no se ha creado!\nNo hay información para realizar esta acción.")


#creando funcion para eliminar datos
def eliminar_datos():
    
    ventana_eliminar = Toplevel()
    ventana_eliminar.title("Eliminar Registro")
    ventana_eliminar.geometry("400x200")
    ventana_eliminar.configure(bg="#e3eaf2")
    frame_eliminar = Frame(ventana_eliminar, bg="#f9fafc", bd=2, relief="groove")
    frame_eliminar.pack(padx=20, pady=20, fill="both", expand=True)
    id_eliminar = IntVar(value=0)

    Label(frame_eliminar, text="ID a eliminar:", font=("Arial", 12), bg="#f9fafc").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_eliminar, textvariable=id_eliminar, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)

    def confirmar_eliminacion():
        conexion = sqlite3.connect("tarea.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tarea WHERE id=?", (id_eliminar.get(),))
        if cursor.fetchone() is not None:
            cursor.execute("DELETE FROM tarea WHERE id=?", (id_eliminar.get(),))
            conexion.commit()
            conexion.close()
            messagebox.showinfo("Eliminar", "Registro eliminado correctamente.")
            ventana_eliminar.destroy()
        else:
            messagebox.showwarning("Advertencia", "ID no encontrado. Por favor, ingrese un ID válido.")
            conexion.close()

    Button(frame_eliminar, text="Eliminar", font=("Arial", 12, "bold"), bg="#ee5253", fg="white", activebackground="#ff6b6b", activeforeground="white", command=confirmar_eliminacion).grid(row=1, column=0, columnspan=2, pady=15)

#creando funcion para actualizar los datos
def actualizar_datos():
    
    update_win = Toplevel()
    update_win.title("Actualizar Registro")
    update_win.geometry("500x450")
    update_win.configure(bg="#e3eaf2")
    frame_update = Frame(update_win, bg="#f9fafc", bd=2, relief="groove")
    frame_update.pack(padx=20, pady=20, fill="both", expand=True)

    id_var = IntVar()
    nombre_var = StringVar()
    apellido_var = StringVar()
    cedula_var = StringVar()
    genero_var = StringVar()

    Label(frame_update, text="ID a actualizar:", font=("Arial", 12), bg="#f9fafc").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_update, textvariable=id_var, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)

    Label(frame_update, text="Nuevo Nombre:", font=("Arial", 12), bg="#f9fafc").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_update, textvariable=nombre_var, font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5)

    Label(frame_update, text="Nuevo Apellido:", font=("Arial", 12), bg="#f9fafc").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_update, textvariable=apellido_var, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)

    Label(frame_update, text="Nueva Cédula:", font=("Arial", 12), bg="#f9fafc").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_update, textvariable=cedula_var, font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=5)

    Label(frame_update, text="Nuevo Género (M/F):", font=("Arial", 12), bg="#f9fafc").grid(row=4, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_update, textvariable=genero_var, font=("Arial", 12)).grid(row=4, column=1, padx=10, pady=5)

    # Agrega el Combobox para el nivel académico en la ventana de actualización
    estado_civil_var = StringVar()
    Label(frame_update, text="Nuevo Estado Civil:", font=("Arial", 12), bg="#f9fafc").grid(row=5, column=0, padx=10, pady=5, sticky="e")
    estado_civil_combo = ttk.Combobox(frame_update, textvariable=estado_civil_var, state="readonly", font=("Arial", 12), style="CustomCombobox.TCombobox")
    estado_civil_combo['values'] = ("Soltero", "Casado", "Viudo", "Divorciado")
    estado_civil_combo.grid(row=5, column=1, padx=10, pady=5, ipady=3, sticky="ew", columnspan=2)
    estado_civil_combo.set("Soltero") 

    direccion_var = StringVar()
    Label(frame_update, text="Nueva Dirección:", font=("Arial", 12), bg="#f9fafc").grid(row=6, column=0, padx=10, pady=5, sticky="e")
    direccion_entry_update = ttk.Entry(frame_update, textvariable=direccion_var, style="Rounded.TEntry")
    direccion_entry_update.grid(row=6, column=1, padx=10, pady=5, ipady=5, sticky="ew", columnspan=2)
    set_placeholder(direccion_entry_update, "Ej: Av. Principal #123, Ciudad")

    def guardar_actualizacion():
        conexion = sqlite3.connect('tarea.db')
        cursor = conexion.cursor()
        
        if not id_var.get() or not nombre_var.get() or not apellido_var.get() or not cedula_var.get() or not genero_var.get() or not estado_civil_var.get() or not direccion_var.get():
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return
        
        cursor.execute(
            "UPDATE tarea SET nombre=?, apellido=?, cedula=?, genero=?, estado_civil=?, direccion=? WHERE id=?",
            (nombre_var.get(), apellido_var.get(), cedula_var.get(), genero_var.get(), estado_civil_var.get(), direccion_var.get(), id_var.get())
        )
        conexion.commit()
        conexion.close()
        messagebox.showinfo("Actualización", "Registro actualizado correctamente.")
        update_win.destroy()

    Button(frame_update, text="Actualizar", font=("Arial", 12, "bold"), bg="#54a0ff", fg="white", activebackground="#2e86de", activeforeground="white", command=guardar_actualizacion).grid(row=7, column=0, columnspan=2, pady=15)

#creando funcion para buscar usuario 
def buscar_usuario():
   
    buscar_win = Toplevel()
    buscar_win.title("Buscar Usuario por ID")
    buscar_win.geometry("400x300")
    buscar_win.configure(bg="#e3eaf2")
    frame_buscar = Frame(buscar_win, bg="#f9fafc", bd=2, relief="groove")
    frame_buscar.pack(padx=20, pady=20, fill="both", expand=True)

    id_buscar = IntVar()

    Label(frame_buscar, text="ID a buscar:", font=("Arial", 12), bg="#f9fafc").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    Entry(frame_buscar, textvariable=id_buscar, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)

    resultado_label = Label(frame_buscar, text="", font=("Arial", 12), bg="#f9fafc", fg="#222f3e")
    resultado_label.grid(row=2, column=0, columnspan=2, pady=10)

    def realizar_busqueda():
        conexion = sqlite3.connect("tarea.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM tarea WHERE id=?", (id_buscar.get(),))
        resultado = cursor.fetchone()
        conexion.close()
        if resultado:
            resultado_label.config(text=f"ID: {resultado[0]}\nNombre: {resultado[1]}\nApellido: {resultado[2]}\nCédula: {resultado[3]}\nGénero: {resultado[4]}\nEstado Civil: {resultado[5]}\nDirección: {resultado[6]}")
        else:
            resultado_label.config(text="No se encontró ningún usuario con ese ID.")

    Button(frame_buscar, text="Buscar", font=("Arial", 12, "bold"), bg="#00b894", fg="white", activebackground="#00cec9", activeforeground="white", command=realizar_busqueda).grid(row=1, column=0, columnspan=2, pady=10)
#creando funcion para validar que solo hayan numeros en la cedula
def validar_cedula(event=None):
    valor = cedula.get()
    if not valor.isdigit() and valor != "" and valor != "Ej: 12345678":
        messagebox.showwarning(
            "Cédula inválida",
            "La cédula solo debe contener números.\nEjemplo de uso: 12345678"
        )
        
        cedula.set(''.join(filter(str.isdigit, valor)))

    cedula_entry.bind("<KeyRelease>", lambda e: validar_cedula())
#creando funcion para validar que solo hayan letras en el nombre y apellido
def validar_nombre_apellido(event=None):
    # Solo letras y espacios permitidos
    valor_nombre = name.get()
    valor_apell = apell.get()
    # Validar nombre
    if valor_nombre and valor_nombre != "Ej: Juan":
        if not all(c.isalpha() or c.isspace() for c in valor_nombre):
            messagebox.showwarning(
                "Nombre inválido",
                "El nombre solo debe contener letras y espacios.\nEjemplo de uso: Juan"
            )
            # Elimina caracteres no válidos
            name.set(''.join(filter(lambda c: c.isalpha() or c.isspace(), valor_nombre)))
    # Validar apellido
    if valor_apell and valor_apell != "Ej: Pérez":
        if not all(c.isalpha() or c.isspace() for c in valor_apell):
            messagebox.showwarning(
                "Apellido inválido",
                "El apellido solo debe contener letras y espacios.\nEjemplo de uso: Pérez"
            )
            apell.set(''.join(filter(lambda c: c.isalpha() or c.isspace(), valor_apell)))

    
frame.columnconfigure(0, weight=0)  
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)
# Definir un placeholder para los campos de entrada
def set_placeholder(entry, placeholder):
    entry.insert(0, placeholder)
    entry.config(foreground="#888")
    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, "end")
            entry.config(foreground="#222")
    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(foreground="#888")
    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)
# Etiquetas y campos de entrada
Label(frame, text="Nombre:", font=("Arial", 13, "bold"), bg="#f9fafc").grid(row=0, column=1, sticky="e", padx=10, pady=10)
name_entry = ttk.Entry(frame, textvariable=name, style="Rounded.TEntry")
name_entry.grid(row=0, column=2, padx=10, pady=10, ipady=5, sticky="ew", columnspan=2)
set_placeholder(name_entry, "Ej: Juan")

Label(frame, text="Apellido:", font=("Arial", 13, "bold"), bg="#f9fafc").grid(row=1, column=1, sticky="e", padx=10, pady=10)
apell_entry = ttk.Entry(frame, textvariable=apell, style="Rounded.TEntry")
apell_entry.grid(row=1, column=2, padx=10, pady=10, ipady=5, sticky="ew", columnspan=2)
set_placeholder(apell_entry, "Ej: Pérez")

Label(frame, text="Cédula de Identidad:", font=("Arial", 13, "bold"), bg="#f9fafc").grid(row=2, column=1, sticky="e", padx=10, pady=10)
cedula_entry = ttk.Entry(frame, textvariable=cedula, style="Rounded.TEntry")
cedula_entry.grid(row=2, column=2, padx=10, pady=10, ipady=5, sticky="ew", columnspan=2)
set_placeholder(cedula_entry, "Ej: 12345678")

Label(frame, text="Género:", font=("Arial", 13, "bold"), bg="#f9fafc").grid(row=3, column=1, sticky="e", padx=10, pady=10)
Radiobutton(frame, text="Masculino", variable=radio_var, value="M", font=("Arial", 12), bg="#f9fafc", activebackground="#f9fafc", fg="#222f3e", selectcolor="#fffbe7").grid(row=3, column=2, sticky="ew", padx=7, pady=10)
Radiobutton(frame, text="Femenino", variable=radio_var, value="F", font=("Arial", 12), bg="#f9fafc", activebackground="#f9fafc", fg="#222f3e", selectcolor="#fffbe7").grid(row=3, column=3, sticky="ew", padx=7, pady=10)


Label(frame, text="Estado Civil:", font=("Arial", 13, "bold"), bg="#f9fafc").grid(row=4, column=1, sticky="e", padx=10, pady=10)
estado_civil_combo = ttk.Combobox(
    frame,
    textvariable=estado_civil,
    state="readonly",
    font=("Arial", 12),
    style="CustomCombobox.TCombobox"
)
estado_civil_combo['values'] = ("Soltero", "Casado", "Viudo", "Divorciado")
estado_civil_combo.grid(row=4, column=2, padx=10, pady=10, ipady=3, sticky="ew", columnspan=2)
estado_civil_combo.set("Soltero")  


# Etiqueta y campo de entrada para Dirección
Label(frame, text="Dirección:", font=("Arial", 13, "bold"), bg="#f9fafc").grid(row=5, column=1, sticky="e", padx=10, pady=10)
direccion_entry = ttk.Entry(frame, textvariable=direccion, style="Rounded.TEntry")
direccion_entry.grid(row=5, column=2, padx=10, pady=10, ipady=5, sticky="ew", columnspan=2)
set_placeholder(direccion_entry, "Ej: Av. Principal #123, Ciudad")

boton_frame = Frame(frame, bg="#f9fafc")
boton_frame.grid(row=6, column=1, columnspan=3, pady=(20, 0), sticky="ew")
boton_frame.columnconfigure((0,1,2,3,4), weight=1)

ttk.Button(boton_frame, text=" Agregar", style="Add.TButton",
           command=lambda: insertar_datos(name.get(), apell.get(), cedula.get(), radio_var.get(), estado_civil.get(), direccion.get())).grid(row=1, column=0, padx=10, sticky="ew")
ttk.Button(boton_frame, text=" Ver Datos", style="View.TButton",
           command=ver_datos).grid(row=1, column=1, padx=10, sticky="ew")
ttk.Button(boton_frame, text=" Actualizar", style="Update.TButton",
           command=lambda: check_db_and_open_window(actualizar_datos)).grid(row=1, column=2, padx=10, sticky="ew")
ttk.Button(boton_frame, text=" Eliminar", style="Delete.TButton",
           command=lambda: check_db_and_open_window(eliminar_datos)).grid(row=1, column=3, padx=10, sticky="ew")
ttk.Button(boton_frame, text=" Buscar Usuario", style="Search.TButton",
           command=lambda: check_db_and_open_window(buscar_usuario)).grid(row=1, column=4, padx=10, sticky="ew")


# Footer al final del root
footer = Label(root, text="David Lovera CI: 25.531.572", font=("Arial", 10, "italic"), bg="#e3eaf2", fg="#636e72")
footer.pack(side="bottom", pady=8)


# Asocia la validación a los campos de nombre y apellido
name_entry.bind("<KeyRelease>", lambda e: validar_nombre_apellido())
apell_entry.bind("<KeyRelease>", lambda e: validar_nombre_apellido())

root.mainloop()