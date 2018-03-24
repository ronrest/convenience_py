# %load_ext autoreload
# %autoreload 2
import torch
from torch import nn
from torch.autograd import Variable

def accuracy(preds, labels):
    return (preds==labels).mean()

def n_correct(preds, labels):
    return (preds==labels).sum()


class ImageClassifier(object):
    def __init__(self, net, n_classes):
        """
        Args:
            net:    A pytorch network module that will computer a forward pass
            n_classes: number of output classes.
        """
        self.history = []
        self.n_classes = n_classes
        self.net = net

        # LOSS FUNCTION
        if n_classes <= 2:
            # Binary classification
            self.loss_func = torch.nn.BCEWithLogitsLoss(weight=None)
        else:
            # multiclass classification
            self.loss_func = torch.nn.CrossEntropyLoss(weight=None) # on logits
            #self.loss_func = torch.nn.NLLLoss(weight=None) #on LogSoftmax() outputs

        # OPTIMIZER
        self.optimizer = None

    def set_optimizer(self, opt_func=torch.optim.Adam, **kwargs):
        """
        Args:
            opt_func:   (function class) the optimization function creator to use
            **kwargs:   The keyword arguments to pass to opt_func
                        eg: lr=1e-3, weight_decay=0
        """
        self.opt_func = opt_func
        self.opt_args = kwargs
        self.optimizer = opt_func(self.net.parameters(), **kwargs)

    def update_lr(self, lr):
        self.opt_args = self.optimizer.defaults
        self.opt_args["lr"] = lr
        self.optimizer = self.opt_func(self.net.parameters(), **self.opt_args)

    def predict_step(self, x, probs=False):
        """ Make predictions on input data in one go.
            Optionally return probabilities
        """
        logits = self.net(Variable(torch.Tensor(x)))
        if probs:
            return torch.nn.functional.softmax(logits, dim=1).data.numpy().astype(np.float32)
        else:
            _, preds = torch.max(logits, dim=1)
            return preds.data.numpy().astype(np.int32)

    def predict(self, x, batch_size=32, probs=False):
        """ Make predictions on a numpy array in batches."""
        n_steps = int(np.ceil(x.shape[0]/float(batch_size)))
        shape = (x.shape[0], self.n_classes)if probs else (x.shape[0],)
        dtype = np.float32 if probs else np.int32
        out = np.zeros(shape, dtype=dtype)

        for i in range(n_steps):
            X_batch = x[i*batch_size:(i+1)*batch_size]
            out[i*batch_size:(i+1)*batch_size] = self.predict_step(X_batch, probs=probs)
        return out

    def predict_gen(self, datagen, n_steps, probs=False):
        """ Make predictions on a data generator."""
        out = []
        for i in range(n_steps):
            X_batch = next(datagen)
            out.append(self.predict_step(X_batch, probs=probs))
        return np.concatenate(out)

    def evaluate_gen(self, datagen, n_steps):
        """ Evaluate by returning (loss, accuracy) """
        original_train_mode = self.net.training
        self.net.eval()
        running_loss = 0.0
        running_correct = 0.0
        running_samples = 0.0
        for i in range(n_steps):
            X_batch, Y_batch = next(datagen)
            # X_batch, Y_batch = preprocess_func(X_batch, Y_batch)
            X_batch, Y_batch = Variable(torch.Tensor(X_batch)), Variable(torch.LongTensor(Y_batch))

            # Run a forward pass of the network
            self.optimizer.zero_grad() # zero the parameter gradients
            logits = self.net(X_batch)
            _, preds = torch.max(logits, dim=1)
            loss = self.loss_func(logits, Y_batch)

            running_loss += loss
            running_correct += n_correct(preds=preds.data.numpy(), labels=Y_batch.data.numpy())
            running_samples += len(Y_batch)

        # Set trining mode back to original setting
        self.net.train(original_train_mode)

        avg_loss = running_loss / (running_samples)
        avg_acc = running_correct / (running_samples)
        return avg_loss, avg_acc

    def fit(self, train_gen, valid_gen, n_epochs, steps_per_epoch, valid_steps=100, print_every=100):
        for epoch in range(n_epochs):
            running_loss = 0.0
            running_correct = 0.0
            running_samples = 0.0
            for i in range(steps_per_epoch):
                # Get the batch of data  and Prerpocess and wrap them in Variable
                X_batch, Y_batch = next(train_gen)
                # X_batch, Y_batch = preprocess_func(X_batch, Y_batch)
                X_batch, Y_batch = Variable(torch.Tensor(X_batch)), Variable(torch.LongTensor(Y_batch))

                # Training steps
                self.optimizer.zero_grad() # zero the parameter gradients
                logits = self.net(X_batch)
                _, preds = torch.max(logits, dim=1)
                loss = self.loss_func(logits, Y_batch)
                loss.backward()
                self.optimizer.step()

                # print statistics
                running_loss += loss.data[0]
                running_correct += n_correct(preds=preds.data.numpy(), labels=Y_batch.data.numpy())
                running_samples += len(Y_batch)
                if i>0 and i % print_every == 0:
                    avg_loss = running_loss / print_every
                    avg_acc = running_correct / (running_samples)
                    running_loss = 0.0
                    running_correct = 0.0
                    running_samples = 0.0
        print('Finished Training')
