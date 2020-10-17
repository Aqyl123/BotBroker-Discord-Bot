# 351io RECENT SALES
import cloudscraper
import pandas as pd
from pandas import DataFrame

scraper = cloudscraper.create_scraper()

# RENEWAL
threefiveoneR_url = 'https://botbroker.io/bots/16/chart?key_type=renewal&days=365'
response = scraper.get(threefiveoneR_url)
response.raise_for_status()

try:
	result = response.json()
	df2 = DataFrame(result).sort_values(by=[0], ascending=False).reset_index(drop=True)
except (IndexError, KeyError):
	result = None

threefiveoneR = 'No recent sales' if not result else f'${df2[1][0]}'