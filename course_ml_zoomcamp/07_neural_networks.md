# Neural Networks and Deep Learning

- Deep Learning for Computer Vision | [Stanford Course](https://cs231n.github.io/)


## Tensorflow and Keras - Introduction

- `import tensorflow as tf`: to import tensorflow library
- `from tensorflow import keras`: to import keras
- `from tensorflow.keras.preprocessing.image import load_img`: to import load_img function
- `load_img('path/to/image', targe_size=(150,150))`: to load the image of 150 x 150 size in PIL format
- `np.array(img)`: convert image into a numpy array of 3D shape, where each row of the array represents the value of red, green, and blue color channels of one pixel in the image.

## Pre-trained models

- The keras.applications module has different pre-trained models with different architectures. - We'll use the model Xception which takes the input image size of (229, 229) and each image's pixel is scaled between -1 and 1.
- We create the instance of the pre-trained model using model = Xception(weights='imagenet', input_shape=(299, 229, 3)). Our model will use the weights from pre-trained imagenet and expect the input shape of (229, 229, 3) for images.
- Along with image size, the model also expects the batch_size which is the size of the batches of data (default 32). If one image is passed to the model, then the expected shape of the model should be (1, 229, 229, 3).
- The image data was peprocessed using preprocess_input function during Xception model's pre-taining. Therefore, we'll have to use this function on our data before making predictions, like so: X = preprocess_input(X).
The pred = model.predict(X) function returns 2D array of shape (1, 1000), where 1000 is the probablity of the image classes. decode_predictions(pred) can be used to get the class names and their probabilities in readable format.
In order to make the pre-trained model useful specific to our case, we'll have to do some tweak, which we'll do in the coming sections.
Classes, functions, and methods:

from tensorflow.keras.applications.xception import Xception: import the model from keras applications
from tensorflow.keras.application.xception import preprocess_input: function to perform preprocessing on images
from tensorflow.keras.applications.xception import decode_predictions: extract the predictions class names in the form of tuple of list
model.predict(X): function to make predictions on the test images