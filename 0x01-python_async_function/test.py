import asyncio


async def func1():
	print("Function 1 started..")
	await asyncio.sleep(2)
	print("Function 1 Ended")


async def func2():
	print("Function 2 started..")
	await asyncio.sleep(3)
	print("Function 2 Ended")


async def func3():
	print("Function 3 started..")
	await asyncio.sleep(1)
	print("Function 3 Ended")


async def main():
	L = await asyncio.gather(
		func1(),
		func2(),
		func3(),
	)
	print("Main Ended..")


asyncio.run(main())


# async def wait_me(num: int, num2: int) -> int:
#     return num + num2

# async def main():
#     print("hello")
#     await asyncio.sleep(2)
#     res = await wait_me(4, 4)
#     print(res)
#     print("abokhadra")

# if __name__ == '__main__':
#     asyncio.run(main())

"""
Now if you want the program to be actually asynchronous,
In the actual order of execution we’ll need to make tasks 
in order to accomplish this. This means that the other function
will begin to run anytime if there is any free time using 'asyncio.create_task(fn2())'
"""
