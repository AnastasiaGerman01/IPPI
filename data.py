from keras.preprocessing import image
from random import randint
import pandas as pd
import os

test_data = []
count = 0

folder_dir = "C:/Users/germa/Downloads/SimpleCube++/SimpleCube++/1train/PNG"

for images in os.listdir(folder_dir):
    count += 1
    if (images.endswith(".png")):
        img_path = folder_dir + '/' + images
        img = image.load_img(img_path)
        img_array = image.img_to_array(img)/255
        for i in range(10):
            x_number = randint(0, 116)
            y_number = randint(0, 580)
            new_test = img_array[x_number:x_number+64,y_number:y_number+64]
            test_data.append(new_test)

answer = df = pd.read_csv('C:/Users/germa/Downloads/SimpleCube++/SimpleCube++/1train/gt.csv')
test_answer = []

for i in range(answer.shape[0]):
    arr = [answer.iloc[i]['mean_r'], answer.iloc[i]['mean_g'], answer.iloc[i]['mean_b']]
    for j in range(10):
        test_answer.append(arr)

folder_dir = "C:/Users/germa/Downloads/SimpleCube++/SimpleCube++/test/PNG"

check_data = []

for images in os.listdir(folder_dir):
    count += 1
    if (images.endswith(".png")):
        img_path = folder_dir + '/' + images
        img = image.load_img(img_path)
        img_array = image.img_to_array(img)/255
        for i in range(10):
            x_number = randint(0, 116)
            y_number = randint(0, 580)
            new_test = img_array[x_number:x_number+64,y_number:y_number+64]
            check_data.append(new_test)

answer = df = pd.read_csv('C:/Users/germa/Downloads/SimpleCube++/SimpleCube++/test/gt.csv')
check_answer = []

for i in range(answer.shape[0]):
    arr = [answer.iloc[i]['mean_r'], answer.iloc[i]['mean_g'], answer.iloc[i]['mean_b']]
    for j in range(10):
        check_answer.append(arr)

