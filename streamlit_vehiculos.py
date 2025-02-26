import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Título de la aplicación
st.title("Visualización de Costes por Tipo de Vehículo")

# Definir opciones
vehicles = ["Camión", "Tren", "Tráiler", "Remolque"]
vehicle_defaults = {
    "Camión": (1000, 2.0),
    "Tren": (2000, 3.5),
    "Tráiler": (1500, 2.5),
    "Remolque": (2500, 1.5)
}

selected_vehicle = st.radio("Selecciona un vehículo:", vehicles)

def_peso, def_longitud = vehicle_defaults[selected_vehicle]

tab1, tab2 = st.tabs(["Gráfica Estática", "Gráfica Dinámica"])


with tab1:
    # Crear columnas para organizar los inputs
    col1, col2 = st.columns([2, 1])

    with col2:
        peso = st.number_input("Peso (kg):", min_value=500, max_value=5000, value=def_peso, step=100)
        longitud = st.number_input("Longitud (m):", min_value=1.0, max_value=10.0, value=def_longitud, step=0.1)
        st.write(f"**Peso seleccionado:** {peso} kg")
        st.write(f"**Longitud seleccionada:** {longitud} m")

    # Generar datos para la curva y = x^2
    x = np.arange(0, 10, 0.1)
    y = np.cos(x)
    z = np.cos(x*def_longitud)
    fig = plt.figure(figsize=(12, 6))

    ax = fig.add_subplot(121)

    ax.set_title(f"Curva de Coste para {selected_vehicle}")
    ax.plot(y, color='blue', label='Sine wave')
    ax.plot(z, color='black', label='Cosine wave')

    # ax.set_xlim([25, 50])

    ax.set_xlabel("Tiempo o Consumo")
    ax.set_ylabel("Coste")

    # Mostrar el gráfico en Streamlit
    with col1:
        st.pyplot(fig)

with tab2:
    # Datos de la tabla de coste
    tiempo = list(range(1, 11))
    coste = [22, 23, 26, 35, 47, 55, 60, 65, 70, 75]  # Aseguramos 10 valores

    # Controles para la gráfica dinámica
    st.subheader("Gráfica Dinámica de Coste en el Tiempo")
    start_button = st.button("Iniciar")
    stop_button = st.button("Parar")
    reset_button = st.button("Reiniciar")

    if "running" not in st.session_state:
        st.session_state.running = False
    if "index" not in st.session_state:
        st.session_state.index = 0

    if start_button:
        st.session_state.running = True
    if stop_button:
        st.session_state.running = False
    if reset_button:
        st.session_state.running = False
        st.session_state.index = 0

    # Gráfica dinámica con actualización en tiempo real
    time_chart = st.empty()

    def update_chart():
        fig, ax = plt.subplots()
        ax.plot(tiempo[:st.session_state.index + 1], coste[:st.session_state.index + 1], 'bo-', label="Coste")
        ax.set_title("Evolución del Coste en el Tiempo")
        ax.set_xlabel("Tiempo")
        ax.set_ylabel("Coste")
        ax.set_xlim(0, 10)  # Mantener el eje X fijo de 0 a 10
        ax.set_ylim(min(coste) - 5, max(coste) + 5)
        ax.set_xticks(range(0, 11))
        ax.legend()
        time_chart.pyplot(fig)

    while st.session_state.running and st.session_state.index < len(tiempo):
        update_chart()
        st.session_state.index += 1
        time.sleep(1)
