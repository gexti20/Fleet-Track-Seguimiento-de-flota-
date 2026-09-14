import pandas as pd
import streamlit as st
class Vehiculo:
    def __init__(self, cuentaquilometros , matricula, modelo):
        self.cuentaquilometros = cuentaquilometros 
        self.matricula = matricula
        self.modelo = modelo
        def requiere_mantenimiento(self):
            if self.cuentaquilometros < 0:
                st.warning("No se aceptan valores por debajo de 0")
            pass
class Furgoneta(Vehiculo):
    
    def requiere_mantenimiento(self):
        return print("Los kilometros no son los requeridos") if self.cuentaquilometros > 15000 else print("Todo perfecto")

class VehiculoElectrico(Vehiculo):
   
    def requiere_mantenimiento(self):
        return print("Los kilometros no son los requeridos ") if self.cuentaquilometros > 5000 else print("Todo correcto")

def cargar_flota():
    data = {
        "Vehiculo": {
            "cuentaquilometros": 10000,
            "matricula": "1234ABC",
            "modelo": "Toyota",
            "latitud": 42.8550,
            "longitud": -2.6750
            },
        "Furgoneta": {
            "cuentaquilometros": 12000,
            "matricula": "5678DEF",
            "modelo": "Ford Transit",
            "latitud": 42.8467,
            "longitud": -2.6716
            },
        "VehiculoElectrico": {
            "cuentaquilometros": 4000,
            "matricula": "9012GHI",
            "modelo": "Tesla",
            "latitud": 42.8380,
            "longitud": -2.6750
            }
        }

    df = pd.DataFrame(data)
    return df
def instanciar_flota():
    return [Vehiculo(10000, "1234ABC", "Toyota", 42.8550, -2.6750),
            Furgoneta(12000, "5678DEF", "For Transit", 42.8467, -2.6716),
            VehiculoElectrico(4000, "9012GHI", "Tesla", 42.8380, -2.6750)]

