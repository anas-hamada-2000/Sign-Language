import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import pickle
import tensorflow_hub as hub


X=np.empty(shape=(14500,224,224,3), dtype=np.float16)

with open("data/images and there labels dataset/XXX (1)", "rb") as fp:
  for i in range(29):
    X[i*500:i*500+500] = pickle.load(fp)

with open("data/images and there labels dataset/YYY (1)", "rb") as fp:
  Y = pickle.load(fp)

  print(X.shape, Y.shape)

letters = ['A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R',
           'S', 'Ş', 'T', 'U', 'Ü', 'V', 'Y', 'Z']


def plot_sample(X, Y, index):
  plt.imshow(X[index].astype(int))
  plt.xlabel(letters[Y[index]])
  plt.show()

plot_sample(X, Y, 145)

for index,item in enumerate(X):
  X[index]=X[index]/255

feature_extractor_model = "https://tfhub.dev/google/tf2-preview/mobilenet_v2/feature_vector/4"

pretrained_model_without_top_layer = hub.KerasLayer(
    feature_extractor_model, input_shape=(224, 224, 3), trainable=False)

num_of_letters = 29

model = tf.keras.Sequential([
pretrained_model_without_top_layer,
tf.keras.layers.Dense(num_of_letters)
])

model.summary()

model.compile(
  optimizer="adam",
  loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
  metrics=['acc'])

model.fit(X, Y, epochs=3)

model.save('my_model.h5')