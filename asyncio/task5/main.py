import time
import os
import asyncio


AF = 3 / 1000
DISINSECTION = 5 / 1000


async def treat_plant(name, before_planting, remove_cover, plant):
    before_planting /= 1000
    remove_cover /= 1000
    plant /= 1000

    print(f"0 Beginning of sowing the {name} plant")

    print(f"1 Soaking of the {name} started")
    time.sleep(before_planting)
    print(f"2 Soaking of the {name} is finished")

    print(f"3 Shelter of the {name} is supplied")
    time.sleep(remove_cover)
    print(f"4 Shelter of the {name} is removed")

    print(f"5 The {name} has been transplanted")
    time.sleep(plant)
    print(f"6 The {name} has taken root")

    print(f"7 Application of fertilizers for {name}")
    await asyncio.sleep(AF)
    print(f"7 Fertilizers for the {name} have been introduced")

    print(f"8 Treatment of {name} from pests")
    await asyncio.sleep(DISINSECTION)
    print(f"8 The {name} is treated from pests")
    print(f"9 The seedlings of the {name} are ready")


async def sowing(*data):
    tasks = [asyncio.create_task(treat_plant(*row)) for row in data]
    await asyncio.gather(*tasks)


if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
