from collections import deque
"""
The class collections.deque is a thread-safe double-ended queue designed for
fast inserting and removing from both ends. It is also the way to go if you
need to keep a list of “last seen items” orsomething like that, because a deque can be bounded
"""

dq = deque(range(10), maxlen=10)
print(dq)

"""
The append and popleft operations are atomic, so deque is safe to use as a FIFO queue in multithreaded
applications without the need for using locks.

"""
