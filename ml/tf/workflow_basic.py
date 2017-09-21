""" The most basic workflow for testing components of tensorflow.
"""
from __future__ import print_function, division
import numpy as np
import tensorflow as tf

graph = tf.Graph()
with graph.as_default():
    tf_X = tf.placeholder(tf.float32, shape=(3, 4))
    tf_y = tf_X * 2

with tf.Session(graph=graph) as sess:
    sess.run(tf.global_variables_initializer())
    X = np.random.randn(3,4)
    output = sess.run(tf_y, feed_dict={tf_X: X})
    print(output)


# # INTERACTIVE MODE
# sess = with tf.Session(graph=graph):
# X = np.random.randn(3,4)
# output = session.run(tf_y, feed_dict={tf_X: X})
# print(output)
#
# sess.close()
