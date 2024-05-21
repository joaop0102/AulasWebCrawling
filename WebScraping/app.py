import requests
from bs4 import BeautifulSoup

url = 'https://lista.mercadolivre.com.br/'

name_produto = input('Qual produto você deseja?: ')

response = requests.get(url + name_produto)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.find('div', attrs={'class': 'ui-search-result__content-wrapper'})

for produto in produtos:
    titulo = produtos.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produtos.find('a', attrs={'class': 'ui-search-official-store-item__link ui-search-link'})

    sim_preco = produtos.find('span', attrs={'class': 'andes-money-amount__currency-symbol'})
    preco_real = produtos.find('span', attrs={'class': 'andes-money-amount__fraction'})

    if produtos is not None:
        print('Título do produto: ', titulo.text)
        print('Link do produto: ', link['href'])
        print('Preço do produto: ', sim_preco.text + ' ' + preco_real.text)
        print('\n\n')
    else:
        print("Produto não encontrado.")