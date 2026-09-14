import folium
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
from streamlit_folium import st_folium

# Título y subtítulo
st.title("🚚 Panel de despacho - Fleet Track")
st.subheader("Flota de reparto - Vitoria-Gasteiz")

# Datos de la flota
data = [
    {
        "ID": "A1007",
        "Vehiculo": "Mercedes Vito Tourer 2016",
        "Kilometros": "11,000",
        "Estado": "Operativo",
        "latitud": 42.8550,
        "longitud": -2.6750,
    },
    {
        "ID": "A1009",
        "Vehiculo": "Audi A6",
        "Kilometros": "20,000",
        "Estado": "Operativo",
        "latitud": 42.8467,
        "longitud": -2.6716,
    },
    {
        "ID": "V003",
        "Vehiculo": "BMW X4 2024",
        "Kilometros": "108,000",
        "Estado": "Próximo mantenimiento",
        "latitud": 42.8380,
        "longitud": -2.6750,
    }
]

df = pd.DataFrame(data)

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

    # Guardamos el ID del vehículo seleccionado
    id_vehiculo = info_map["last_object_clicked_popup"]

    
    for _, vehiculo in df.iterrows():

        if vehiculo["ID"] == id_vehiculo:

            # Mostramos el vehículo y su estado
            st.success(
                f"Has seleccionado correctamente {vehiculo['Vehiculo']} - "
                f"Estado: {vehiculo['Estado']}"
            )