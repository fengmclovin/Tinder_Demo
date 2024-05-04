import asyncio
import time

async def task(name, delay):
    print(f"Task {name} started")
    await asyncio.sleep(delay)
    print(f"Task {name} completed after {delay} seconds")

async def main():
    # List of tasks to execute concurrently
    tasks = [
        task("A", 2),
        task("B", 1),
        task("C", 3),
        task("D", 2),
        task("E", 1)
    ]

    # Execute tasks concurrently using asyncio.gather
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    start_time = time.time()

    # Run the main coroutine
    asyncio.run(main())

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Total execution time: {execution_time} seconds")
