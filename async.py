import asyncio
import datetime

async def task(name, delay):
    print(f"{datetime.datetime.now()} : Start {name}")
    await asyncio.sleep(delay)
    print(f"{datetime.datetime.now()} :End {name}")


async def time_out_ex():
    await asyncio.sleep(5)


async def main():
    await asyncio.gather(
        task("Task1", 2),
        task("Task2", 3)
        )
    try:
        await asyncio.wait_for(time_out_ex(), timeout=3)
    except asyncio.TimeoutError as e:
        print(f"{e}")


asyncio.run(main())


'''
KEY NOTES:
----------

Python async is designed for I/O-bound work, not CPU-heavy tasks

Async uses a single thread with an event loop

It provides concurrency, not true CPU parallelism

Async allows multiple API calls to be in-flight at the same time

Total execution time equals the slowest API call, not the sum

The event loop schedules and resumes tasks when they’re ready

async functions don’t run immediately; they return coroutines

await pauses execution and gives control back to the event loop

Blocking operations freeze the entire async system

Async works only with non-blocking (async-compatible) libraries

Async is different from threads and does not bypass Python’s GIL

Spring Boot uses multi-threading; Python async uses cooperative multitasking

Async is ideal for REST calls, LLM APIs, databases, and tools

AI agents benefit because they make many network calls

Golden rule: never block the event loop

Python programs start synchronously.
    await requires an active event loop, so it is only allowed inside async functions.
    asyncio.run() explicitly creates the event loop and bridges sync to async.

'''
