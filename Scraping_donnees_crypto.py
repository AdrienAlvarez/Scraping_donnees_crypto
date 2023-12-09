import requests
import pandas as pd

# CoinGecko API URL pour obtenir des détails sur toutes les crypto-monnaies
api_url = "https://api.coingecko.com/api/v3/coins/markets"

# Paramètres pour la requête API
params = {
    'vs_currency': 'usd',  # Comparaison avec la monnaie USD
    'order': 'market_cap_desc',  # Trier par capitalisation boursière, ordre décroissant
    'per_page': 250,  # Nombre de résultats par page
    'page': 1,  # Numéro de la page (peut être ajusté pour obtenir plus de résultats)
    'price_change_percentage': '1h,24h,7d,14d,30d,200d,1y'  # Pourcentage de changement de prix pour différentes périodes
}

# Effectuer la requête à l'API
response = requests.get(api_url, params=params)

# Vérifier si la réponse est réussie
if response.status_code == 200:
    # Extraire les données JSON
    all_coins_data = response.json()

    # Création d'une liste pour stocker les données de toutes les crypto-monnaies
    all_coins_info = []

    # Parcourir les données de chaque crypto-monnaie et extraire les informations pertinentes
    for coin in all_coins_data:
        coin_info = {
            'Name': coin['name'],
            'Market Cap (USD)': coin['market_cap'],
            'Market Cap Rank': coin['market_cap_rank'],
            'Fully Diluted Valuation': coin['fully_diluted_valuation'],
            'Total Volume (24h)': coin['total_volume'],
            'High (24h)': coin['high_24h'],
            'Low (24h)': coin['low_24h'],
            '1h Price Change Percentage': coin['price_change_percentage_1h_in_currency'],
            '24h Price Change Percentage': coin['price_change_percentage_24h'],
            '7d Price Change Percentage': coin['price_change_percentage_7d_in_currency'],
            '14d Price Change Percentage': coin['price_change_percentage_14d_in_currency'],
            '30d Price Change Percentage': coin['price_change_percentage_30d_in_currency'],
            '200d Price Change Percentage': coin['price_change_percentage_200d_in_currency'],
            '1y Price Change Percentage': coin['price_change_percentage_1y_in_currency'],
            'Circulating Supply': coin['circulating_supply'],
            'Total Supply': coin.get('total_supply', 'N/A'),
            'Max Supply': coin.get('max_supply', 'N/A'),
            'Market Cap Change (24h)': coin['market_cap_change_24h'],
            'Market Cap Change Percentage (24h)': coin['market_cap_change_percentage_24h'],
            'All-Time High (ATH)': coin['ath'],
            'ATH Change Percentage': coin['ath_change_percentage'],
            'ATH Date': int(''.join(filter(str.isdigit, coin['ath_date']))),
            'All-Time Low (ATL)': coin['atl'],
            'ATL Change Percentage': coin['atl_change_percentage'],
            'ATL Date': int(''.join(filter(str.isdigit, coin['atl_date']))),
            'ROI': 0 if pd.isna(coin['roi']) else 1,
        }
        all_coins_info.append(coin_info)

    # Convertir la liste en DataFrame
    df = pd.DataFrame(all_coins_info)