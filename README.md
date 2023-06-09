# Image Classifier

## Importing the Dataset
The dataset used for this project consisted of 60,000 32x32 colour images in 10 classes. It was split into 48,000 training images and 12,000 validation images. The images and labels were loaded from binary files and the lists were combined into numpy arrays. The images were normalized to have values between 0 and 1.

## Preprocessing the Data
The images were reshaped to 32x32x3 and normalized to range from 0 to 1. The data was then split into training and validation sets with a 80% - 20% split.

## Model Architecture 
The model used a sequential API with the following layers:
* Convolutional layer with 32 filters of size 3x3 and ReLU activation
* Max pooling layer with size 2x2
* Convolutional layer with 64 filters of size 3x3 and ReLU activation  
* Max pooling layer with size 2x2
* Convolutional layer with 64 filters of size 3x3 and ReLU activation
* Flatten layer  
* Dense layer with 64 units and ReLU activation
* Dense layer with 10 units and softmax activation for output   

The model was compiled with the Adam optimizer, sparse categorical crossentropy loss and accuracy metric.

## Training  
The model was trained for 20 epochs with a batch size of 64. The training and validation accuracy and loss were plotted.


## Evaluation
The final validation loss was 0.8829 and accuracy was 73.85%.  

## Testing on New Photo 
The model was tested on a new photo and predicted the class `airplane' with a probability of 0.8113.

![Testing Image and Prediction](testing-image.jpg)  

## Saving the Model   
The trained model was saved in .h5 format using the Keras model.save() method.
