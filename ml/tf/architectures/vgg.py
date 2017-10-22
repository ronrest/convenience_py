""" ############################################################################
            CODE FOR CREATING VGG 16 ARCHITECTURES
################################################################################
compatible with tensorflow's pretrained snapshots

Based on this code:
    https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/slim/python/slim/nets/vgg.py
But allows for the inclusion of batchnorm for each convolution layer.

USAGE:
    # Note there is no need for specifying arg scopes outside the functions. The
    # functions create the necessary arg scopes internally.

    # To use just the trunk of VGG
    x = vgg_16_trunk(X, weight_decay=0.0005, name="vgg_16")

    # To use all of the VGG model
    vgg_16(inputs, n_classes=1000, is_training=True, dropout=0.5, weight_decay=0.0005, spatial_squeeze=True, name="vgg_16")

NOTES FOR WHEN USING PRETRAINED WEIGHTS:
    # TODO: Add link to tensorflows pretrained weights
    - If running the entire VGG model up to fully connected layers, eg for
      classification, then pass inputs that are 224x224x3.
    - If only using the convolution trunk layers, then the inputs should
      be a minimum size of 32x32 to accomodate 5 downsamples that get
      halved each time.
    - NOTE: that the original model, and the pretrained weights, do not include
      batchnorm layers. But it can be useful to have them included when
      performing transfer learning. It just means that the parameters in the
      batchnorm layers will be trained from scratch.

    WEIGHTS TO INCLUDE/EXCLUDE FROM PRETRAINED SNAPSHOT
    For full VGG:
        pretrained_include = ["vgg_16"]
        pretrained_exclude = None

    For full VGG with batchnorm:
        pretrained_include = ["vgg_16"]
        pretrained_exclude = [".*BatchNorm"]

    For VGG trunk:
        pretrained_include = ["vgg_16"]
        pretrained_exclude = ["vgg_16/fc6", "vgg_16/fc7", "vgg_16/fc8"]

    For VGG trunk with batchnorm:
        pretrained_include = ["vgg_16"]
        pretrained_exclude = ["vgg_16/fc6", "vgg_16/fc7", "vgg_16/fc8", ".*BatchNorm"]


PRETRAINED WEIGHTS
                   ACCURACY
    MODEL       TOP 1   TOP 5
    VGG 16	    71.5	89.8
    VGG 19	    71.1	89.8

    VGG 16
    PAPER: http://arxiv.org/abs/1409.1556.pdf
    WEIGHTS: http://download.tensorflow.org/models/vgg_16_2016_08_28.tar.gz
    FROZEN :

    # TODO: Add VGG 19 model to code
    # VGG 19
    # PAPER: http://arxiv.org/abs/1409.1556.pdf
    # WEIGHTS: http://download.tensorflow.org/models/mobilenet_v1_1.0_224_2017_06_14.tar.gz
    # FROZEN :
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
batchnorm = tf.contrib.layers.batch_norm
# bn_params = {"is_training": is_training}
winit = tf.contrib.layers.xavier_initializer()
l2_regularizer = tf.contrib.layers.l2_regularizer
repeat = tf.contrib.layers.repeat
arg_scope = tf.contrib.framework.arg_scope

# ==============================================================================
#                                                               GET_VGG_ARGSCOPE
# ==============================================================================
def get_vgg_argscope(weight_decay=0.0005, use_batch_norm=False, is_training=False):
    """ Gets the arg scope needed for VGG.
    Args:
        weight_decay: The l2 regularization coefficient.
    Returns:
        An arg_scope with the default arguments for layers in VGG .
    """
    with tf.contrib.framework.arg_scope(
        [conv],
        activation_fn=tf.nn.relu,
        normalizer_fn = batchnorm if use_batch_norm else None,
        normalizer_params = {"is_training": is_training},
        weights_regularizer=l2_regularizer(weight_decay),
        biases_initializer=tf.zeros_initializer(),
        trainable = True):
        with tf.contrib.framework.arg_scope([conv], padding='SAME') as scope:
                return scope


# ==============================================================================
#                                                                   VGG16_TRUNK
# ==============================================================================
def vgg16_trunk(inputs, weight_decay=0.0005, use_batch_norm=False, is_training=False, name="vgg_16"):
    with tf.variable_scope(name, name):
        return _vgg16_trunk_ops(inputs, weight_decay=weight_decay, use_batch_norm=use_batch_norm, is_training=is_training)

def _vgg16_trunk_ops(inputs, weight_decay=0.0005, use_batch_norm=False, is_training=False):
    """ VGG layers before the fully connected layers """
    with tf.contrib.framework.arg_scope(get_vgg_argscope(
            weight_decay=weight_decay,
            use_batch_norm=use_batch_norm,
            is_training=is_training)):
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
def vgg16(inputs, n_classes=1000, use_batch_norm=False, is_training=True, dropout=0.5, weight_decay=0.0005, spatial_squeeze=True, name="vgg_16"):
    with tf.variable_scope(name, name):
        # Trunk of convolutional layers
        x = _vgg16_trunk_ops(inputs, weight_decay=weight_decay, use_batch_norm=use_batch_norm, is_training=is_training)

        # "Fully connected" layers
        # Use conv2d instead of fully_connected layers.
        with tf.contrib.framework.arg_scope(get_vgg_argscope(
                weight_decay=weight_decay,
                use_batch_norm=use_batch_norm,
                is_training=is_training)):
            x = conv(x, num_outputs=4096, kernel_size=7, padding='VALID', scope='fc6')
            x = dropout_layer(x, dropout, training=is_training, name='dropout6')
            x = conv(x, num_outputs=4096, kernel_size=1, scope='fc7')
            x = dropout_layer(x, dropout, training=is_training, name='dropout7')
            x = conv(x, num_outputs=n_classes, kernel_size=1, activation_fn=None, normalizer_fn=None, scope='fc8')
            if spatial_squeeze:
                x = tf.squeeze(x, [1, 2], name='fc8/squeezed')
        return x
