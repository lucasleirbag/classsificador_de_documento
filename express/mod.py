import os
import shutil
from tqdm import tqdm

def organize_png_files(model_directory, png_directory, destination_directory):
    # Criando um mapeamento da estrutura da pasta modelo
    model_structure = {}
    print("Lendo estrutura da pasta modelo...")
    for uf in tqdm(os.listdir(model_directory)):
        uf_path = os.path.join(model_directory, uf)
        if os.path.isdir(uf_path):
            for subfolder in os.listdir(uf_path):
                subfolder_path = os.path.join(uf_path, subfolder)
                if os.path.isdir(subfolder_path):
                    for file in os.listdir(subfolder_path):
                        if file.endswith('.pdf'):
                            file_base_name = os.path.splitext(file)[0]
                            model_structure[file_base_name] = os.path.join(destination_directory, uf, subfolder)

    # Organizando os arquivos PNG
    print("Organizando arquivos PNG...")
    for png_file in tqdm(os.listdir(png_directory)):
        base_name = os.path.splitext(png_file)[0]
        base_name = base_name.split('_pagina_')[0]  # Tratar arquivos com sufixos _pagina_
        if base_name in model_structure:
            dest_path = model_structure[base_name]
            os.makedirs(dest_path, exist_ok=True)
            shutil.move(os.path.join(png_directory, png_file), os.path.join(dest_path, png_file))
            print(f"Movendo '{png_file}' para '{dest_path}'")

# Exemplo de uso
organize_png_files("//arquivos/Areas/CL/COORDENACAO DE LOGISTICA/LOGsDOCs_V2020/PROJETOS DE AVALIAÇÃO/2023/INEP_ENEM _2023/1. PROVA_OBJETIVA_E_DISCURSIVA/TERMOS LIMPEZA ENEM",
                   "//arquivos/Areas/CL/COORDENACAO DE LOGISTICA/LOGsDOCs_V2020/PROJETOS DE AVALIAÇÃO/2023/INEP_ENEM _2023/1. PROVA_OBJETIVA_E_DISCURSIVA/RESULTADOS/resultado/resultado/verdadeiro",
                   "//arquivos/Areas/CL/COORDENACAO DE LOGISTICA/LOGsDOCs_V2020/PROJETOS DE AVALIAÇÃO/2023/INEP_ENEM _2023/1. PROVA_OBJETIVA_E_DISCURSIVA/RESULTADOS/resultado/Resultado_blabla")
