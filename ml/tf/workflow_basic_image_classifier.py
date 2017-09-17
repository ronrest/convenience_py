""" Bare minimum workflow to test an classifier architecture """
from __future__ import print_function, division
import numpy as np
import tensorflow as tf


graph = tf.Graph()
with graph.as_default():
    n_classes = 2
    input_rows,input_cols = [128,128]
    n_channels = 3
    # Initializers
    he_init = tf.contrib.keras.initializers.he_normal()
    relu = tf.nn.relu

    # Placeholders
    tf_X = tf.placeholder(dtype=tf.float32, shape=[None, input_rows, input_cols, n_channels], name="X")
    tf_Y = tf.placeholder(dtype=tf.int32, shape=None, name="Y")
    tf_alpha = tf.placeholder_with_default(0.001, shape=None, name="alpha")
    tf_is_training = tf.placeholder_with_default(False, shape=None)

    # BODY
    x = tf.div(tf_X, 255., name="normalized_input") # Normalize input

    # Conv layers
    x = tf.layers.conv2d(x, filters=8, kernel_size=3,  strides=2, kernel_initializer=he_init, activation=relu)

    ##################
    # INSERT MORE HERE
    ##################

    # Fully connected layers
    x = tf.contrib.layers.flatten(x)
    tf_logits = tf.layers.dense(x, units=n_classes, activation=None, kernel_initializer=he_init)

    # LOSS
    unrolled_logits = tf.reshape(tf_logits, (-1, n_classes))
    unrolled_labels = tf.reshape(tf_Y, (-1,))
    tf_loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=unrolled_logits, labels=unrolled_labels, name="loss"))

    # TRAIN STEP
    tf_optimizer = tf.train.AdamOptimizer(tf_alpha)
    update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS) # allow batchnorm
    with tf.control_dependencies(update_ops):
        tf_train_op = tf_optimizer.minimize(tf_loss)


with tf.Session(graph=graph) as sess:
    n_epochs = 20
    batch_size = 32
    alpha = 0.001
    print_every = 10
    n_samples = len(data["X_train"])               # Num training samples
    n_batches = int(np.ceil(n_samples/batch_size)) # Num batches per epoch

    sess.run(tf.initialize_all_variables())
    # sess.run(tf.global_variables_initializer())

    for epoch in range(1, n_epochs+1):
        print("="*70, "\nEPOCH {}/{})".format(epoch, n_epochs),"\n"+("="*70))

        # Shuffle the data
        permutation = list(np.random.permutation(n_samples))
        data["X_train"] = data["X_train"][permutation]
        data["Y_train"] = data["Y_train"][permutation]

        # Iterate through each mini-batch
        for i in range(n_batches):
            Xbatch = data["X_train"][batch_size*i: batch_size*(i+1)]
            Ybatch = data["Y_train"][batch_size*i: batch_size*(i+1)]

            # TRAIN STEPS
            feed_dict = {tf_X: Xbatch, tf_Y: Ybatch, tf_alpha: alpha, tf_is_training:True}
            loss, _ = sess.run([tf_loss, tf_train_op], feed_dict=feed_dict)

            # Print feedback every so often
            if i%print_every==0:
                print("Batch_loss: {}".format(loss))
