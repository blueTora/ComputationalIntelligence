# Handwritten Digit Recognition from Scratch

This project focuses on implementing a handwritten digit recognition system without relying on any pre-existing machine learning frameworks or libraries. The aim is to develop a deep learning model entirely from scratch to recognize and classify handwritten digits.

## Video References

Please refer to the following YouTube videos for detailed explanations and examples:

<a href="http://www.youtube.com/watch?feature=player_embedded&v=aircAruvnKk" target="_blank"><img src="http://img.youtube.com/vi/aircAruvnKk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=IHZwWFHWa-w" target="_blank"><img src="http://img.youtube.com/vi/IHZwWFHWa-w/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=Ilg3gGewQ5U" target="_blank"><img src="http://img.youtube.com/vi/Ilg3gGewQ5U/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
<a href="http://www.youtube.com/watch?feature=player_embedded&v=tIeHLnjs5U8" target="_blank"><img src="http://img.youtube.com/vi/tIeHLnjs5U8/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

## Introduction

Handwritten digit recognition plays a crucial role in various applications, such as optical character recognition (OCR) and automated form processing. This project aims to develop a deep learning model that can accurately identify and classify handwritten digits. Unlike traditional approaches that heavily rely on machine learning frameworks or libraries, this project emphasizes building the entire model from scratch.

## Description

The purpose of this project is to gain a deeper understanding of the inner workings of deep learning algorithms by implementing them without relying on pre-existing frameworks or libraries. By developing the handwritten digit recognition system from scratch, we aim to grasp the fundamental concepts and mechanisms involved in deep learning.

## Algorithms

The project utilizes the following algorithms:

1. **Feedforward Neural Networks (FNN)**: FNNs form the basis of the deep learning model in this project. They consist of an input layer, one or more hidden layers, and an output layer. Each layer is composed of interconnected nodes (neurons) that perform weighted computations and pass the information forward through activation functions.

2. **Backpropagation**: Backpropagation is a learning algorithm used to train the FNN. It involves the propagation of errors backward through the network, adjusting the weights of the connections iteratively to minimize the difference between the predicted outputs and the actual outputs.

3. **Mini-batch Gradient Descent**: Instead of using the traditional gradient descent, this project employs mini-batch gradient descent. Mini-batch gradient descent divides the training dataset into smaller batches, and for each batch, it computes the gradient and updates the model's parameters. This approach offers a balance between the computational efficiency of stochastic gradient descent and the stability of batch gradient descent.

4. **Activation Functions**: Activation functions are applied to the outputs of neurons within the network. This project employs popular activation functions like sigmoid, ReLU (Rectified Linear Unit), and softmax to introduce non-linearity and allow the model to learn complex representations.

## Logic of the Project
**Data Acquisition**: Obtain a dataset of handwritten digits, such as the MNIST dataset, which consists of thousands of labeled examples.

2. **Data Preprocessing**: Preprocess the dataset by normalizing the pixel values to a suitable range, converting labels to one-hot encodings, and splitting the data into training and testing sets.

3. **Model Architecture**: Design the architecture of the deep learning model, specifying the number of layers, the number of neurons in each layer, and the activation functions to be used.

4. **Initialization**: Initialize the weights and biases of the model using appropriate techniques, such as random initialization or Xavier initialization.

5. **Forward Propagation**: Implement the forward propagation mechanism, where inputs are passed through the network, weights are multiplied, and activation functions are applied to produce predictions.

6. **Loss Calculation**: Define an appropriate loss function, such as cross-entropy loss, to measure the discrepancy between predicted and actual outputs.

7. **Backpropagation**: Implement the backpropagation algorithm to calculate the gradients of the loss function with respect to the weights and biases. Update the weights and biases accordingly to minimize the loss.

8. **Training**: Iterate through the training dataset using mini-batches, performing forward and backward propagation for each batch. Adjust the model's parameters using mini-batch gradient descent and update the weights and biases.

9. **Evaluation**: Evaluate the performance of the trained model on the testing dataset. Calculate relevant metrics such as accuracy, precision, and recall to assess its effectiveness.

10. **Prediction**: Utilize the trained model to make predictions on new, unseen handwritten digit samples. Convert the model's outputs into human-readable digit labels.

By implementing the logic outlined above, this project provides a comprehensive understanding of the key components and processes involved in building a deep learning model for handwritten digit recognition without relying on external machine learning frameworks or libraries.

## Results

The project aims to achieve accurate handwritten digit recognition.

<img align="center" alt="Loss Diagram" width="60%" src="https://github.com/negarK2000/ComputationalIntelligence/blob/master/HandwrittenDigitRecognition/loss_diagram.jpg" />
<img align="center" alt="Accuracy Diagram" width="60%" src="https://github.com/negarK2000/ComputationalIntelligence/blob/master/HandwrittenDigitRecognition/accuracy.jpg" />

## Acknowledgments

We would like to express our gratitude to the authors of the YouTube videos mentioned above for their valuable tutorials and examples. Additionally, we acknowledge any other resources, libraries, or frameworks utilized in this project.
