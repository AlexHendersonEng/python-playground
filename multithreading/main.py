# Multithreading: A programming technique that allows a single process to run multiple
#                 threads concurrently. Threads are small units of a process that share
#                 the same memory space and resources but can execute independently.
#                 Thread must manage shared resources carefully to avoid issues like race
#                 conditions or deadlocks. Due to the Python Global Interpreter Lock (GIL)
#                 threads must take turns to execute so they are not truly run concurrently.
#                 This is often used in situation involving I/O operations, background 
#                 processing or real-time data handling.

# daemon thread: A thread that runs in the background and will not be waited for by the main
#                thread to complete its task before exiting. Daemon threads are killed 
#                automatically when the main thread exits.

# Import modules
import threading
import time

# Define timer functions
def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print("Time:", count, "seconds")

# Define step functions
def step1():
    time.sleep(3)
    print("Step 1")

def step2():
    time.sleep(5)
    print("Step 2")

def step3():
    time.sleep(3)
    print("Step 3")

# Call functions on separate threads
a = threading.Thread(target=timer, args=(), daemon=True)
a.start()
b = threading.Thread(target=step1, args=())
b.start()
c = threading.Thread(target=step2, args=())
c.start()
d = threading.Thread(target=step3, args=())
d.start()

# Print thread info
print("Number of active threads:", threading.active_count())
print("Active threads:", threading.enumerate())

# Wait for threads to finish
b.join()
c.join()
d.join()