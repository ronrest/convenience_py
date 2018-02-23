def freeze_layers(model, layer_names, unfreeze=False):
    """ Given a model and a list of layer names, it freezes the weights for
        those layers. (if `unfreeze` is set to `True`, then it makes the
        layers trainable instead).

        NOTE: You should call model.compile() after running this.
    """
    for layer_name in layer_names:
        model.get_layer(layer_name).trainable = unfreeze
