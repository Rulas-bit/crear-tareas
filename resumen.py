# resumir datos de tareas

def resumir_tareas(tareas):
    if not tareas:
        print("No hay tareas para resumir.")
        return
    print("Resumen de tareas:")
    for tarea in tareas:
        print(f"- {tarea['titulo']} - Estado: {tarea['estado']}") # muestra titulo y estado de cada tarea.
# fin resumen de tareas