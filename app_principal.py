import streamlit_authenticator as stauth
import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
from flota_poo import cargar_flota, instanciar_flota
from mapa import crear_mapa
credentials = {
    "usernames":{
        "admin":{
            "name": "administrador",
            "password": "12345"
        }, 
        "usuario1":{
            "name": "operativo",
            "password": "contraseña"
        },
        "iker(ceo)":{
            "name": "Ceo de la empresa",
            "password": "12345"
        }
    }
}
#inicalizamos el componente de autenticacion de github pasando las credenciales de los usuarios
authenticator = stauth.Authenticate(
    credentials= credentials,
    cookie_name="dashboard_cookie",
    key= "signature_key",
    cookie_expiry_days=30
)
#El componente se encarga de reenderizar el formulario en pantalla
authenticator.login(
    location='main',
    fields={'Form name': 'Formulario de Acceso'}
)

#CONTROL DE FLUJO MEDIANTE EL ESTADO INTERNO DE LA MEMORIA(sesion state)
if st.session_state.get("authentication_status") == False:
    st.error("Usuario o contraseña incorrecta")
elif st.session_state.get("authentication_status") is None:
    st.warning('Por favor, ingresa tu usuario y contraseña')
elif st.session_state.get("authentication_status"):
    #si el usuario se auntetica con existo, se muestra el resto de la app
    #extraemos el resto del usuario
    name_usuario = st.session_state["name"]

    st.title(f"dashboard corporativo de {name_usuario}")
    #Boton de cerrar sesion en un sidebar
    authenticator.logout(button_name='cerrar sesion', location='sidebar')

    df = cargar_flota()

    # Crear las instancias de los vehículos
    flota = instanciar_flota()
    st.header("Flota de vehículos")
    st.dataframe(df)

    # Componente del mapa
    crear_mapa(df, flota)