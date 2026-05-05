import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Télécharger les données
data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

# Calcul du rendement
data['Return'] = data['Close'].pct_change()

# Moyennes mobiles
data['MA50'] = data['Close'].rolling(50).mean()
data['MA200'] = data['Close'].rolling(200).mean()

# Statistiques simples
print("Rendement moyen :", data['Return'].mean())
print("Volatilité :", data['Return'].std())

# Graphique
plt.figure(figsize=(10,5))
plt.plot(data['Close'], label="Prix")
plt.plot(data['MA50'], label="MA50")
plt.plot(data['MA200'], label="MA200")
plt.legend()
plt.title("Analyse AAPL")
plt.show()
