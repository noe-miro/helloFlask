import tensorflow as tf
import keras 
from keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from keras.applications.vgg16 import preprocess_input, decode_predictions

#problems with libcudnn
# physical_devices = tf.config.experimental.list_physical_devices('GPU') 
# tf.config.experimental.set_memory_growth(physical_devices[0], True)

def predict_pic(filename):
    vgg16 = VGG16()
    img = load_img(filename, target_size=(224, 224))
    img = img_to_array(img)  # Convertir en tableau numpy
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))  # Créer la collection d'images (un seul échantillon)
    img = preprocess_input(img)
    try:
        y = vgg16.predict(img)
    except:
        return('Error: something went wrong with the GPU')
    label = decode_predictions(y)
    # retrieve the most likely result, e.g. highest probability
    label = label[0][0]
    # print the classification
    return str(label[1]) + '(probability: ' + str(label[2]*100) + '%)'
