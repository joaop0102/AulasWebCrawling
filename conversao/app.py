link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

import requests

req =  requests.get(link)

print(req.json())