# %%
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from math import ceil

# %%
estado = 'sp'
cidade = 'Sao Paulo'
cidade = cidade.replace(' ', '-').lower()

url = 'https://www.vivareal.com.br/venda/{}/{}/apartamento_residencial/?pagina={}'

# %%
i = 1
ret = requests.get(url.format(estado, cidade, i))
soup = bs(ret.text)
#soup

# %%
houses =  soup.find_all('a', {'class': 'property-card__content-link js-card-title'})
qty_houses = float(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.', ''))
pages = ceil(qty_houses / len(houses))

#len(houses)
#qty_houses
pages

# %%
