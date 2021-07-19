import asyncio

async def amogus():
    print("suspicious")
    task = asyncio.create_task(sus("red"))
    tugas = asyncio.create_task(sus("green"))
    await asyncio.sleep(2)
    print("amogus")

async def sus(color):
    print("{0} is sus".format(color)) 
    await asyncio.sleep(1.5)
    print("IMPOSTOR")

asyncio.run(amogus())