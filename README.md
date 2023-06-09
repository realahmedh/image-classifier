# Image Classifier

\documentclass{article}
\usepackage{amsmath}
\usepackage{graphicx} 
\usepackage{listings}
\usepackage{color}

\title{Image Classifier Project Documentation}
\author{Human}

\begin{document}

\maketitle

\section{Importing the Dataset}
The dataset used for this project consisted of 60,000 32x32 colour images in 10 classes. It was split into 48,000 training images and 12,000 validation images. The images and labels were loaded from binary files and the lists were combined into numpy arrays. The images were normalized to have values between 0 and 1.

\section{Preprocessing the Data}
The images were reshaped to $32\\times32\\times3$ and normalized to range from 0 to 1. The data was then split into training and validation sets with a 80\% - 20\% split.

\section{Model Architecture}
The model used a sequential API with the following layers:
\begin{itemize} 
\item Convolutional layer with 32 filters of size 3x3 and ReLU activation
\item Max pooling layer with size 2x2
\item Convolutional layer with 64 filters of size 3x3 and ReLU activation 
\item Max pooling layer with size 2x2
\item Convolutional layer with 64 filters of size 3x3 and ReLU activation
\item Flatten layer
\item Dense layer with 64 units and ReLU activation
\item Dense layer with 10 units and softmax activation for output 
\end{itemize}

The model was compiled with the Adam optimizer, sparse categorical crossentropy loss and accuracy metric.

\section{Training} 
The model was trained for 20 epochs with a batch size of 64. The training and validation accuracy and loss were plotted. 
\begin{figure}[H]
\centering
\includegraphics[width=10cm]{accuracy_loss.png}
\caption{Training and Validation Accuracy/Loss Curves}
\label{fig:accuracy_loss}
\end{figure}

\section{Evaluation}
The final validation loss was 0.8829 and accuracy was 73.85\%.

\section{Testing on New Photo}
The model was tested on a new photo and predicted the class `airplane' with a probability of 0.8113.
\begin{figure}[H]
\centering
\includegraphics[width=8cm]{testing.png}
\caption{Testing Image and Prediction}
\label{fig:testing} 
\end{figure}

\section{Saving the Model} 
The trained model was saved in .h5 format using the Keras model.save() method.

\end{document}
