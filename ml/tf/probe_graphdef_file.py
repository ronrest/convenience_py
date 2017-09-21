""" A barebones workflow for experimentally probing a pretrained tensorflow
    graph_def (*.pb) file.
"""
from __future__ import print_function, division
import numpy as np
import tensorflow as tf

# SETTINGS
tensorboard_dir = "/tmp/tf"
graph_file = "mygraph.pb"


tf_graph = tf.Graph()
with tf_graph.as_default():
    # with tf.variable_scope('inputs') as scope:
    #     tf_X = tf.placeholder(tf.float32, shape=(3, 4))

    # LOAD GRAPH_DEF FILE
    access_these=[]           # operations to extract
    remap_input = None        # remap pretrained model input to a new tensor
    with tf.device('/cpu:0'): # Prevent multiple prallel I/O operations
        with tf.gfile.FastGFile(graph_file, 'rb') as file_obj:
            # Load the graph from file
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(file_obj.read())

            # Extract particular operations/tensors
            requested_ops = tf.import_graph_def(
                graph_def,
                name='',
                return_elements=access_these,
                input_map=remap_input
                )
    print(requested_ops)

    # TENSORBOARD
    with tf.variable_scope('tensorboard') as scope:
        tf_summary_writer = tf.summary.FileWriter(tensorboard_dir, graph=tf_graph)
        tf_summary_op = tf.summary.scalar(name="dummy", tensor=4)


# INTERACTIVE MODE
sess = tf.Session(graph=tf_graph)
# sess.run(tf.global_variables_initializer())

# RUN TENSORBOARD
summary_str = sess.run(tf_summary_op)
tf_summary_writer.add_summary(summary_str, 0)
tf_summary_writer.flush()
# tensorboard --logdir="/tmp/tf"
# 0.0.0.0:6006

# INPUTS
# X = np.random.randn(3,4)
# feed_dict = {tf_X: X}
# output = sess.run(tf_y, feed_dict=feed_dict)
# print(output)

# PROBE OPERATIONS
#Get a list of all the operations in a graph
tf_graph.get_operations()

#Get a list of all the operation names in a graph
[op.name for op in graph.get_operations()]

# Get specific operations/tensors
# tf_graph.get_operation_by_name("layer1")
# tf_graph.get_tensor_by_name("layer1:0")


sess.close()
