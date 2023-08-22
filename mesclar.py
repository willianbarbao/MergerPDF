import PyPDF2
import os

# Inicializando o objeto de mesclagem de PDFs
merger = PyPDF2.PdfMerger()

# Listando os arquivos na pasta "arquivos" e ordenando-os
lista_arquivos = os.listdir("arquivos")
lista_arquivos.sort()
print(lista_arquivos)

# Iterando sobre cada arquivo na lista de arquivos
for arquivo in lista_arquivos:
    # Verificando se o arquivo possui a extensão .pdf
    if ".pdf" in arquivo:
        # Adicionando o arquivo atual à operação de mesclagem
        merger.append(f"arquivos/{arquivo}")

# Escrevendo o PDF final mesclado
merger.write("PDF Final.pdf")
