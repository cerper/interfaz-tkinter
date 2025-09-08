Este programa implementa una interfaz gráfica en Python usando Tkinter y ttk para la gestión de usuarios. Permite agregar, ver, actualizar, eliminar y buscar usuarios en una base de datos SQLite. Los datos incluyen nombre, apellido, cédula de identidad, género, estado civil y dirección.
Funcionalidades

1. Agregar Datos
   Valida que todos los campos estén completos.
   Resalta en rojo los campos faltantes.
   Muestra una alerta indicando qué campos faltan.
   Inserta los datos en la base de datos.
   Limpia todos los campos tras agregar.
2. Ver Datos
   Muestra todos los registros en una ventana nueva.
   Si no hay datos, muestra un mensaje invitando a registrarse.
3. Actualizar Datos
   Abre una ventana para actualizar un registro por ID.
   Si no hay datos, muestra una alerta.
   Valida que todos los campos estén completos antes de actualizar.
4. Eliminar Datos
   Abre una ventana para eliminar un registro por ID.
   Si no hay datos, muestra una alerta.
   Valida el ID antes de eliminar.
5. Buscar Usuario
   Abre una ventana para buscar un usuario por ID.
   Si no hay datos, muestra una alerta.
   Muestra los datos del usuario si existe.
