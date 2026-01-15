# marcar tareas

def marcar_tarea (tareas):
    id_marcar = int(input("ingrese el ID de la tarea a marcar como completada: "))
    for tarea in tareas:
        if tarea["id"] == id_marcar:
            tarea["estado"] = "completada"
            print(f"Tarea con ID {id_marcar} ha sido marcada como completada.")
            return
    else:
        print(f"No se encontró ninguna tarea con ID {id_marcar}")
# si no existe ninguna tarea con su ID correspondiente.
# fin marcar tarea.