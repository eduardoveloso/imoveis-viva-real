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
df = pd.DataFrame(
    columns=[
        'descricao',
        'endereco',
        'area',
        'quartos',
        'wc',
        'vagas',
        'valor',
        'condominio',
        'wlink'
    ]
)
i = 0

# %%
ret = requests.get(url.format(estado, cidade, i))
soup = bs(ret.text)
houses =  soup.find_all('a', {'class': 'property-card__content-link js-card-title'})
qty_houses = int(soup.find('strong', {'class': 'results-summary__count'}).text.replace('.', ''))
pages = ceil(qty_houses / len(houses))

while qty_houses <= pages:
    i += 1
    print(f"valor i: {i} \t\t qtd_imoveis: {df.shape[0]}")
    
    for house in houses:
        try:
            descricao = house.find('span', {'class': 'property-card__title'}).text.strip()
        except:
            descricao = None
        try:
            endereco = house.find('span', {'class': 'property-card__address'}).text.strip()
        except:
            endereco = None
        try:
            area = house.find('span', {'class': 'js-property-card-detail-area'}).text.strip()
        except:
            area = None
        try:
            quartos = house.find('li', {'class': 'property-card__detail-room'}).span.text.strip()
        except:
            quartos = None
        try:
            wc = house.find('li', {'class': 'property-card__detail-bathroom'}).span.text.strip()
        except:
            wc = None
        try:
            vagas = house.find('li', {'class': 'property-card__detail-garage'}).span.text.strip()
        except:
            vagas = None
        try:
            valor = house.find('div', {'class': 'property-card__price'}).p.text.strip()
        except:
            valor = None
        try:
            condominio = house.find('strong', {'class': 'js-condo-price'}).text.strip()
        except:
            condominio = None
        try:
            wlink = 'https://www.vivareal.com.br' + house['href']
        except:
            wlink = None

        df.loc[df.shape[0]] = [
            descricao,
            endereco,
            area,
            quartos,
            wc,
            vagas,
            valor,
            condominio,
            wlink
        ]

# %%
df

# %%
df.to_csv('banco_de_imoveis.csv', sep=';', index=False)
# %%
