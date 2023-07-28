# # Opción 1
# import re
# from pdfminer.high_level import extract_pages,extract_text

# text = extract_text(r'C:\Users\Sergio_Lenovo\OneDrive - sergiovelayos gmail\OneDrive\Documentos\Jugando con datos\Badalona\seguimiento gobierno Albiol\expedientes\2023\ple_12_05_2023_03_certificat_acord_ple_AJB106921.pdf')

# print(text) # Formato correcto pero encoding incorrecto. Ejemplo:
# # D. de Comptabilitat
# # Tramitaci� i aprovaci� d�una proposta de modificaci� del pressupost municipal de 



# # print(text.encode(encoding='utf-8')) # Encoding y formato incorrecto: b"Expedient:\nRef. Addic.:\nUO Responsable:\nAssumpte:\n\nProcediment:\n\n2023/00017719J\nPLE-MAIG-1\nD. de Comptabilitat\nTramitaci\xc3\xb3 i aprovaci\xc3\xb3 d\xe2\x80\x99una proposta de modificaci\xc3\xb3 del pressupost municipal de \n2023, en pr\xc3\xb2rroga 



# Opción 2
# from PyPDF2 import PdfReader
# import codecs

# reader = PdfReader(r'C:\Users\Sergio_Lenovo\OneDrive - sergiovelayos gmail\OneDrive\Documentos\Jugando con datos\Badalona\seguimiento gobierno Albiol\expedientes\2023\ple_12_05_2023_03_certificat_acord_ple_AJB106921.pdf')
# page = reader.pages[0]
# print(page.extract_text().encode("utf-8")) # Formato y encoding incorrecto


