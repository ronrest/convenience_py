# Threads

## Basic thread functions

```py
import threading
QUEUE_TERMINATING_VALUE = "zzz this is a killer"

def get_thread_name():
    return threading.current_thread().name


def create_thread(worker_func, as_daemon=True, start=True, name="Thread1", **kwargs):
    """ `kwargs` is keyword args to be passed on to worker_func """
    # put each worker to work to process items in queue
    t = threading.Thread(target=worker_func, kwargs=kwargs, name=name)
    if as_daemon:
        t.setDaemon(True)
    if start:
        t.start()
    return t

def create_threads(worker_func, output=None, n=1, as_daemon=True, prefix="Thread", **kwargs):
    """ `kwargs` is keyword args to be passed on to worker_func
        `output` =  a list, whose values you want to overide with new threads.
                    This will ignore `n`.
                    In this case, it modifies the output list **in place**.
    """
    # put each worker to work to process items in queue
    if output is None:
        output = [None]*n
    for i in range(len(output)):
        t = create_thread(worker_func, as_daemon=True, start=True, name=prefix+str(i), **kwargs)
        output[i] = t
    return output
```


## Thread health

```py
def print_threads_health(threads):
    with threading.Lock():
        for thread in threads:
            print("{}: {}".format(thread.getName(), "alive" if thread.is_alive() else "dead"))

def get_threads_health(threads):
    summaries = []
    with threading.Lock():
        for thread in threads:
            status = "alive" if thread.is_alive() else "dead"
            summaries.append({"name":thread.getName(), "status":status})
    return summaries
```


