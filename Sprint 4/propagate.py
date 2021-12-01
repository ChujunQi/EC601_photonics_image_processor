import tensorflow as tf
import numpy as np
Iterator = tf.data.Iterator

xx = np.load('xx.npy')
yy = np.load('yy.npy')
Lambda = np.load('Lambda.npy')
k_z_values = np.load('k_z_values.npy')
x_tensor = tf.constant(xx, tf.float32)
y_tensor = tf.constant(yy, tf.float32)
Lambda_tensor = tf.constant(Lambda, tf.float32)
k_z = tf.constant(k_z_values, tf.complex64)
f = tf.constant(0.3E-2)

def propagate(input_field, propagator):
    output = tf.ifft2d(tf.fft2d(input_field) * propagator)
    return output
