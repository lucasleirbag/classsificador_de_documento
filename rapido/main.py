import os
import shutil

def organizar_pdfs_por_uf(diretorio):
    # Lista todos os arquivos no diretório
    arquivos = os.listdir(diretorio)

    for arquivo in arquivos:
        # Verifica se o arquivo é um PDF
        if arquivo.endswith('.pdf'):
            # Extrai a UF do nome do arquivo
            uf = arquivo.split(' - ')[-1].replace('.pdf', '')

            # Caminho da pasta da UF
            pasta_uf = os.path.join(diretorio, uf)

            # Cria a pasta da UF se ela não existir
            if not os.path.exists(pasta_uf):
                os.makedirs(pasta_uf)

            # Caminho completo do arquivo PDF
            arquivo_original = os.path.join(diretorio, arquivo)

            # Caminho completo do novo local do arquivo PDF
            novo_arquivo = os.path.join(pasta_uf, arquivo)

            # Move o arquivo para a pasta da UF
            shutil.move(arquivo_original, novo_arquivo)

# Substitua '/caminho/para/seus/pdfs' pelo caminho real onde os PDFs estão armazenados
organizar_pdfs_por_uf("//arquivos/areas/CL/COORDENACAO DE LOGISTICA/LOGsDOCs_V2020/PROJETOS DE AVALIAÇÃO/2023/INEP_ENEM_23_REAPLICAÇÃO/EQUIPE DE CAMPO/RESUMO DE CONTRATAÇÃO")
