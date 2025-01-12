# The asyncio module implements a single-threaded event loop to handle concurrency. It
# uses asynchronous coroutines and non-blocking operations.

# Import module
import asyncio

# Define hello async function
async def hello(i):
    print(f"hello {i} started")
    await asyncio.sleep(3) # asyncio.sleep() is non-blocking so allows other tasks
                           # in the event loop to run while this task 'sleeps'.
    print(f"hello {i} done")

# Define main async function
async def main():
    # Create two asynchronous tasks
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))

    # Await tasks finish
    await task1
    await task2

# Run asynchronous main function
asyncio.run(main())

