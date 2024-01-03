import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Caminhos para os diretórios de treinamento e validação
diretorio_treino = 'C:/Users/lucas.ribeiro/validar_doc/aprendizado/data/treino'
diretorio_validacao = 'C:/Users/lucas.ribeiro/validar_doc/aprendizado/data/validacao'

# Configurações para o treinamento
batch_size = 32
image_size = (150, 150)

# Geradores de dados - eles também farão o pré-processamento das imagens
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    diretorio_treino,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary')

validation_generator = validation_datagen.flow_from_directory(
    diretorio_validacao,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary')

# Modelo de CNN
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Verifique se o número de amostras é maior que 0
if train_generator.samples == 0 or validation_generator.samples == 0:
    raise ValueError("Não foram encontradas imagens nos diretórios de treino/validação.")

# Calcule os passos por época corretamente
steps_per_epoch = max(1, train_generator.samples // batch_size)
validation_steps = max(1, validation_generator.samples // batch_size)

# Treinando o modelo
history = model.fit(
    train_generator,
    steps_per_epoch=steps_per_epoch,
    epochs=15,
    validation_data=validation_generator,
    validation_steps=validation_steps
)

# Salvar o modelo treinado
model.save('modelo_classificador.h5')

# Imprimir o histórico de treinamento
print("Histórico de treinamento:")
for epoch, stats in enumerate(zip(history.history['accuracy'], history.history['loss']), start=1):
    print(f"Época {epoch}:")
    print(f"Acurácia: {stats[0]}")
    print(f"Perda: {stats[1]}")

# Imprimir a acurácia de validação
val_accuracy = history.history['val_accuracy'][-1]
print(f"\nAcurácia de validação após o treinamento: {val_accuracy * 100:.2f}%")
