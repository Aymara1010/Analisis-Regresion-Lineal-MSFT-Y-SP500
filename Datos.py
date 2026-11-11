import yfinance as yf
import pandas as pd
import numpy as np

# Definir tickers de Yahoo Finance y tiempo
activos = ["MSFT", "^GSPC"]
fecha_inicio = "2021-01-01"
fecha_fin = "2026-01-01" 

# Descargar los datos
datos_precios = yf.download(activos, start=fecha_inicio, end=fecha_fin)['Close']

# Depuración 
df = datos_precios.dropna()
df = df.reset_index()

# Cálculo de Rendimiento
df['R_MSFT'] = np.log(df['MSFT'] / df['MSFT'].shift(1))
df['R_SP500'] = np.log(df['^GSPC'] / df['^GSPC'].shift(1))
df["Date"] = pd.to_datetime(df["Date"]).dt.strftime('%d-%m-%Y')

df = df.dropna()

# Renombrando Variables
df.rename(columns={
    'Date': 'Fecha',
    '^GSPC': 'Precio_SP500',
    'MSFT': 'Precio_MSFT',
    'R_MSFT': 'Rendimiento_MSFT',
    'R_SP500': 'Rendimiento_SP500'
}, inplace=True)

df.to_csv("precios.csv")