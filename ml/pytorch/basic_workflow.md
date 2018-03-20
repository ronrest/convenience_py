# Pytorch Basic Workflow

## Preprocessing

Note that images in Pytorch are expected to be in `NCHW` format.

```py
def nhwc2nchw(x):
    """ Given an array of images as NHWC it converts to NCHW format """
    return np.moveaxis(x, [0,1,2,3], [0,2,3,1])
```

## Data

```py
# DATA
train_gen = data_generator(data["X_train"], data["Y_train"], preprocess_func=preprocess_images, shuffle=True)
valid_gen = data_generator(data["X_valid"], data["Y_valid"], preprocess_func=preprocess_images, shuffle=False)
```


## Define network

```py
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F

# SETTINGS
n_classes = 10
img_shape = [28,28,1] # height, width, channels
height, width, channels = img_shape

# EVALUATION METRICS
def accuracy(preds, labels):
    return (preds==labels).mean()

def n_correct(preds, labels):
    return (preds==labels).sum()

class Flatten(nn.Module):
    def forward(self, input):
        return input.view(input.size(0), -1)


# NETWORK SETTINGS
n_downsamples = 2
final_conv_channels = 32
n_flattened = ((np.array(img_shape[:2]) * (1./(2**n_downsamples))).astype(np.int32)).prod() * final_conv_channels

# NETWORK
net = nn.Sequential(
          nn.Conv2d(channels,16,3, padding=1),
          nn.ReLU(),
          nn.MaxPool2d(kernel_size=2, stride=2, padding=0),
          nn.Conv2d(16,final_conv_channels,3, padding=1),
          nn.ReLU(),
          nn.MaxPool2d(kernel_size=2, stride=2, padding=0),
          Flatten(),
          nn.Linear(n_flattened, 128),
          nn.ReLU(),
          nn.Linear(128, n_classes),
        )

# NAMED LAYERS
# net = nn.Sequential(OrderedDict([
#           ('conv1', nn.Conv2d(1,20,5)),
#           ('relu1', nn.ReLU()),
#           ('conv2', nn.Conv2d(20,64,5)),
#           ('relu2', nn.ReLU())
#         ]))
#


# LOSS FUNC
loss_func = torch.nn.CrossEntropyLoss(weight=None)  # Loss to be used on raw logits
# loss_func = torch.nn.NLLLoss(weight=None)  # Loss to be used on outputs of LogSoftmax() layer
#torch.nn.BCEWithLogitsLoss(weight=None)     # For binary classification from raw logits

# OPTIMIZER
optimizer = torch.optim.Adam(net.parameters(), lr=0.001, betas=(0.9, 0.999), eps=1e-08, weight_decay=0)
# optimizer = torch.optim.RMSprop(net.parameters(), lr=0.01, alpha=0.99, eps=1e-08, weight_decay=0, momentum=0)
# optimizer = torch.optim.SGD(net.parameters(), lr=0.001, momentum=0, dampening=0, weight_decay=0, nesterov=False)

# TRAIN loop
n_epochs = 2
steps_per_epoch = 500
print_every = 100
for epoch in range(n_epochs):
    running_loss = 0.0
    running_correct = 0.0
    for i in range(steps_per_epoch):
        # Get the batch of data  and Prerpocess and wrap them in Variable
        X_batch, Y_batch = next(train_gen)
        X_batch, Y_batch = Variable(torch.Tensor(X_batch)), Variable(torch.LongTensor(Y_batch))

        # Training steps
        optimizer.zero_grad() # zero the parameter gradients
        logits = net(X_batch)
        _, preds = torch.max(logits, dim=1)
        loss = loss_func(logits, Y_batch)
        loss.backward()
        optimizer.step()

        # print statistics
        running_loss += loss.data[0]
        running_correct += n_correct(preds=preds.data.numpy(), labels=Y_batch.data.numpy())
        if i>0 and i % print_every == 0:
            avg_loss = running_loss / print_every
            avg_acc = running_correct / (print_every*batch_size)

            print("{e} - {s} LOSS: {l} ACC:{a}".format(e=epoch,s=i,l=avg_loss, a=avg_acc))
            running_loss = 0.0
            running_correct = 0.0
print('Finished Training')

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


## GPU

```py
# Move all parameters to GPU
# NOTE:must be called before constructing optimizer.
net.cuda()
```

## Train/Evaluation mode

```py
net.train()      # set to train mode
train(mode=True) # set to train mode

train(mode=False) # set to evaluation mode
net.eval()        # set to evaluation mode
```



## Schedulers for adjusting learning rate

http://pytorch.org/docs/0.3.1/optim.html#how-to-adjust-learning-rate


## Get modules that make up the network
```py
m = model.net.modules()                     # modules of a net
m = model.net.named_modules()               # named modules
m = model.net.named_modules(prefix="mynet") # named modules but adding a prefix to the returned names
```

## Gradients

```py
net.zero_grad()  # zero out the gradients of a model.
```
