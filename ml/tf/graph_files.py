import tensorflow as tf


# ==============================================================================
#                                                                GRAPH_FROM_FILE
# ==============================================================================
def graph_from_file(graph_file, access_these, remap_input=None):
    """ Given a tensorflow GraphDef (*.pb) file, it loads up the
        graph specified by that file.

        You need to specify which operations or tensors you want
        to get access to directly by passing a list of the
        operation or tensor names you want to get access to. This
        is particularly useful for getting access to the input
        and output tensors so you can feed values to the graph,
        and specify that it should run up to the output tensor.

        You can also optionally replace the original input tensor
        in the graph with your own tensor. This is useful in the
        following cases:

        - You wish to modify the dimensions of the input placehoder,
          and specify your own.
        - You do not want to feed directly to the graph's original
          placeholder directly, but instead, you wish to perform
          some operations before feeding to the graph.

        In either case, you need to first create the tensor you
        wish to use as the new input to the graph.

        If you use this option, then DO NOT try to access the
        input tensorf using the `access_these` argument, as it
        will return the original input tensor, not the new
        replaced tensor.

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

    Examples:
        graph = tf.Graph()
        with graph.as_default():
            X = tf.placeholder(tf.float32, shape=[None, 32, 32, 3], name="X")
            rescaled_inputs = tf.div(X, 255., name="rescaled_inputs")

            # Load pretrained model
            graph_file = "path/to/pretrained_model.pb"
            which_tensors = ["conv1/relu:0", "conv2/relu:0"]
            requested_ops = graph_from_file(graph_file=graph_file,
                                            access_these=which_tensors,
                                            remap_input={"input:0": X})

            final_conv = requested_ops[-1]

            # Fully connected layers
            x = tf.contrib.layers.flatten(final_conv)
            logits = tf.layers.dense(x, units=10)

            print(requested_ops)
            # [<tf.Tensor 'conv1/relu:0' shape=(1, 8, 8, 32) dtype=float32>,
            #  <tf.Tensor 'conv2/relu:0' shape=(1, 4, 4, 64) dtype=float32>]
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
