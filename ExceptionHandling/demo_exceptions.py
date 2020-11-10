# An exception is an error that occurs during the run time of your program.
# Some of the exceptions that can occur in a Python program are listed below.

# IOError (Input Output Error) This error occurs if a file cannot be opened
# ImportError This error occurs if Python cannot find a module
# KeyboardInterrupt - This error is raised when the user hits the interrupt key (normally Ctrl+C or Delete)
# ZeroDivisionError: This error occurs when a number is divided by zero
# NameError: This error occurs when the name of a local or a global variable is not found
# EOFError: It occurs when the end of a file is reached, and yet operations are being performed

# If we do not handle an exception, the Python interpreter terminates the entire execution of the program.
# So, handling exceptions is very important for the other part of the program to execute without any disruption.

# we mainly use two blocks 'try' block followed by 'except' block to handle exceptions. Any Python program that is suspicious to raise exceptions should be written inside the 'try' block. And the 'except' block should


try:
    a = int(input("enter the first number:"))
    b = int(input("enter the second number:"))
    res = a / b

except:
    print("cannot divide a number by zero")
else:  #'else' block should be written with the code that has to be executed if no exception occurs in the code
    print(int(res))
    print("FACE Prep")
finally:
    print("finally block has been executed")





# The statements written inside the 'finally' block will be executed regardless of the exception status. Statements that perform an operation like closing a file can be written inside the 'finally' block as closing the file has to be done irrespective of exception occurrence.

