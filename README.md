# EC601 photonics image processing
Our code is separated in each sprints. Sprint 2 contains basice CNN code and some tests about ONN(Optical Neural Networks). Sprint 3 have some implementations about VGG 16 and FFT. In sprint 4, we mainly focus on building optical layers and also trying to compare VGG 16, ResNet, and AlexNet. Finally, we use AlexNet to be our basic CNN. 

Resource paper: https://arxiv.org/pdf/1901.03661.pdf
## Introduction
1. We will use CNN for image processing, the type of CNN could be AlexNet, VGG 16, or ResNet. They have different functionalities, but all of them are suitable for image processing.
2. Try to replace the first group of convolutional layers to optical layers in order to speed up the system.

## Product Mission
We aims to let our product detect or recognize things in images or videos automatically, having faster speed on image processing than the usual image processor, and Having high accuracy on recognizing important features in images.

## MVPs
1. Can detect the main feature of images or videos
2. Dealing with multiple things 
3. Using optical functionalities to speed our image processing system

## User Stories
1. Government: use face recognition to find criminals.
2. Smartphone users: unlock phone with face recognition and find things online by taking a photo

## Development Environment
1. Language: Python
2. Environment: Tensorflow, Keras

