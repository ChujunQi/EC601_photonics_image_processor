import tensorflow as tf
import numpy as np
Iterator = tf.data.Iterator

def propagate(input_field, propagator):
    output = tf.ifft2d(tf.fft2d(input_field) * propagator)
    return output
