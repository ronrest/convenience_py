import tensorflow as tf
import numpy as np

# Label and prediction images
label = np.array([
    [1, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1]], dtype=np.uint8)

prediction = np.array([
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0]], dtype=np.uint8)


# TODO: THere is a bug in the folowing code. Fix it.
# ------------------------------------------------
#                                    Build a graph
# ------------------------------------------------
graph = tf.Graph()
with graph.as_default():
    tf_label = tf.constant(label, dtype=tf.int32)
    tf_prediction = tf.constant(prediction, dtype=tf.int32)
    # p = tf.reshape(prediction, [-1])
    # l = tf.reshape(label, [-1])
    # tf.constant([])
    tf_iou, _ = tf.metrics.mean_iou(tf_label, tf_prediction, num_classes=1)
    # iou_tf, _ = tf.metrics.mean_iou(label, prediction, num_classes=3)

# ------------------------------------------------
#              Create a session, and run the graph
# ------------------------------------------------
with tf.Session(graph=graph) as sess:
    sess.run(tf.local_variables_initializer())
    sess.run(tf.global_variables_initializer())
    # tf.metrics.mean_iou requires local variables to be initialized
    for i in range(10):
        iou = sess.run(tf_iou)
        print(iou)
