# guardar tareas.

def guadar_tarea (tareas, nombre_archivo):
    import json
    with open (nombre_archivo, "w") as archivo: # abre el archivo en modo escritura.
        json.dump(tareas, archivo) # guarda la lista de tareas en formato JSON.
    print(f"tareas guardadas en {nombre_archivo}")
# fin guardar tareas.