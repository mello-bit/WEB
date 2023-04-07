import asyncio
import os
import time


async def do_some_work(applicant):
    name = applicant[0]
    for i in range(2):
        print(f"{name} started the {i + 1} task.")
        await asyncio.sleep(applicant[1 + i] / 100)
        print(f"{name} moved on to the defense of the {i + 1} task.")
        await asyncio.sleep(applicant[2 + i] / 100)
        print(f"{name} completed the {i + 1} task.")

        if i != 1:
            print(f"{name} is resting.")
            await asyncio.sleep(5 / 100)


async def interviews(*applicants):
    applicantsTasks = []
    for j in range(len(applicants)):
        applicantsTasks.append(
            asyncio.create_task(do_some_work(applicants[j])))

    await asyncio.gather(*applicantsTasks)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews(*data))
    print(time.time() - t0)
