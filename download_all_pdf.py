# Source: https://www.youtube.com/watch?v=ng2o98k983k
import requests
from bs4 import BeautifulSoup
import urllib.request
import os
import re 


# Definir la URL de la página web
url = "http://badalona.cat/portalWeb/badalona.portal?_nfpb=true&_pageLabel=contingut_estatic&dCollectionID=5176"

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

# Create a folder named pdfs if it does not exist
if not os.path.exists("pdfs/2023"):
  os.mkdir("pdfs/2023")

# Loop through the list
for i in lista_pdf_urls:
    # Get the response from the URL
    response = requests.get(i)
    # Search for the pattern in the URL
    match = re.search(pattern, i)
    # If there is a match, get the file name from the group 1 and add .pdf
    if match:
      file_name = match.group(1) + ".pdf"
      # Join the folder name and the file name
      file_path = os.path.join("pdfs","2022", file_name)
      # Open a file with the same name as write mode
      with open(file_path, "wb") as file:
        # Write the response content to the file
        file.write(response.content)

    