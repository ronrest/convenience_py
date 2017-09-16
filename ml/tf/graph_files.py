import tensorflow as tf

# ==============================================================================
#                                                                GRAPH_FROM_FILE
# ==============================================================================
def graph_from_file(graph_file, access_these=[]):
    """ Given a tensorflow GraphDef (*.pb) file, it loads up the
        graph specified by that file.

        This is useful for transfer learning.

        You can optionally get access to particular operations or
        tensors within the graph by passing a list of the operation
        or tensor names you want to get access to. This is
        particularly useful for getting access to the input and
        output tensors so you can feed values to the graph, and
        specify that it should run up to the output tensor.

    Args:
        graph_file:   (str) Path to the GraphDef (*.pb) file
        access_these: (list of strings) A list of all the tensor
                      names you wish to extract. The tensor names
                      MUST EXACTLY match tensor names in the graph.
    Returns: (tuple)
        A tuple with the following two items:

        - graph:         Tensorflow Graph object that was saved in the file.
        - requested_ops: List of tensorflow operations or tensor objects
                         that were retreived by the names specified in the
                         `access_these` list.
    """
    with tf.Graph().as_default() as graph:
        with tf.gfile.FastGFile(graph_file, 'rb') as file_obj:
            # Load the graph from file
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(file_obj.read())

            # Extract particular operations/tensors
            requested_ops = tf.import_graph_def(
                graph_def,
                name='',
                return_elements=access_these)
    return graph, requested_ops
