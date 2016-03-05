

def wrap_slice(x, start, slice_len):
    return x[[index % x.shape[0] for index in range(start, start+slice_len)]]

