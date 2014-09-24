# -*- coding: utf-8 -*-

import thread

class EventPoller(object):
    """Poll for mouse events and change its status"""

    LEFT_BUTTON_MASK = 1
    RIGHT_BUTTON_MASK = 2

    def __init__(self, mouse):
        self.mouse = mouse
        self.thread = None

    def run(self):
        if self.thread is None:
            self.thread = thread.start_new_thread(EventPoller._polling, (self,))
            return 0
        else:
            print('Poller already running')
            return 1

    def stop(self):
        # TODO Exit self.thread
        pass

    def _polling(self):
        """Run non stop: polling and update mouse"""
        mouse = open(self.mouse.mfile)
        while True:
            status, dx, dy = tuple(ord(c) for c in mouse.read(3))

            # Toggle Mouse buttons status
            if status & EventPoller.LEFT_BUTTON_MASK:
                self.mouse.left = True
            elif self.mouse.left:
               self.mouse.left = False

            if status & EventPoller.RIGHT_BUTTON_MASK:
                self.mouse.right = True
            elif self.mouse.right:
               self.mouse.right = False
