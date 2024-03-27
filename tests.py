import asyncio


async def main():
    task = asyncio.create_task(inner())
    print("One", end=" ")
    await asyncio.sleep(3)
    print("Four", end=" ")
    await asyncio.sleep(1)
    print("Five")


async def inner():
    print("Two", end=" ")
    await asyncio.sleep(1)
    print("Three", end=" ")


asyncio.run(main())

