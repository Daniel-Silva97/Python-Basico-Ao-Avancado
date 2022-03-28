import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions/tagged/python?sort=Newest&edited=true'
response = requests.get(url)  # Pegando o retorno do link acima
html = BeautifulSoup(response.text, 'html.parser')  # Criando um objeto com o HTML do resultado acima
# print(html)

# Fui no chrome e peguei o nome da classe pelo 'Inspecionar' para o bloco da pergunta
for pergunta in html.select('.s-post-summary'):
    # Aqui peguei a classe que contém os títulos da pergunta
    titulo = pergunta.select_one('.s-link')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.s-post-summary--stats-item-number')
    print(titulo.text, data.text, votos.text, sep='\t')

