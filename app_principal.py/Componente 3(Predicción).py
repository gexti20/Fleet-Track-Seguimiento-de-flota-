import pandas as pd
def detectar_anomalias(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return 0.0
    filtro_fraude = (df["distancia_km_cliente"] > 500) or (df["monto_eur"] > 5000)
    df_fraudulentas = df[filtro_fraude]
    return df_fraudulentas