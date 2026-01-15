# borrar tarea.

def borrar_tareas(tareas):
    id_borrar = int(input("ingrese el ID de la tarea a borrar: "))
    for tarea in tareas:
        if tarea["id"] == id_borrar:
            tareas.remove(tarea)
            print(f"Tarea con ID {id_borrar} ha sido borrada.")
# si no existe nunguna tarea con su ID correspondiente.
        else :
           print(f"No se encontró ninguna tarea con ID{id_borrar}")
           return
