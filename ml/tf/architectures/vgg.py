""" ############################################################################
            CODE FOR CREATING VGG 16 ARCHITECTURES
################################################################################
compatible with tensorflow's pretrained snapshots

Based on this code:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/slim/python/slim/nets/vgg.py


USAGE:
    # Note there is no need for specifying arg scopes outside teh functions. The
    # functions create the necessary arg scopes internally.

    # To use just the trunk of VGG
    x = vgg_16_trunk(X, weight_decay=0.0005, name="vgg_16")

    # To use all of the VGG model
    vgg_16(inputs, n_classes=1000, is_training=True, dropout=0.5, weight_decay=0.0005, spatial_squeeze=True, name="vgg_16")

NOTE:
    To use with pretrainied weingts, pass inputs that are 224x224x3
"""
import tensorflow as tf

# USEFUL LAYERS
fc = tf.contrib.layers.fully_connected
conv = tf.contrib.layers.conv2d
# convsep = tf.contrib.layers.separable_conv2d
deconv = tf.contrib.layers.conv2d_transpose
relu = tf.nn.relu
maxpool = tf.contrib.layers.max_pool2d
dropout_layer = tf.layers.dropout
# bn = tf.contrib.layers.batch_norm
# bn_params = {"is_training": self.is_training}
winit = tf.contrib.layers.xavier_initializer()
repeat = tf.contrib.layers.repeat
arg_scope = tf.contrib.framework.arg_scope
l2_regularizer = tf.contrib.layers.l2_regularizer


# ==============================================================================
#                                                               GET_VGG_ARGSCOPE
# ==============================================================================
def get_vgg_argscope(weight_decay=0.0005):
    """ Gets the arg scope needed for VGG.
    Args:
        weight_decay: The l2 regularization coefficient.
    Returns:
        An arg_scope with the default arguments for layers in VGG .
    """
    with tf.contrib.framework.arg_scope(
        [conv],
        activation_fn=tf.nn.relu,
        weights_regularizer=l2_regularizer(weight_decay),
        biases_initializer=tf.zeros_initializer()):
        with tf.contrib.framework.arg_scope([conv], padding='SAME') as scope:
                return scope



# ==============================================================================
#                                                                   VGG16_TRUNK
# ==============================================================================
def vgg16_trunk(inputs, weight_decay=0.0005, name="vgg_16"):
    with tf.variable_scope(name, name):
        return _vgg16_trunk_ops(inputs, weight_decay=weight_decay)

def _vgg16_trunk_ops(inputs, weight_decay=0.0005):
    """ VGG layers before the fully connected layers """
    with tf.contrib.framework.arg_scope(get_vgg_argscope(weight_decay=weight_decay)):
        x = repeat(inputs, 2, conv, num_outputs=64, kernel_size=3, scope='conv1')
        x = maxpool(x, kernel_size=2, scope='pool1')
        x = repeat(x, 2, conv, num_outputs=128, kernel_size=3, scope='conv2')
        x = maxpool(x, kernel_size=2, scope='pool2')
        x = repeat(x, 3, conv, num_outputs=256, kernel_size=3, scope='conv3')
        x = maxpool(x, kernel_size=2, scope='pool3')
        x = repeat(x, 3, conv, num_outputs=512, kernel_size=3, scope='conv4')
        x = maxpool(x, kernel_size=2, scope='pool4')
        x = repeat(x, 3, conv, num_outputs=512, kernel_size=3, scope='conv5')
        x = maxpool(x, kernel_size=2, scope='pool5')
        return x


# ==============================================================================
#                                                                          VGG16
# ==============================================================================
def vgg16(inputs, n_classes=1000, is_training=True, dropout=0.5, weight_decay=0.0005, spatial_squeeze=True, name="vgg_16"):
    with tf.variable_scope(name, name):
        # Trunk of convolutional layers
        x = _vgg_16_trunk_ops(inputs, weight_decay=weight_decay)

        # "Fully connected" layers
        # Use conv2d instead of fully_connected layers.
        with tf.contrib.framework.arg_scope(get_vgg_argscope(weight_decay=weight_decay)):
            x = conv(x, num_outputs=4096, kernel_size=7, padding='VALID', scope='fc6')
            x = dropout_layer(x, dropout, is_training=is_training, scope='dropout6')
            x = conv(x, num_outputs=4096, kernel_size=1, scope='fc7')
            x = dropout_layer(x, dropout, is_training=is_training, scope='dropout7')
            x = conv(x, num_outputs=n_classes, kernel_size=1, activation_fn=None, normalizer_fn=None, scope='fc8')
            if spatial_squeeze:
                x = array_ops.squeeze(x, [1, 2], name='fc8/squeezed')
        return x
