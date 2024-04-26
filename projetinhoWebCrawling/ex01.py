import requests 
import re

url = 'https://metodoaplicado.com.br/conhecimentos-especificos-concurso-nacional-unificado-2024-bloco-5-questoes-comentadas/'
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