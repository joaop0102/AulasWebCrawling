import requests

def pegar_cotacao_moeda(moeda_origem, moeda_destino):
    moeda_origem = "USD"
    moeda_destino = "EUR"
    link = f'https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}'
    requisicao = requests.get(link)

    cotacao = requisicao.json()[f"{moeda_origem}{moeda_destino}"]["bid"]
    return cotacao