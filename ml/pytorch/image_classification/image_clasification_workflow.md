# Pytorch Image Classification WOrkflow


## Data Generators

```py

```


## The Data

```py


data["X_train"].shape

img_dims = data["X_train"].shape[1:3]



```


## Define network

```py

# Create Model
img_shape = data["X_train"].shape[1:]
model = Net(img_shape=img_shape, n_classes=10)


# LOSS FUNC
loss_func = torch.nn.CrossEntropyLoss(weight=None)  # Loss to be used on raw logits
# loss_func = torch.nn.NLLLoss(weight=None)  # Loss to be used on outputs of LogSoftmax() layer
#torch.nn.BCEWithLogitsLoss(weight=None)     # For binary classification from raw logits

# OPTIMIZER
optimizer = torch.optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
# optimizer = torch.optim.RMSprop(model.parameters(), lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0)
# optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0, dampening=0, weight_decay=0, nesterov=False)


```


## Losses and Optimizers

- [loss functions](http://pytorch.org/docs/0.3.1/nn.html#loss-functions)
- [Optimizers](http://pytorch.org/docs/0.3.1/optim.html)


**NOTE FOR GPUS:** If you need to move a model to GPU via .cuda(), please do so before constructing optimizers for it.

Other Losses:

- `torch.nn.BCEWithLogitsLoss(weight=None)` -  For binary classification from raw logits
- `torch.nn.BCELoss(weight=None)` - For binary classification on outputs of sigmoid function.
- `torch.nn.NLLLoss2d(weight=None)` - NLL applied to 2D images
- `torch.nn.MSELoss()`

Advanced Per-layer optimization parameters, eg different learning rates for differernt portions of the model.

```py
optimizer = torch.optim.SGD(
            [{'params': model.base.parameters()},
             {'params': model.classifier.parameters(), 'lr': 1e-3}
            ], lr=1e-2, momentum=0.9)
```


## Training Loop:

```py
# def train_model(model, loss_func, optimizer, lr):








batch_size = 32
train_gen = np_datagen(data["X_train"], data["Y_train"], batch_size=batch_size, shuffle=False)
n_epochs = 2
n_train_samples = data["X_train"].shape[0]
steps_per_epoch = n_train_samples // batch_size
print_every = 100 # print out feed back every this number of steps
preprocess_func = preprocess_images

# train model
for epoch in range(n_epochs):  # loop over the dataset multiple times
    running_loss = 0.0
    running_correct = 0.0
    for i in range(steps_per_epoch):

        # Get the batch of data  and Prerpocess and wrap them in Variable
        X_batch, Y_batch = next(train_gen)
        X_batch, Y_batch = preprocess_func(X_batch, Y_batch)
        X_batch, Y_batch = Variable(torch.Tensor(X_batch)), Variable(torch.LongTensor(Y_batch))

        # Training steps
        optimizer.zero_grad() # zero the parameter gradients
        probs = model(X_batch)
        _, preds = torch.argmax(probs, dim=1)
        loss = loss_func(probs, Y_batch)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.data[0]
        running_correct += n_correct(preds=preds.data.numpy(), labels=Y_batch.data.numpy())
        if i>0 and i % print_every == 0:
            avg_loss = running_loss / print_every
            avg_acc = running_correct / (print_every*batch_size)
            print("{e} - {s} LOSS: {l} ACC: {a}".format(e=epoch,s=i,l=avg_loss, a=avg_acc))
            running_loss = 0.0
            running_correct = 0.0
print('Finished Training')






(preds == Y_batch).data.numpy().mean()


_, argmax = torch.max(v, dim=1)

Y_batch











```

optimizer.zero_grad()   # zero the gradient buffers

preds = model(input)
loss = criterion(output, target)
loss.backward()
optimizer.step()    # Does the update



loss = loss_func(preds, Y_batch)

```



## Train

```py



# model = Net(img_shape=img_shape, n_classes=10)*/*/
# Learnable parameters
# list(model.parameters())

X_batch = data["X_train"][:32]
Y_batch = data["Y_train"][:32]

model.zero_grad() # Zero the gradient buffers of all parameters
out = model(X_batch) # Forward Pass






net.parameters()
params = list(net.parameters())

print(len(params))
print(params[0].size())  # conv1's .weight

from torch import nn

c = nn.Conv2d(8, 16, 3, stride=1, padding=1, dilation=2, bias=True)
dir(c)

c.out_channels
c.kernel_size[0] * c.kernel_size[0] * c.out_channels


c.weight.shape




```



## Schedulers for adjusting learning rate

http://pytorch.org/docs/0.3.1/optim.html#how-to-adjust-learning-rate
