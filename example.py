# -*- coding: utf-8 -*-

from mouse import Mouse
from eventpoller import EventPoller

class Display(object):
    """Mouse status display, Observer of Mouse"""

    def __init__(self, mouse):
        self.mouse = mouse
        mouse.add_observer(self)

    def update(self):
        print("")
        print("Mouse is:")

        if self.mouse.left:
            print('1. [X]')
        else:
            print('1. [ ]')

        if self.mouse.right:
            print('2. [X]')
        else:
            print('2. [ ]')

def main():
    # Create a mouse
    m = Mouse()
    # Create a poller for mouse event interpretation
    e = EventPoller(m)

    # Create a display to observe the mouse
    disp = Display(m)
    disp.update()

    # Run the poller
    e.run()

    # Prevent the main app from exiting
    while True:
        pass

    # Kill the poller thread
    e.stop()

    return 0

if __name__ == "__main__":
    main()
