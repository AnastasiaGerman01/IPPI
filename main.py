import numpy as np
from keras.models import Sequential
from keras import activations
from keras.layers import Input, Conv2D, MaxPooling2D, Dense, Flatten
from data import test_data, test_answer, check_data, check_answer

folder_dir = "C:/Users/germa/Downloads/SimpleCube++/SimpleCube++/1train/PNG"

print("start learning model")

test_data = np.array(test_data)
test_answer = np.array(test_answer)
check_data = np.array(check_data)
check_answer = np.array(check_answer)
print(test_answer.shape)
print(test_data.shape)

model = Sequential([
    Input(shape=(64, 64, 3)),
    Conv2D(240, (1, 1), activation='relu'),
    MaxPooling2D(pool_size=(16, 16)),
    Flatten(),
    Dense(40, activation=activations.relu),
    Dense(3, activation=activations.softmax)
])

model.compile('adam',
              loss='mean_squared_error',
              metrics=['accuracy'])

model.fit(test_data, test_answer, batch_size=32, epochs=7)

model.evaluate(check_data, check_answer)
