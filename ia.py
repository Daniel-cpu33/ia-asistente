def iniciar():
    print("Hola, soy tu asistente IA")
    print("Escribe algo y te responderé (escribe 'salir' para terminar)\n")

def procesar(mensaje):
    mensaje = mensaje.lower()

    if "hola" in mensaje:
        return "Hola, ¿cómo estás?"
    elif "tarea" in mensaje:
        return "Organiza tus tareas por prioridad y empieza por lo más difícil."
    elif "estres" in mensaje:
        return "Respira profundo, toma un descanso y luego continúa."
    elif "ia" in mensaje:
        return "La inteligencia artificial simula el pensamiento humano usando datos y reglas."
    elif "ayuda" in mensaje:
        return "Puedes preguntarme sobre tareas, estrés o qué es la IA."
    elif "gracias" in mensaje:
        return "De nada, estoy para ayudarte."
    else:
        return "No entiendo eso todavía, pero estoy aprendiendo."

def recomendaciones():
    print("\nRecomendaciones:")
    print("- Estudia al menos 30 minutos diarios")
    print("- Toma descansos cortos")
    print("- Practica programación constantemente\n")

# PROGRAMA PRINCIPAL
iniciar()

while True:
    entrada = input("Tú: ")

    if entrada.lower() == "salir":
        print("Adiós, fue un gusto ayudarte")
        break

    respuesta = procesar(entrada)
    print("IA:", respuesta)

    if "recomienda" in entrada.lower():
        recomendaciones()
