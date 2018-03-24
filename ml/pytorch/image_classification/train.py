%load_ext autoreload
%autoreload 2

from data_process import np
from data_process import pickle2obj, create_valid_split
from data_process import data_generator, preprocess_images

# SETTINGS
pickle_file = "/home/ronny/TEMP/MNIST/pickled_data/mnist.pickle"
n_valid = 10000

# ##############################################################################
#                                     DATA
# ##############################################################################
# Load data and create validation split
data = pickle2obj(pickle_file)
create_valid_split(data, n_valid=10000)

# Printout of shapes
for key in data.keys():
    print("{} = {}".format(key, data[key].shape))

img_dims = data["X_train"].shape[1:3]
img_shape = data["X_train"].shape[1:4]

train_gen = data_generator(data["X_train"], data["Y_train"], preprocess_func=preprocess_images, shuffle=True)
valid_gen = data_generator(data["X_valid"], data["Y_valid"], preprocess_func=preprocess_images, shuffle=True)


# ##############################################################################
#                                  MODEL
# ##############################################################################
from image_classifier import ImageClassifier
from architectures import torch, Variable
from architectures import BasicNet
net = BasicNet(img_shape=[28,28,1], n_classes=10)
model = ImageClassifier(net=net, n_classes=10)
model.set_optimizer(lr=1e-3)
model.fit(train_gen=train_gen, valid_gen=valid_gen, n_epochs=2, steps_per_epoch=500)

# TODO: Save and load model
# Save model
