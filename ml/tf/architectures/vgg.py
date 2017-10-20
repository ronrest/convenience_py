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
#                                                                  GET_VGG_SCOPE
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


