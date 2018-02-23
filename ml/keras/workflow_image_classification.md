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

### Evaluation Metrics
[Evaluation Metrics Docs](https://keras.io/metrics/)

```py
from keras import metrics

binary_accuracy(y_true, y_pred)
categorical_accuracy(y_true, y_pred)
sparse_categorical_accuracy(y_true, y_pred)
top_k_categorical_accuracy(y_true, y_pred, k=5)
sparse_top_k_categorical_accuracy(y_true, y_pred, k=5)
```

#### Custom Metrics

[Custom Metrics](https://keras.io/metrics/#custom-metrics)



## Train Using Generator

[Data Generator Docs](https://keras.io/preprocessing/image/)

```py
from keras.preprocessing.image import ImageDataGenerator

# SETTINGS
train_dir = "data/train"
valid_dir = "data/valid"
test_dir = "data/test"

n_data = SOMETHING
n_valid = SOMETHING
batch_size = 32
steps_per_epoch = n_data // batch_size
steps_per_valid = n_valid // batch_size

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.3,
    channel_shift_range=0.0,
    fill_mode='nearest', # "constant", "nearest", "reflect" or "wrap"
    horizontal_flip=True,
    vertical_flip=True,
    zca_whitening=False,
    preprocessing_function=None,
    )

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=img_shape[:2],
        batch_size=batch_size,
        classes=id2class, # actually mapping class id to dir name
        class_mode='sparse')

validation_generator = test_datagen.flow_from_directory(
        valid_dir,
        target_size=img_shape[:2],
        batch_size=batch_size,
        classes=id2class, # actually mapping class id to dir name
        class_mode='sparse')


history = model.fit_generator(
      train_generator,
      steps_per_epoch=steps_per_epoch,
      epochs=10,
      validation_data=validation_generator,
      validation_steps=steps_per_valid,
      verbose=2, # Verbosity mode, 0, 1, or 2.
      callbacks=None,
      validation_data=None, # A generator or a tuple (x, y)
      class_weight=None,
      max_q_size=10,  # Maximum size for the generator queue
      workers=1,      # Maximum number of processes to spin up
      )

plot_history(history, metrics=["loss", "acc"], use_valid=True, savedir=None, show=True)


# Evaluate
# loss, acc = model.evaluate_generator(test_generator, test_steps, max_q_size=10, workers=1)

# Predict
# model.predict_generator(pred_generator, steps, max_q_size=10, workers=1, verbose=0)


```

- **Class Mode**
    - Determines the type of label arrays that are returned
    - `"categorical"` (default)  One-hot vector labels
    - `"binary"` integer binary labels (0,1)
    - `"sparse"` Integer class id labels
    - `"input"` images identical to input images (for use with autoencoders)
    - `None` no labels are returned


