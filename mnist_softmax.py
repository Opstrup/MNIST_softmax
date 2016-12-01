"""
First tensorflow project, solve the MNIST problem.
(recognise hand-written numbers and label them correctly)

Source of MNIST data: http://yann.lecun.com/exdb/mnist/
"""
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import import_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

# The MNIST data is split into three parts:
# 55,000 data points of training data (mnist.train),
# 10,000 points of test data (mnist.test),
# 5,000 points of validation data (mnist.validation).
