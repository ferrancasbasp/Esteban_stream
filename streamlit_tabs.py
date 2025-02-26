import streamlit as st

# Crear pestañas
tab1, tab2 = st.tabs(["Pestaña 1", "Pestaña 2"])

with tab1:
    st.header("Contenido de la Pestaña 1")
    st.write("Este es el contenido de la primera pestaña.")

with tab2:
    st.header("Contenido de la Pestaña 2")
    st.write("Este es el contenido de la segunda pestaña.")
