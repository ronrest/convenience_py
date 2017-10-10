from __future__ import print_function, division, unicode_literals
import numpy as np
import tensorflow as tf

from model_base import ImageClassificationModel
from data_processing import prepare_data

__author__ = "Ronny Restrepo"
__copyright__ = "Copyright 2017, Ronny Restrepo"
__credits__ = ["Ronny Restrepo"]
__license__ = "Apache License"
__version__ = "2.0"


# ##############################################################################
#                                                                       MY MODEL
# ##############################################################################
class MyModel(ImageClassificationModel):
    def __init__(self, name, img_shape, n_channels=3, n_classes=10, dynamic=False, l2=None, best_evals_metric="valid_acc"):
        super().__init__(name=name, img_shape=img_shape, n_channels=n_channels, n_classes=n_classes, dynamic=dynamic, l2=l2, best_evals_metric=best_evals_metric)

    def create_body_ops(self):
        with tf.variable_scope("preprocess"):
            x = tf.div(self.X, 255.)

        with tf.contrib.framework.arg_scope(
            [tf.contrib.layers.conv2d, tf.contrib.layers.fully_connected],
            activation_fn=tf.nn.relu,
            normalizer_fn=tf.contrib.layers.batch_norm,
            normalizer_params={"is_training": self.is_training}
            ):
            x = tf.contrib.layers.conv2d(x, num_outputs=8, kernel_size=3, stride=1)
            x = tf.layers.dropout(x, rate=self.dropout)
            x = tf.contrib.layers.conv2d(x, num_outputs=8, kernel_size=3, stride=2)
            x = tf.layers.dropout(x, rate=self.dropout)

            x = tf.contrib.layers.conv2d(x, num_outputs=16, kernel_size=3, stride=1)
            x = tf.layers.dropout(x, rate=self.dropout)
            x = tf.contrib.layers.conv2d(x, num_outputs=16, kernel_size=3, stride=2)
            x = tf.layers.dropout(x, rate=self.dropout)

            x = tf.contrib.layers.conv2d(x, num_outputs=32, kernel_size=3, stride=1)
            x = tf.layers.dropout(x, rate=self.dropout)
            x = tf.contrib.layers.conv2d(x, num_outputs=32, kernel_size=3, stride=2)
            x = tf.layers.dropout(x, rate=self.dropout)

            x = tf.contrib.layers.flatten(x)
            self.logits = tf.contrib.layers.fully_connected(x, num_outputs=self.n_classes, normalizer_fn=None, activation_fn=None, scope="logits")


# ##############################################################################
#                                                                   AUGMENTATION
# ##############################################################################
from image_processing import create_augmentation_func

aug_func = create_augmentation_func(
    shadow=(0.01, 0.8),
    shadow_file="shadow_pattern.jpg",
    shadow_crop_range=(0.02, 0.5),
    rotate=30,
    crop=0.66,
    lr_flip=False,
    tb_flip=False,
    brightness=(0.5, 0.4, 4),
    contrast=(0.5, 0.3, 5),
    blur=1,
    noise=10
    )

# # Visualize samples of augmentations
# from viz import viz_sample_augmentations
# viz_sample_augmentations(data["X_train"], aug_func=aug_func, n_images=10, n_per_image=5, saveto=None)


# ##############################################################################
#                                                                           MAIN
# ##############################################################################
if __name__ == '__main__':
    # SETTINGS
    n_valid = 1024
    data_file = "/path/to/data.pickle"

    data = prepare_data(data_file, valid_from_train=True, n_valid=n_valid, max_data=None)

    model = MyModel("delete2", img_shape=[28,28], n_channels=1, n_classes=10)
    model.create_graph()
    model.train(data, n_epochs=5, print_every=300, dropout=0.2, aug_func=aug_func)
