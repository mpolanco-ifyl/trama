import streamlit as st
import openai
import random

# Pide la clave de API de OpenAI al usuario
openai.api_key = st.text_input("Introduce tu clave de API de OpenAI:")

# Lista de autores españoles
autores_espanoles = ["Javier Marías", "Carlos Ruiz Zafón", "Arturo Pérez-Reverte", "Almudena Grandes", "Juan José Millás", "María Dueñas", "Javier Cercas", "Rosa Montero", "Eduardo Mendoza", "Luis Landero"]

# Se define la función para generar la trama de un cuento
def generar_trama(tema, autor):
    # Se establecen los parámetros para la generación del texto
    prompt = (f"Escribe una trama de cuento sobre el tema {tema}, imitando el estilo de escritura de {autor}.")
    temperatura = random.uniform(0.7, 1.2)  # Ajuste de temperatura
    max_tokens = 2048  # Ajuste de max_tokens

    # Se genera el texto con el modelo GPT-3 de OpenAI
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        temperature=temperatura
    )

    # Se devuelve la trama generada
    return completions.choices[0].text

# Se define la app de Streamlit
def main():
    # Título de la app
    st.title("Generador de tramas de cuentos con OpenAI")

    # Descripción de la app
    st.write("Esta aplicación genera una trama de cuento a partir de un tema dado, imitando el estilo de escritura de un autor español seleccionado por el usuario.")

    # Input del tema
    tema = st.text_input("Introduce el tema de la trama:")

    # Input del autor
    autor = st.selectbox("Selecciona el autor a imitar:", autores_espanoles)

    # Se genera la trama
    if st.button("Generar trama"):
        trama = generar_trama(tema, autor)
        st.write("Aquí está tu trama:")
        st.write(trama)

# Se ejecuta la app
if __name__ == "__main__":
    main()
