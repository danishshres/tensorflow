'''
HelloWorld example using TensorFlow.
Author: Danish shrestha
Project: https://github.com/danishshres/tensorflow/
'''

import tensorflow as tf

# Hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.
hello = tf.constant('Hello world from Tensorflow!')

# Start tf session
sess = tf.Session()

# Run the op
print(sess.run(hello))