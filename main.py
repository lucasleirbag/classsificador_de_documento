import os
import shutil

def copiar_arquivos(diretorio_principal, diretorio_destino):
    # Lista todas as subpastas (UFs) dentro do diretório principal
    ufs = [os.path.join(diretorio_principal, nome) for nome in os.listdir(diretorio_principal) if os.path.isdir(os.path.join(diretorio_principal, nome))]

    # Processa cada pasta de UF
    for diretorio_uf in ufs:
        # Percorre todos os diretórios e subdiretórios na pasta da UF
        for pasta_atual, subpastas, arquivos in os.walk(diretorio_uf):
            for arquivo in arquivos:
                # Monta o caminho completo do arquivo
                caminho_completo = os.path.join(pasta_atual, arquivo)
                # Copia o arquivo para o diretório de destino
                shutil.copy2(caminho_completo, diretorio_destino)

# Defina aqui o diretório da UF e o diretório de destino
diretorio_uf = 'C:/Users/lucas.ribeiro/Music'
diretorio_destino = 'C:/Users/lucas.ribeiro/Videos/Resultado'

copiar_arquivos(diretorio_uf, diretorio_destino)
