#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`apqueue` module

:author: `FIL - Faculté des Sciences et Technologies -
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september
:last revision: 2017, october

A module for queue data structure.

:Provides:

* class ApQueue

and methods

* `enqueue`
* `dequeue`
* `is_empty`

:Examples:

>>> ap_queue = ApQueue()
>>> ap_queue.is_empty()
True
>>> ap_queue.enqueue(1)
>>> ap_queue.is_empty()
False
>>> ap_queue.enqueue(2)
>>> ap_queue.dequeue()
1
>>> ap_queue.dequeue()
2
>>> ap_queue.is_empty()
True
>>> ap_queue.dequeue()
Traceback (most recent call last):
   ...
ApQueueEmptyError: empty queue, nothing to dequeue
"""


class ApQueueEmptyError(Exception):
    """
    Exception for empty stacks
    """
    def __init__(self, msg):
        self.message = msg


class ApQueue():

    def __init__(self):
        """
        :build: a new empty queue
        :UC: none
        """
        self.__content = []

    def enqueue(self, x):
        """
        :param x: a value
        :type x: any
        :return: None
        :rtype: Nonetype
        :Side effect: queue self contains a new value : x
        :UC: none
        """
        self.__content.append(x)

    def dequeue(self):
        """
        :return: element on top of self
        :Side effect: self contains an element less
        :UC: self must be non empty
        """
        if len(self.__content) > 0:
            res = self.__content.pop(0)
        else:
            raise ApQueueEmptyError('empty queue, nothing to dequeue')
        return res

    def is_empty(self):
        """
        :return:
           * ``True`` if s is empty
           * ``False`` otherwise
        :rtype: bool
        :UC: none
        """
        return self.__content == []

    def __len__(self):
        """
        :return: len of ApQueue
        :rtype: int
        """
        return len(self.__content)


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE |
                    doctest.ELLIPSIS,
                    verbose=True)
