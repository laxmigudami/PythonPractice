from time import sleep
from threading import *

class Face(Thread):
    def run(self):
        for i in range(3):
            print("Face Prep")
            sleep(1)


class Python(Thread):
    def run(self):
        for i in range(3):
            print("Python")
            sleep(1)


# main method
t1 = Face()
t2 = Python()
# t1.run() So instead of calling the threads using the method name run, we need to call using the name 'start'. To put simple, 'start' is used to start the execution of a thread.
# t2.run()

t1.start()
t2.start()
t1.join()
t2.join()
print("bbye")


