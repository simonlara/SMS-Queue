"""
update this file to implement the following already declared methods:
- enqueue: Should add a member to the list
- dequeue: Should remove and return an element from the top or the bottom of the list (depending on the list mode: FIFO or LIFO)
- get_all: should return the entire list as it is
- size: Should return the total size of the list
"""
from random import randint
from tulio import tulio
tulio=tulio()


class Queue:

    def __init__(self, mode='FIFO'):
        self._queue = []
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        self._mode = mode

    def enqueue(self, new):
         self._queue.append(new)
         mensaje=new['name']+' hay '+str(len(self._queue)-1 )+' personas antes que tu'
         tulio.enviarMensaje(msg=mensaje,numero=new['phone'])

         return mensaje

    def dequeue(self):
         turno=self._queue[0]
         mensaje=turno['name']+' es tu turno'
         tulio.enviarMensaje(msg=mensaje,numero=turno['phone'])
         self._queue.pop(0)

         return self._queue

    def get_all(self):

         return self._queue

    def size(self):

        # fill this function with the logic needed to make it work
        pass