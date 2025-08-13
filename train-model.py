import tensorflow as tf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Import tools from tensorflow
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, BatchNormalization, Input
from sklearn.model_selection import train_test_split

# Load parsed data using os
base_dir = os.getcwd()
data_file_path = os.path.join(base_dir, "stock_data.npz")
data = np.load("stock_data.npz")

X = data['X_data']
Y = data['Y_data']

print(f"X shape : {X.shape}")
print(f"Y shape : {Y.shape}")

# Split data and check shapes
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2)

print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)

# Create the model
model = Sequential([
    Input(shape=(60,)),
    Dense(128),
    BatchNormalization(),
    Activation('relu'),
    Dropout(0.25),

    Dense(64),
    BatchNormalization(),
    Activation('relu'),
    Dropout(0.25),

    Dense(64),
    BatchNormalization(),
    Activation('relu'),
    Dropout(0.25),

    Dense(1),
    Activation('sigmoid')
])

model.summary()

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Train and plot
history = model.fit(X_train, y_train, batch_size=32, epochs=50)

plt.plot(history.history['accuracy'])
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
model.save("stock_model.keras")

y_preds = np.round(model.predict(X_test))

# Accuracy (about 52%)
test_acc = np.mean(y_preds == y_test)
print(f"Accuracy: {test_acc}")