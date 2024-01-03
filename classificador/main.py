import os
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.models import load_model
from tqdm import tqdm
from PIL import Image

# Remover o limite de pixels do PIL
Image.MAX_IMAGE_PIXELS = None

# Caminhos necessários
caminho_pasta_entrada = 'D:/data'
caminho_saida_verdadeiro = 'D:/Resultados/verdadeiro'
caminho_saida_falso = 'D:/Resultados/falso'
caminho_modelo = 'C:/Users/lucas.ribeiro/validar_doc/modelo_classificador.h5'

# Carregar o modelo treinado
modelo = load_model(caminho_modelo)

# Função para preprocessar a imagem
def preprocessar_imagem(caminho_imagem):
    img = load_img(caminho_imagem, target_size=(150, 150))
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img /= 255.0
    return img

# Lista de arquivos de imagem
arquivos_imagem = [f for f in os.listdir(caminho_pasta_entrada) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Processar e classificar as imagens com barra de progresso
total_images = len(arquivos_imagem)
correct_predictions = 0

# Usando tqdm para mostrar a barra de progresso
for filename in tqdm(arquivos_imagem, desc="Processando imagens"):
    try:
        img_path = os.path.join(caminho_pasta_entrada, filename)
        img = preprocessar_imagem(img_path)
        prediction = modelo.predict(img)
        
        # Classificação e movimento do arquivo
        if prediction > 0.5:
            shutil.move(img_path, os.path.join(caminho_saida_verdadeiro, filename))
            if 'verdadeiro' in filename:
                correct_predictions += 1
        else:
            shutil.move(img_path, os.path.join(caminho_saida_falso, filename))
            if 'falso' in filename:
                correct_predictions += 1
    except Exception as e:
        print(f"Erro ao processar a imagem {filename}: {e}")

# Análise do classificador
if total_images > 0:
    accuracy = (correct_predictions / total_images) * 100
    print(f"Total de imagens: {total_images}")
    print(f"Classificações corretas: {correct_predictions}")
    print(f"Acurácia do classificador: {accuracy:.2f}%")
else:
    print("Nenhuma imagem para classificar.")
