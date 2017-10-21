# ==============================================================================
#                                                               INCEPTIONV3TRUNK
# ==============================================================================
def inceptionV3trunk():
    # TODO: include docstring with info about include and exclude scopes
    with tf.name_scope("preprocess") as scope:
        x = tf.div(self.X, 255, name="rescaled_inputs")

    is_training = self.is_training
    winit = tf.contrib.layers.xavier_initializer()
    relu = tf.nn.relu
    n_classes = self.n_classes
    conv2d = tf.contrib.layers.conv2d
    deconv = tf.contrib.layers.conv2d_transpose
    batchnorm = tf.contrib.layers.batch_norm
    drop = 0.5

    # INCEPTION TRUNK
    arg_scope = tf.contrib.slim.nets.inception.inception_v3_arg_scope
    # architecture_func = tf.contrib.slim.nets.inception.inception_v3_base
    with tf.contrib.framework.arg_scope(arg_scope()):
        with tf.variable_scope("InceptionV3", 'InceptionV3') as scope:
            with tf.contrib.framework.arg_scope([tf.contrib.layers.batch_norm, tf.contrib.layers.dropout], is_training=self.is_training):
                mixed_7c, end_points = tf.contrib.slim.nets.inception.inception_v3_base(
                      inputs=x,
                      final_endpoint='Mixed_7c',
                      scope=scope)
    # INSERT MORE HERE
