import requests 
import re

url = 'https://www.terra.com.br/noticias/brasil/cidades/tentativa-de-assalto-termina-em-tiroteio-na-regiao-da-faria-lima-em-sp-suspeito-e-preso,538127ea1c356f5265ab60a6b9f351337opnqwnt.html'
check = []

r = requests.get(url)
html = r.text
search = re.findall(r'<a href=[\'"?](https[://\w\-._]+)', html)

for link in search:
    if link not in check:
        check.append(link)
        print(link)
        with open("link.txt", "+a") as file:
            file.write(f'{link}\n')