import pandas as pd
import streamlit as st

# Configuración de la interfaz del agente
st.set_page_config(page_title="Agente Corporativo AI", page_icon="🤖")
st.title("🤖 Agente Corporativo de IA - Consulta de Documentos")
st.write("Bienvenido. Consulta información sobre las políticas de la empresa en tiempo real.")

# 1. Carga de la base de conocimiento (CSV / Documentos)
@st.cache_data
def cargar_datos():
    url = "https://raw.githubusercontent.com/Jebareiro/agente-corporativo-ch-alura/main/politicas_tienda.csv"
    df = pd.read_csv(url, sep=';')
    df.columns = ['pregunta', 'respuesta']
    return df

try:
    df = cargar_datos()
    st.success("✅ Base de datos cargada correctamente desde el repositorio.")
except Exception as e:
    st.error(f"❌ Error al cargar los documentos corporativos: {e}")

# 2. Capa de Recuperación RAG (Búsqueda semántica)
def agente_corporativo(pregunta_usuario):
    pregunta = pregunta_usuario.lower().strip()

    # Búsqueda de coincidencia contextual en la base de datos
    for index, row in df.iterrows():
        pregunta_base = str(row['pregunta']).lower()
        if any(palabra in pregunta_base for palabra in pregunta.split() if len(palabra) > 3):
            return row['respuesta'], "politicas_tienda.csv"

    return None, None

# 3. Interacción con el usuario (Chat Corporativo)
pregunta_usuario = st.text_input("Haz tu pregunta sobre los documentos corporativos:")

if pregunta_usuario:
    respuesta, fuente = agente_corporativo(pregunta_usuario)

    if respuesta:
        st.markdown(f"**🤖 Agente:** {respuesta}")
        st.info(f"📌 **Fuente citada:** {fuente}")
    else:
        st.warning("🤖 **Agente:** Lo siento, no encontré esa información en los documentos corporativos disponibles. Por favor, consulta con el área correspondiente.")