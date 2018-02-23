# Image Classification Workflow

```py
from keras import layers
from keras import models
from keras import optimizers

def create_model_a(input_shape=(150,150,3), n_classes=10):
    model = models.Sequential([
        layers.Conv2D(32, (3,3), activation="relu", padding="same", name="conv1", input_shape=input_shape),
        layers.MaxPooling2D((2,2), strides=2, name="maxpool1"),
        layers.Conv2D(64, (3,3), activation="relu", padding="same", name="conv2"),
        layers.MaxPooling2D((2,2), strides=2, name="maxpool2"),

        # FC layers
        layers.Flatten(),
        layers.Dense(256, activation="relu"),
        # layers.Dense(1, activation="sigmoid"), # for binary classification
        layers.Dense(n_classes, activation="softmax"),
    ])
    return model

# Create model
img_shape = (64,64,3)
model = create_model_a(input_shape=img_shape, n_classes=10)
model.summary()

# Compile
model.compile(optimizer=optimizers.RMSprop(lr=1e-4),
            loss="sparse_categorical_crossentropy",#for class id labels
            # loss="binary_crossentropy", # For binary classification
            # loss="categorical_crossentropy", #for one hot vector labels
            metrics=["accuracy"])


# Train
history = model.fit(data["X_train"], data["Y_train"],
                    batch_size=32,
                    epochs=10,
                    validation_data=[data["X_valid"], data["Y_valid"]]
                   )
plot_history(history, metrics=["loss", "acc"], use_valid=True, savedir=None, show=True)

# Evaluate on Test set
loss, accuracy = model.evaluate(data["X_test"], data["Y_test"], batch_size=32)
```

### Common Losses

[Losses Docs](https://keras.io/losses/)

- `"binary_crossentropy"` (requires integer 1 or 0 labels)
- `"sparse_categorical_crossentropy"` (requires integer category id labels)
- `"categorical_crossentropy"` (required one hot vector labels)



### Common Optimizers

[Optimizers Docs](https://keras.io/optimizers/)

**As string**

- `"rmsprop"`
- `"adam"`

**As object**

```py
from keras import optimizers

# SGD
optimizers.SGD(lr=0.01, momentum=0.0, decay=0.0, nesterov=False)

# RMSProp optimizer. Usually a good choice for RNNs.
optimizers.RMSprop(lr=0.001, rho=0.9, epsilon=1e-08, decay=0.0)

# Adam. Default parameters based on the original paper.
optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
```
