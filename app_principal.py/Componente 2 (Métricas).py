def calcular_kpis_fraude(df):
    volumen_total_procesado = df["Volumen_total"].sum()
    cantidad_de_transacciones_evaluadas = df["Cantidad_de_transacciones"].sum()

    if cantidad_de_transacciones_evaluadas > 0:
        ticket_promedio = (volumen_total_procesado / cantidad_de_transacciones_evaluadas)
    else:
        ticket_promedio = 0

    return {
        "Volumen_total": volumen_total_procesado,
        "Ticket_promedio": ticket_promedio,
        "Cantidad_de_transacciones": cantidad_de_transacciones_evaluadas
    }
