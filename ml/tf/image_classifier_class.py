""""
Contains the ClassifierModel class. Which contains all the
boilerplate code necessary to Create a tensorlfow graph, and training
operations.
"""
import tensorflow as tf
import numpy as np
import os
import shutil
import time
import pickle

# DEPENDS ON train_curves, random_transformations, ....
from viz import train_curves
from image_processing import random_transformations
from dynamic_data import load_batch_of_images, maybe_make_pardir, pickle2obj, obj2pickle
from dynamic_data import str2file

# ==============================================================================
#                                                                    PRETTY_TIME
# ==============================================================================
def pretty_time(t):
    """ Given a time in seconds, returns a string formatted as "HH:MM:SS" """
    t = int(t)
    H, r = divmod(t, 3600)
    M, S = divmod(r, 60)
    return "{:02n}:{:02n}:{:02n}".format(H,M,S)


# ##############################################################################
#                                                          CLASSIFIER MODEL BASE
# ##############################################################################
# Depends on load_batch_of_images()
class ClassifierModel(object):
    def __init__(self, name, img_shape, n_channels=3, n_classes=10, dynamic=False, l2=None, best_evals_metric="valid_acc"):
        """ Initializes a Classifier Class
            n_classes: (int)
            dynamic: (bool)(default=False)
                     Load the images dynamically?
                     If the data just contains paths to image files, and not
                     the images themselves, then set to True.

            If logits_func is None, then you should create a new class that inherits
            from this one that overides `self.body()`
        """
        self.n_classes = n_classes
        self.batch_size = 4
        self.global_epoch = 0
        self.best_evals_metric = best_evals_metric
        self.l2 = l2

        self.model_dir = os.path.join("models", name)
        self.snapshot_file = os.path.join(self.model_dir, "snapshots", "snapshot.chk")
        self.best_snapshot_file = os.path.join(self.model_dir, "snapshots_best", "snapshot.chk")
        self.evals_file = os.path.join(self.model_dir, "evals.pickle")
        self.best_score_file = os.path.join(self.model_dir, "best_score.txt")
        self.train_status_file = os.path.join(self.model_dir, "train_status.txt")

        self.tensorboard_dir = os.path.join(self.model_dir, "tensorboard")

        # directories to create
        self.dir_structure = [
            self.model_dir,
            os.path.join(self.model_dir, "snapshots"),
            os.path.join(self.model_dir, "snapshots_best"),
            os.path.join(self.model_dir, "tensorboard"),
            ]

        self.create_directory_structure()
        self.initialize_evals_dict(["train_acc", "valid_acc", "train_loss", "valid_loss", "global_epoch"])
        self.global_epoch = self.evals["global_epoch"]

        self.img_shape = img_shape
        self.img_width, self.img_height = img_shape
        self.n_channels = n_channels
        self.n_classes = n_classes
        self.dynamic = dynamic
        self.create_graph()

    def create_graph(self):
        self.graph = tf.Graph()
        with self.graph.as_default():
            self.create_input_ops()
            self.create_body_ops()
            self.create_loss_ops()
            self.create_optimization_ops()
            self.create_saver_ops()
            self.create_tensorboard_ops()

    def create_input_ops(self):
        # TODO: This handling of L2 is ugly, fix it.
        if self.l2 is None:
            l2_scale = 0.0
        else:
            l2_scale = l2

        with tf.variable_scope("inputs"):
            self.X = tf.placeholder(tf.float32, shape=(None, self.img_height, self.img_width, self.n_channels), name="X") # [batch, rows, cols, chanels]
            self.Y = tf.placeholder(tf.int32, shape=[None], name="Y") # [batch]
            self.alpha = tf.placeholder_with_default(0.001, shape=None, name="alpha")
            self.is_training = tf.placeholder_with_default(False, shape=(), name="is_training")
            self.l2_scale = tf.placeholder_with_default(l2_scale, shape=(), name="l2_scale")
            self.dropout = tf.placeholder_with_default(0.0, shape=None, name="dropout")


    def create_body_ops(self):
        """Override this method in child classes.
           must return pre-activation logits of the output layer

           Ops to make use of:
               self.is_training
               self.X
               self.Y
               self.alpha
               self.dropout
               self.l2_scale
               self.l2
               self.n_classes
        """
        # TODO: This handling of L2 is ugly, fix it.
        if self.l2 is None:
            l2_scale = 0.0
        else:
            l2_scale = l2

        # TODO: Use arg_scopes instead of having to use these if then statements for regularization
        if self.l2_scale > 0.0:
            self.regularizer = tf.contrib.layers.l2_regularizer(scale=self.l2_scale)
        else:
            self.regularizer = None

        # default body graph. Override this.
        # print(self.X.name, self.X.shape.as_list())
        x = tf.contrib.layers.flatten(X)
        self.logits = tf.contrib.layers.fully_connected(x, self.n_classes, activation_fn=None, name="logits")
        self.preds = tf.argmax(self.logits, axis=1, name="preds")


    def create_loss_ops(self):
        # LOSS - Sums all losses even Regularization losses automatically
        with tf.variable_scope('loss') as scope:
            unrolled_logits = tf.reshape(self.logits, (-1, self.n_classes))
            unrolled_labels = tf.reshape(self.Y, (-1,))
            tf.losses.sparse_softmax_cross_entropy(labels=unrolled_labels, logits=unrolled_logits, reduction="weighted_sum_by_nonzero_weights")
            self.loss = tf.losses.get_total_loss()

    def create_optimization_ops(self):
        # OPTIMIZATION - Also updates batchnorm operations automatically
        with tf.variable_scope('opt') as scope:
            self.optimizer = tf.train.AdamOptimizer(self.alpha, name="optimizer")
            update_ops = tf.get_collection(tf.GraphKeys.UPDATE_OPS) # allow batchnorm
            with tf.control_dependencies(update_ops):
                self.train_op = self.optimizer.minimize(self.loss, name="train_op")

    def create_tensorboard_ops(self):
        # # TENSORBOARD
        # self.summary_writer = tf.summary.FileWriter(os.path.join(self.model_dir, "tensorboard"), graph=self.graph)
        # self.summary_op = tf.summary.scalar(name="dummy", tensor=4)

        # TENSORBOARD - To visialize the architecture
        with tf.variable_scope('tensorboard') as scope:
            self.summary_writer = tf.summary.FileWriter(self.tensorboard_dir, graph=self.graph)
            self.dummy_summary = tf.summary.scalar(name="dummy", tensor=1)
            #self.summary_op = tf.summary.merge_all()

    def create_saver_ops(self):
        """ Create operations to save/restore model weights """
        with tf.device('/cpu:0'): # prevent more than one thread doing file I/O
            # # Inception Saver
            #  excluded_weights = ["InceptionV3/AuxLogits", "InceptionV3/Logits"]
            # trunk_vars = tf.contrib.framework.get_variables_to_restore(include=["InceptionV3"], exclude=excluded_weights)
            # self.trunk_saver = tf.train.Saver(trunk_vars, name="trunk_saver")

            # Main Saver
            main_vars = tf.contrib.framework.get_variables_to_restore(exclude=None)
            self.saver = tf.train.Saver(main_vars, name="saver")
            # best_snapshot_file

    def create_directory_structure(self):
        """ Ensure the necessary directory structure exists for saving this model """
        for dir in self.dir_structure:
            if not os.path.exists(dir):
                os.makedirs(dir)

    def initialize_evals_dict(self, keys):
        """ If evals file exists, load it, otherwise create one from scratch.
            You should specify the keys you want to use in the dict."""
        if os.path.exists(self.evals_file):
            print("Loading previosuly saved evals file from: \n- ", self.evals_file)
            with open(self.evals_file, mode = "rb") as fileObj:
                self.evals = pickle.load(fileObj)
        else:
            self.evals = {key: [] for key in keys}
            self.evals["global_epoch"] = 0

    def save_evals_dict(self):
        """ Save evals dict to a picle file in models root directory """
        with open(self.evals_file, mode="wb") as fileObj:
            self.evals["global_epoch"] = self.global_epoch
            pickle.dump(self.evals, fileObj, protocol=2) #py2.7 & 3.x compatible

    def initialize_vars(self, session, best=False):
        """ Override this if you set up custom savers """
        if best:
            snapshot_file = self.best_snapshot_file
        else:
            snapshot_file = self.snapshot_file
        if tf.train.checkpoint_exists(snapshot_file):
            try:
                print("Restoring parameters from snapshot")
                self.saver.restore(session, snapshot_file)
            except (tf.errors.InvalidArgumentError, tf.errors.NotFoundError) as e:
                msg = "============================================================\n"\
                      "ERROR IN INITIALIZING VARIABLES FROM SNAPSHOTS FILE\n"\
                      "============================================================\n"\
                      "Something went wrong in  loading  the  parameters  from  the\n"\
                      "snapshot. This is most likely due to changes being  made  to\n"\
                      "the  model,  but  not  changing   the  snapshots  file  path.\n\n"\
                      "Loading from a snapshot requires that  the  model  is  still\n"\
                      "exaclty the same since the last time it was saved.\n\n"\
                      "Either: \n"\
                      "- Use a different snapshots filepath to create new snapshots\n"\
                      "  for this model. \n"\
                      "- or, Delete the old snapshots manually  from  the  computer.\n\n"\
                      "Once you have done that, try again.\n\n"\
                      "See the full printout and traceback above  if  this  did  not\n"\
                      "resolve the issue."
                raise ValueError(str(e) + "\n\n\n" + msg)

        else:
            print("Initializing to new parameter values")
            session.run(tf.global_variables_initializer())

    def save_snapshot_in_session(self, session, file):
        """Given an open session, it saves a snapshot of the weights to file"""
        # Create the directory structure for parent directory of snapshot file
        if not os.path.exists(os.path.dirname(file)):
            os.makedirs(os.path.dirname(file))
        self.saver.save(session, file)

    def shuffle_train_data(self, data):
        n_samples = len(data["Y_train"])
        permutation = list(np.random.permutation(n_samples))
        data["X_train"] = data["X_train"][permutation]
        data["Y_train"] = data["Y_train"][permutation]
        return data

    def get_batch(self, i, batch_size, X, Y=None):
        """ Get the ith batch from the data."""
        X_batch = X[batch_size*i: batch_size*(i+1)]
        # Handle dynamic loading option
        if self.dynamic:
            X_batch = load_batch_of_images(X_batch, img_shape=self.img_shape)

        # Batch of labels if needed
        if Y is not None:
            Y_batch = Y[batch_size*i: batch_size*(i+1)]
            return X_batch, Y_batch
        else:
            return X_batch

    def train(self, data, n_epochs, alpha=0.001, batch_size=32, print_every=10, l2=None, augmentation_func=None):
        """Trains the model, for n_epochs given a dictionary of data"""
        n_samples = len(data["X_train"])               # Num training samples
        n_batches = int(np.ceil(n_samples/batch_size)) # Num batches per epoch

        with tf.Session(graph=self.graph) as sess:
            self.initialize_vars(sess)
            t0 = time.time()

            try:
                str2file("training", file=self.train_status_file)
                # TODO: Use global epoch
                for epoch in range(1, n_epochs+1):
                    self.global_epoch += 1
                    print("="*70, "\nEPOCH {}/{} (GLOBAL_EPOCH: {})        ELAPSED TIME: {}".format(epoch, n_epochs, self.global_epoch, pretty_time(time.time()-t0)),"\n"+("="*70))

                    # Shuffle the data
                    data = self.shuffle_train_data(data)

                    # Iterate through each mini-batch
                    for i in range(n_batches):
                        X_batch, Y_batch = self.get_batch(i, X=data["X_train"], Y=data["Y_train"], batch_size=batch_size)
                        if augmentation_func is not None:
                            X_batch = augmentation_func(X_batch)

                        feed_dict = {self.X:X_batch, self.Y:Y_batch, self.alpha:alpha, self.is_training:True}
                        loss, _ = sess.run([self.loss, self.train_op], feed_dict=feed_dict)

                        # Print feedback every so often
                        if print_every is not None and (i+1)%print_every==0:
                            print("{}    Batch_loss: {}".format(pretty_time(time.time()-t0), loss))

                    # Save parameters after each epoch
                    self.save_snapshot_in_session(sess, self.snapshot_file)

                    # Evaluate on full train and validation sets after each epoch
                    train_acc, train_loss = self.evaluate_in_session(data["X_train"][:1000], data["Y_train"][:1000], sess)
                    valid_acc, valid_loss = self.evaluate_in_session(data["X_valid"], data["Y_valid"], sess)
                    self.evals["train_acc"].append(train_acc)
                    self.evals["train_loss"].append(train_loss)
                    self.evals["valid_acc"].append(valid_acc)
                    self.evals["valid_loss"].append(valid_loss)
                    self.save_evals_dict()

                    # If its the best model so far, save best snapshot
                    is_best_so_far = self.evals[self.best_evals_metric][-1] >= max(self.evals[self.best_evals_metric])
                    if is_best_so_far:
                        self.save_snapshot_in_session(sess, self.best_snapshot_file)

                    # Print evaluations (with asterix at end if it is best model so far)
                    s = "TR ACC: {: 3.3f} VA ACC: {: 3.3f} TR LOSS: {: 3.5f} VA LOSS: {: 3.5f} {}\n"
                    print(s.format(train_acc, valid_acc, train_loss, valid_loss, "*" if is_best_so_far else ""))

                    # # TRAIN CURVES
                    train_curves(train=self.evals["train_acc"], valid=self.evals["valid_acc"], saveto=os.path.join(self.model_dir, "accuracy.png"), title="Accuracy over time", ylab="Accuracy", legend_pos="lower right")
                    train_curves(train=self.evals["train_loss"], valid=self.evals["valid_loss"], saveto=os.path.join(self.model_dir, "loss.png"), title="Loss over time", ylab="loss", legend_pos="upper right")

                    # TODO: Visialize predictions.

                    str2file(str(max(self.evals[self.best_evals_metric])), file=self.best_score_file)
                str2file("done", file=self.train_status_file)

            except KeyboardInterrupt as e:
                print("Keyboard Interupt detected")
                # TODO: Finish up gracefully. Maybe create recovery snapshots of model
                str2file("interupted", file=self.train_status_file)
                raise e
            except:
                str2file("crashed", file=self.train_status_file)
                raise

    def prediction(self, X, batch_size=32, verbose=True, best=True):
        """Given input X make a forward pass of the model to get predictions"""
        # Dimensions
        n_samples = X.shape[0]
        n_batches = int(np.ceil(n_samples/batch_size))
        preds = np.zeros(n_samples, dtype=np.int32)
        if verbose:
            print("MAKING PREDICTIONS")
            percent_interval=10
            print_every = n_batches/percent_interval
            percent = 0

        with tf.Session(graph=self.graph) as sess:
            self.initialize_vars(sess, best=best)

            # Make Predictions on mini batches
            for i in range(n_batches):
                X_batch = self.get_batch(i, batch_size=batch_size, X=X)
                feed_dict = {self.X:X_batch, self.is_training:False}
                batch_preds = sess.run(self.preds, feed_dict=feed_dict)
                preds[batch_size*i: batch_size*(i+1)] = batch_preds.squeeze()

                if verbose and (i+1)%print_every == 0:
                    percent += percent_interval
        return preds

    def evaluate(self, X, Y, batch_size=32, best=False):
        """Given input X, and Labels Y, evaluate the accuracy of the model"""
        with tf.Session(graph=self.graph) as sess:
            self.initialize_vars(sess, best=best)
            return self.evaluate_in_session(X,Y, sess, batch_size=batch_size)

    def evaluate_in_session(self, X, Y, session, batch_size=32):
        """ Given input X, and Labels Y, and already open tensorflow session,
            evaluate the accuracy of the model
        """
        # Dimensions
        preds = np.zeros(Y.shape[0], dtype=np.int32)
        loss = 0.0
        n_samples = Y.shape[0]
        n_batches = int(np.ceil(n_samples/batch_size))

        # Make Predictions on mini batches
        for i in range(n_batches):
            X_batch, Y_batch = self.get_batch(i, batch_size=batch_size, X=X, Y=Y)
            feed_dict = {self.X:X_batch, self.Y:Y_batch, self.is_training:False}
            batch_preds, batch_loss = session.run([self.preds, self.loss], feed_dict=feed_dict)
            preds[batch_size*i: batch_size*(i+1)] = batch_preds.squeeze()
            loss += batch_loss

        accuracy = (preds.squeeze() == Y.squeeze()).mean()*100
        loss = loss / n_samples
        return accuracy, loss

