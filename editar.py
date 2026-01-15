# editar tareas 
def editar_tarea (tareas) :
    id_editar = int(input("ingrese el ID de la tarea a editar: "))
    for tarea in tareas:
        if tarea["id"] == id_editar: # encontrar tarea por ID
            nuevo_titulo = input("ingrese el nuevo título de la tarea: ")
            tarea["titulo"] = nuevo_titulo
            print(f"Tarea con ID {id_editar} ha sido actualizada.")
            return
        # si no existe nunguna tarea con su ID correspondiente.
        else :
           print(f"No se encontró ninguna tarea con ID {id_editar}")