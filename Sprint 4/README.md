Sprint 4 
== 
# First Part
## 1. ResNet  
In sprint 4, we built a residual neural network, which could skip connections, or shortcuts to jump over some layers. The main reason to build it is to avoid the problem of vanishing gradients, and to mitigate the Degradation problem.  

Network performace before using residual
![image](https://github.com/ChujunQi/EC601_photonics_image_processor/blob/main/Sprint%204/performance%20before%20using%20resnet.png)  

Network performace using residual
![image](https://github.com/ChujunQi/EC601_photonics_image_processor/blob/main/Sprint%204/performance%20using%20resnet.png)  

## 2. Mnist  
We choose to use MNIST classification by TensorFlow. Mnist is a popular standard in machine learning models consisting of 28 × 28 images of handwritten decimal digits from 0 to 9. TensorFlow is a math library mainly focusing on the tasks of deep neural networks. And in our project, it will be used to predict the image by looking at thousands of examples that have been tagged. We will then use the test data set to check the accuracy of the model.

## 3. ONN
We will implement the first set of convolution operations optically and keep other layers electronically. In order to model diffraction and calculate electric field distribution, we can use FFT and angular spectrum propagator.

![image](https://github.com/ChujunQi/EC601_photonics_image_processor/blob/main/Sprint%204/FFT.png)
Above figure shows our FFT class. In FFT, we have variables to handle input channel, output channel, and kernel size for Convolutional Neural Network. 

![image](https://github.com/ChujunQi/EC601_photonics_image_processor/blob/main/Sprint%204/propagate.png)
The second figure shows how to implement the propagator. The function will use a 2D FFT to calculate the electric field distribution. In the code, input_field is the input electric field, and the function will output a result after propagation. 

![image](https://github.com/ChujunQi/EC601_photonics_image_processor/blob/main/Sprint%204/layers.png)
Based on our previous CNN model, we plan to replace the first group of layers to optical convolutional layers. Right now we haven’t finished yet.

# Second Part
## What we have done in sprint 4  
We have done ResNet and in the first step of building the classification.

