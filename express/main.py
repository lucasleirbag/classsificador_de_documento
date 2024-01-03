import os
import re

def rename_png_files_remove_pagina(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            new_filename = re.sub(r'_pagina_\d+', '', filename)
            new_filepath = os.path.join(directory, new_filename)

            if not os.path.exists(new_filepath):
                os.rename(os.path.join(directory, filename), new_filepath)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"Skipping '{filename}', as '{new_filename}' already exists.")

rename_png_files_remove_pagina("//arquivos/Areas/CL/COORDENACAO DE LOGISTICA/LOGsDOCs_V2020/PROJETOS DE AVALIAÇÃO/2023/INEP_ENEM _2023/1. PROVA_OBJETIVA_E_DISCURSIVA/RESULTADOS/test/verdadeiro")
