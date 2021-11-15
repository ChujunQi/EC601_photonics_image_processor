# Sprint 3

## Overivew
### FFT
In sprint 3, we built FFT(Fast Fourier Transform) layers for our CNN. If we only use filters and kernels, the speed of our system would be slow when we try to train a large number of data, which is O(n^2). In the real time analysis, it might take even a few hours. However, after using computing FFT for kernels of CNN, the speed will be increased to O(nlogn). 

### VGG16
VGG16 is a convolutional neural network for large image recognition. In VGG16 file, we contains 3 types of layers, convolutional layers, max pooling layers, and dense layers. 

Convolutional layers apply a convolution operation to the input, passing the result to the next layer. A convolution converts all the pixels in its receptive field into a single value using dot product.

Maximum pooling is a pooling operation that calculates the maximum, or largest, value in each patch of each feature map. Max pooling layers take the max of the region from the input overlapped by the kernel.

Dense layers are layers that are deeply connected with their preceding layers, which means the neurons of the layer are connected to every neuron of its preceding layer.

## What we have done? 
Now we have built our sample CNN, photonics layers, a FFT to speed up our CNN.
## Future Sprints
1. Try to complete our photonic part.
2. Consider how to connect CNN and our photonic accelerator. 
3. Learn how to use photonics simulator online.


