# Importar las librerías os, glob y PyPDF2
import os
import glob
import PyPDF2

# Definir el nombre de la carpeta que contiene las 4 subcarpetas
carpeta = r'c:\Users\Sergio_Lenovo\OneDrive - sergiovelayos gmail\OneDrive\Documentos\escrapear pdfs ayto badalona\pdfs\normativa municipal'

# print(os.listdir(carpeta))

# Ruta actual
# print(os.getcwd())

# Definir el nombre del fichero de texto donde se exportarán los pdfs
fichero = "all_pdfs_to_text.txt"

# Abrir el fichero de texto en modo escritura
with open(fichero, "w") as file:
  # Recorrer las 4 subcarpetas de la carpeta
  for subcarpeta in os.listdir(carpeta):
    # Obtener la ruta completa de la subcarpeta
    ruta_subcarpeta = os.path.join(carpeta, subcarpeta)
    # Recorrer los archivos pdf de la subcarpeta
    for pdf in glob.glob(ruta_subcarpeta + "/*.pdf"):
      # Obtener el nombre del fichero pdf sin la extensión
      nombre_pdf = os.path.splitext(os.path.basename(pdf))[0]
      # Escribir el nombre del fichero pdf en el fichero de texto seguido de un salto de línea
      file.write(nombre_pdf + "\n")
      # Abrir el archivo pdf en modo lectura binaria
      with open(pdf, "rb") as pdf_file:
        # Crear un objeto PdfFileReader para leer el contenido del pdf
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        # Obtener el número de páginas del pdf
        # num_paginas = pdf_reader.numPages
        num_paginas = len(pdf_reader.pages)
        # Recorrer las páginas del pdf
        for pagina in range(num_paginas):
          # Obtener el objeto Page del pdf_reader
          page_obj = pdf_reader.pages[pagina]
          # Extraer el texto de la página
          texto = page_obj.extract_text()
          # Escribir el texto en el fichero de texto
          file.write(texto)
      # Escribir un salto de línea al finalizar cada fichero pdf
      file.write("\n")
