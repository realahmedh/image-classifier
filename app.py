import pickle
import cv2
import tkinter as tk
from tkinter import filedialog
import numpy as np
import keras


# Load the saved model
model = keras.models.load_model('model.h5')


def load_data(file):
    with open(file, 'rb') as f:
        data = pickle.load(f, encoding='bytes')
    return data


train_data = load_data("my_dataset/data_batch_1")
test_data = load_data("my_dataset/test_batch")

# Access the training data and labels
train_images = train_data[b'data']
train_labels = train_data[b'labels']

# Access the test data and labels
test_images = test_data[b'data']
test_labels = test_data[b'labels']


classes = ['airplane', 'automobile', 'bird', 'cat',
           'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
class_labels = [classes[label] for label in train_labels]



# Predict the model
def predict_image(image, class_labels):
    # Preprocess the image
    image = cv2.resize(image, (32, 32), interpolation=cv2.INTER_CUBIC)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    # Make the prediction
    prediction = model.predict(image)

    # Decode the prediction to get the class label
    class_index = np.argmax(prediction)
    if class_index < len(class_labels):
        class_label = class_labels[class_index]
    else:
        class_label = "Unknown"

    return class_label


root = tk.Tk()
root.title("Image Classifier")


def upload_image():
    file_path = filedialog.askopenfilename()

    # Load the image from the file path
    image = cv2.imread(file_path)

    # Load the CIFAR-10 class labels
    class_labels = ['airplane', 'automobile', 'bird', 'cat', 'deer',
                    'dog', 'frog', 'horse', 'ship', 'truck']

    # Predict the class label for an image
    class_label = predict_image(image, class_labels)

    print("The image is classified as:", class_label)

    result_label.config(
        text=f"The photo you added is classified as: {class_label}")


upload_button = tk.Button(root, text="Upload Photo", command=upload_image)
upload_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()


