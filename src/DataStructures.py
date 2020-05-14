class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFOssss"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        self._queue.append(item)
        colita=self._queue
        return colita

    def dequeue(self):
        if self._mode == "FIFO":
            usuario= self._queue.pop(0)
        else:
            usuario= self._queue.pop()
        return usuario

    def get_queue(self):
        return self._queue

    def size(self):
        pass
