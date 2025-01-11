# Multiprocessing: A programming technique that allows a program to run multiple processes
#                  concurrently. Each process runs in its own memory space and operates
#                  independently of other processes. This allows for true concurrency in
#                  Python as each process has its own Python interpreter so they are not
#                  limited by the Python Global Interpreter Lock (GIL). Inter-process 
#                  communication is expensive and slower comapred to thread communication.
#                  Multiprocessing is typically used for CPU bound tasks.

# Import modules
from multiprocessing import Process, cpu_count
import time

# Define counter function
def counter(num):
    count = 0
    while count < num:
        count += 1

# Define main function
def main():
    # Print CPU count
    print("CPU count:", cpu_count()) 

    # Start processes
    a = Process(target=counter, args=(1e8,))
    a.start()
    b = Process(target=counter, args=(1e8,))
    b.start()
    c = Process(target=counter, args=(1e8,))
    c.start()

    # Wait for processes to finish
    a.join()
    b.join()
    c.join()

# Avoid accidental thread creation by ensuring main is only executed when this
# module is being run directly
if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Run time:", time.time() - start_time)