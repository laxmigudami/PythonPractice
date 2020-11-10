# what is the thread??
# Consider you are playing a game on your mobile. The game as a whole is a single process.
# This process has some mini processes or mini-tasks like playing music, displaying advertisements, etc.
# These mini-processes are referred to as threads.
# egs2 --While creating a word document In MS Office, you can find some threads like spell check, grammar check, etc.

# A thread of a process has its own thread ID, program counter, registers, and stack and can execute independently.
# You can check the number of threads running in your system using Task Manager

# why we need multithreading?/
# Similar to multitasking, multithreading is also very useful for efficient time management and performance improvement.
# Creating a thread is more economical when compared to creating a process


class Face:
    def run(self):
        for i in range(3):
            print("Face Prep")


class Python:
    def run(self):
        for i in range(3):
            print("Python")


# main method
t1 = Face()
t2 = Python()
t1.run()
t2.run()

# We need both the methods to execute simultaneously. But, the 'run()' method of the class 'FACE' is executed
# first followed by the 'run()' method of the class 'Python'. This is because, by default, every execution of a program has
# one thread called the main thread. Even if you are not creating your own thread explicitly, Python provides this main thread.
# So, the execution of the above code is because of the main thread


