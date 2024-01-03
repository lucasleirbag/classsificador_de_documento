import fitz  # PyMuPDF
import os

def converter_pdf_para_imagem(caminho_pdf, pasta_saida, dpi=200):
    # Abre o arquivo PDF
    documento = fitz.open(caminho_pdf)

    # Cria a pasta de saída se não existir
    if not os.path.exists(pasta_saida):
        os.makedirs(pasta_saida)

    # Itera sobre cada página do PDF
    for numero_pagina in range(len(documento)):
        # Pega a página
        pagina = documento.load_page(numero_pagina)

        # Converte a página para um objeto imagem
        imagem = pagina.get_pixmap(matrix=fitz.Matrix(dpi / 72, dpi / 72))

        # Salva a imagem
        nome_arquivo_saida = f"{os.path.splitext(os.path.basename(caminho_pdf))[0]}_pagina_{numero_pagina + 1}.png"
        caminho_completo_saida = os.path.join(pasta_saida, nome_arquivo_saida)
        imagem.save(caminho_completo_saida)

    # Fecha o documento
    documento.close()

# Caminho da pasta que contém os PDFs
pasta_pdf = "D:/pdf"
pasta_saida = "D:/data_resultado_convert"

# Itera sobre cada arquivo na pasta
for arquivo in os.listdir(pasta_pdf):
    caminho_completo = os.path.join(pasta_pdf, arquivo)
    if os.path.isfile(caminho_completo) and arquivo.lower().endswith('.pdf'):
        converter_pdf_para_imagem(caminho_completo, pasta_saida)
        