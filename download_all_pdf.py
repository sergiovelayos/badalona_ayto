# Source: https://www.youtube.com/watch?v=ng2o98k983k
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import re 


# Definir la URL de la página web
url = "http://badalona.cat/portalWeb/badalona.portal;jsessionid=4ylNk92VwLgsvf93SfNv9nqJT9Dvpf0kDG4gvCvXzCq27qT01h6n!-862168623?_nfpb=true&_pageLabel=contingut_estatic&dCollectionID=4820#wlp_contingut_estatic"

# make HTTP GET request to the target URL
response = requests.get(url)

# parse content
soup = BeautifulSoup(response.text, 'lxml')


# Creo una lista donde añadiré cada url de PDF a descargar
lista_pdf_urls = []

# Loop que busca las urls de pdfs a descargar
for noticia in soup.find_all('li', class_='noticia relacionat'):
    pdf_src = noticia.find('a')['href']
    pdf_urls = f'http://badalona.cat{pdf_src}'
    lista_pdf_urls.append(pdf_urls)

# Define the pattern to match
pattern = "dDocName=(\w+)"

# Loop through the list
for i in lista_pdf_urls:
    # Get the response from the URL
    response = requests.get(i)
    # Search for the pattern in the URL
    match = re.search(pattern, i)
    # If there is a match, get the file name from the group 1
    if match:
      file_name = match.group(1)
      # Open a file with the same name as write mode
      with open(file_name, "wb") as file:
        # Write the response content to the file
        file.write(response.content)
    

    