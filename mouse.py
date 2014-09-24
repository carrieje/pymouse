# -*- coding: utf-8 -*-

class Mouse(object):
    """Mouse status, observable"""

    def __init__(self, mfile='/dev/input/mice'):
        # Assuming that at start, both buttons are released
        self.mfile = mfile
        self._left = False
        self._right = False
        self.observers = []

    def warn_observers(self):
        for o in self.observers:
            o.update()

    def add_observer(self, observer):
        self.observers.append(observer)

    def rm_observer(self, observer):
        self.observers.remove(observer)

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        if self._left != value:
            self._left = value
            self.warn_observers()

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        if self._right != value:
            self._right = value
            self.warn_observers()
