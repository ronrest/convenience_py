# MNIST Dataset

```py
import os
import numpy as np
from keras.datasets import mnist

n_valid = 10000
data_dir = "/home/ronny/TEMP/MNIST/keras"
data_file = os.path.join(data_dir, "mnist.npz")


data = {}
(data["X_train"], data["Y_train"]), (data["X_test"], data["Y_test"]) =  mnist.load_data(data_file)

# Add the color channel axis
data["X_train"] = np.expand_dims(data["X_train"], axis=3)
data["X_test"] = np.expand_dims(data["X_test"], axis=3)

# PREPROCESS THE IMAGES
# Scale to between 0-1
data["X_train"] = data["X_train"].astype(np.float32) / 255.
data["X_test"] = data["X_test"].astype(np.float32) / 255.

# Create Validation Split
data["X_valid"] = data["X_train"][:n_valid]
data["Y_valid"] = data["Y_train"][:n_valid]
data["X_train"] = data["X_train"][n_valid:]
data["Y_train"] = data["Y_train"][n_valid:]

# Print Shapes
print("X_train shape: ", data["X_train"].shape)
print("X_valid shape: ", data["X_valid"].shape)
print("X_test shape: ", data["X_test"].shape)
```
