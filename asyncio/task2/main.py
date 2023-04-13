import asyncio
import os
import time


async def completeTask(applicant):
    name = applicant[0]

    print(f"{name} started the {1} task.")
    await asyncio.sleep(applicant[1] / 100)
    print(f"{name} started the {2} task.")
    await asyncio.sleep(applicant[3] / 100)

    print(f"{name} moved on to the defense of the {1} task.")
    await asyncio.sleep(applicant[2] / 100)
    print(f"{name} completed the {1} task.")

    print(f"{name} moved on to the defense of the {2} task.")
    await asyncio.sleep(applicant[4] / 100)
    print(f"{name} completed the {2} task.")


async def interviews_2(*applicants):
    applicantsTasks = []
    for i in range(len(applicants)):
        applicantsTasks.append(
            asyncio.create_task(completeTask(applicants[i]))
        )

    await asyncio.gather(*applicantsTasks)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    data = [('Ivan', 5, 2, 7, 2), ('John', 3, 4, 5, 1), ('Sophia', 4, 2, 5, 1)]
    t0 = time.time()
    asyncio.run(interviews_2(*data))
    print(time.time() - t0)
