# Name: Gerald Turner
# Assignment: Unit 9 Assignment
# Date: Mar 9. 2026

import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np

(train_images, train_labels), (test_images, test_labels) = datasets.mnist.load_data()

train_images = train_images.reshape((60000, 28, 28, 1)).astype("float32") / 255.0
test_images = test_images.reshape((10000, 28, 28, 1)).astype("float32") / 255.0

model = models.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(28,28,1)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Dropout(0.25),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10,activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

history = model.fit(train_images,train_labels,epochs=5,validation_split=0.1)

test_loss,test_acc = model.evaluate(test_images,test_labels)
print("Test Loss:",test_loss)
print("Test Accuracy:",test_acc)

predictions = model.predict(test_images)

plt.figure(figsize=(15,6))
for i in range(10):
    plt.subplot(2,5,i+1)
    plt.imshow(test_images[i].reshape(28,28),cmap='gray')
    plt.title(f"Actual:{test_labels[i]} Pred:{np.argmax(predictions[i])}")
    plt.axis('off')

plt.tight_layout()
plt.show()