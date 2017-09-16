import tensorflow as tf

def graph_from_file(graph_file, access_these=[]):
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
