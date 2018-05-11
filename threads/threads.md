# Threads

## Basic thread functions

```py
import threading
QUEUE_TERMINATING_VALUE = "zzz this is a killer"

def create_thread(worker_func, as_daemon=True, start=True, name="Thread1", **kwargs):
    """ `kwargs` is keyword args to be passed on to worker_func """
    # put each worker to work to process items in queue
    t = threading.Thread(target=worker_func, kwargs=kwargs, name=name)
    if as_daemon:
        t.setDaemon(True)
    if start:
        t.start()
    return t

```


