
import folium
import streamlit as st
from streamlit_folium import st_folium

from flota_poo import cargar_flota, instanciar_flota


def crear_mapa(df, flota):

    mapa = folium.Map(
        location=[42.8467, -2.6716],
        zoom_start=13
    )

    for nombre, vehiculo in df.items():

        folium.Marker(
            location=[
                vehiculo["latitud"],
                vehiculo["longitud"]
            ],
            popup=vehiculo["matricula"],
            tooltip=vehiculo["modelo"],
            icon=folium.Icon(
                color="red",
                icon="info-sign"
            )
        ).add_to(mapa)

    info_map = st_folium(
        mapa,
        width=700,
        height=400
    )

    if info_map and info_map.get("last_object_clicked_popup"):

        matricula = info_map["last_object_clicked_popup"]

        for vehiculo in flota:

            if vehiculo.matricula == matricula:

                st.subheader(f"🚚 {vehiculo.modelo}")

               
                vehiculo.requiere_mantenimiento()

df = cargar_flota()
flota = instanciar_flota()