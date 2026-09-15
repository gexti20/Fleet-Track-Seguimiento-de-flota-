import folium
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from streamlit_folium import st_folium

# Título y subtítulo
st.title("🚚 Panel de despacho - Fleet Track")
st.subheader("Flota de reparto - Vitoria-Gasteiz")



df = pd.DataFrame

st.divider()

# Tabla de vehículos
st.subheader("🚚 Flota de vehículos")
AgGrid(df)

# Creamos el mapa
mapa = folium.Map(
    location=[42.8467, -2.6716],
    zoom_start=13
)

for _, vehiculo in df.iterrows():

    # Creamos un marcador para cada vehículo
    folium.Marker(
        location=[
            vehiculo["latitud"],
            vehiculo["longitud"]
        ],
        popup=vehiculo["ID"],
        tooltip=vehiculo["Vehiculo"],
        icon=folium.Icon(
            color="red",
            icon="info-sign"
        )
    ).add_to(mapa)

# Mostramos el mapa
info_map = st_folium(
    mapa,
    width=700,
    height=400
)

st.divider()

if info_map and info_map.get("last_object_clicked_popup"):

    if info_map and info_map.get("last_object_clicked_popup"):

    # Guardamos el ID del vehículo seleccionado
     id_vehiculo = info_map["last_object_clicked_popup"]

    for _, vehiculo in df.iterrows():

        if vehiculo["ID"] == id_vehiculo:

            # Mostramos el vehículo y su estado
            st.success(
                f"Has seleccionado correctamente {vehiculo['Vehiculo']} - "
                f"Estado: {vehiculo['Estado']}"
            )