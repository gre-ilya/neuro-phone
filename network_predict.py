from tensorflow.python.keras.models import load_model
from PIL import Image
import numpy as np

# путь к нейронке
model = load_model(r'restnet2.h5')

# размер изображениния для нейронки
img_width, img_height = 240, 240

# важная константа - определяет вероятность
# при которой выход нейронки декодируется как наличие телефона
# если часто не распознается телефон там где он есть можно понизить до 0.5
# если часто видит телефон там где его нет можно повысить до 0.95
const = 0.9


def resize_image(image):
    im = Image.open(image).convert('RGB')
    im = im.resize((img_width, img_height))
    return im


# Подавать на вход путь к картинке любого размера
# True - есть телефон, False - нет
def get_predict(image_path):
    im = np.asarray(resize_image(image_path))
    im = np.expand_dims(im, axis=0)
    result = model.predict(im)
    if result[0] >= const:
        return True
    return False
