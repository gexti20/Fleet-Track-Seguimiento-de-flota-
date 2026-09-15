import streamlit as st
import pandas as pd

from componente_datos import cargar_y_validar_transacciones
from componente_metrica import calcular_kpis_fraude
from componente_prediccion import detectar_anomalias

# Configuración inicial del tablero
st.set_page_config(
    page_title="Detección de Fraude Streaming",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Detección de Fraude Streaming")
st.subheader("Sistema en Tiempo Real de Detección de Anomalías en Transacciones")
st.write(
    "Visualizar en tiempo real el fraude con tarjeta de crédito clonadas, "
    "la tarjeta crítica y la predicción de riesgo operativo y congelar previamente las operaciones sospechosas."
)

# Control de estado de la sesión
if "transacciones" not in st.session_state:
    st.session_state.transacciones = pd.DataFrame()

# Menú lateral
st.sidebar.title("Menú")
st.sidebar.markdown("---")

archivo = st.sidebar.file_uploader(
    "📁 Selecciona un archivo CSV",
    type=["csv"]
)

st.sidebar.markdown("---")
st.sidebar.info("Sube un archivo CSV para visualizar los datos de transacciones.")

# Componente 1: Ingesta de Datos
if archivo:
    try:
        st.session_state.transacciones = cargar_y_validar_transacciones(archivo)
        st.sidebar.success("✅ Componente de Datos: ingesta y validación exitosas.")
    except Exception as e:
        st.sidebar.error(f"❌ Falló en la interfaz de datos: {e}")

df = st.session_state.transacciones

# Flujo Visual principal
if not df.empty:
    st.markdown("---")
    st.markdown("### 🔍 Filtro por transacción")

    transaccion_disponibles = ["Todas"] + sorted(df["id_transaccion"].unique().tolist())
    transaccion_seleccionada = st.selectbox("Selecciona una transacción:", transaccion_disponibles)

    if transaccion_seleccionada == "Todas":
        df_filtrado = df
    else:
        df_filtrado = df[df["id_transaccion"] == transaccion_seleccionada]

    # Componente 2: Métricas
    st.markdown("---")
    st.markdown("### 📊 Métricas Principales")
    
    kpis = calcular_kpis_fraude(df_filtrado)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Volumen Total Procesado", f"€{kpis['Volumen_total']:,.2f}")
    col2.metric("Ticket Promedio", f"€{kpis['Ticket_promedio']:,.2f}")
    col3.metric("Transacciones Evaluadas", f"{kpis['Cantidad_de_transacciones']:,}")

    # Componente 3: Detección de anomalías
    st.markdown("---")
    st.markdown("### 🚨 Transacciones Sospechosas Detectadas")

    df_anomalias = detectar_anomalias(df_filtrado)

    if not df_anomalias.empty:
        st.warning(f"⚠️ **Alerta de Fraude**: Se han detectado **{len(df_anomalias)}** operaciones sospechosas.")
        st.dataframe(df_anomalias, use_container_width=True)
    else:
        st.success("✅ **Estado Óptimo**: No se encontraron anomalías en los datos evaluados.")

    # Gráfico de Tendencia
    st.markdown("---")
    st.markdown("### 📈 Tendencia del Monto en el Tiempo")

    if "timestamp" in df_filtrado.columns and "monto_eur" in df_filtrado.columns:
        st.line_chart(df_filtrado.set_index("timestamp")["monto_eur"])
    else:
        st.info("Asegúrate de que el CSV contenga las columnas 'timestamp' y 'monto_eur' para visualizar la gráfica.")


        