# ==============================================================================
#                                                       GRAPH_FROM_GRAPHDEF_FILE
# ==============================================================================
def graph_from_graphdef_file(graph_file, access_these, remap_input=None):
    """ Given a tensorflow GraphDef (*.pb) file, it loads up the
        graph specified by that file.

        You need to specify which operations or tensors you want
        to get access to directly by passing a list of the
        operation or tensor names you want to get access to.

        You can also replace the original input tensor
        in the graph with your own tensor.

    Args:
        graph_file:   (str) Path to the GraphDef (*.pb) file
        access_these: (list of strings) A list of all the tensor
                      names you wish to extract. The tensor names
                      MUST EXACTLY match tensor names in the graph.
        remap_input: (dict) Swap out the input tensor in the graph
                     with your own tensor object.
                     A dictionary:
                     - Key is a string of the input tensor name within the
                       saved graph you are loading.
                     - Value is the new tensor object you want
                        to use as the new input to the saved graph instead.
                    Eg:
                        {"input:0": MyPlaceholder}

    Returns: (list)
        requested_ops: List of tensorflow operations or tensor objects
                       that were retreived by the names specified in the
                       `access_these` list.

        NOTE: the remapped input tensor is not returned, as it is
              already a tensor you have access to (since you created
              it outside the function)
    """
    with tf.device('/cpu:0'): # Prevent multiple prallel I/O operations
        with tf.gfile.FastGFile(graph_file, 'rb') as file_obj:
            # Load the graph from file
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(file_obj.read())

    # Extract particular operations/tensors
    requested_ops = tf.import_graph_def(
        graph_def,
        name='',
        return_elements=access_these,
        input_map=remap_input)
    return requested_ops
