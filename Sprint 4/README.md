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

# Second Part
## What we have done in sprint 4  
We have done ResNet and in the first step of building the classification.

