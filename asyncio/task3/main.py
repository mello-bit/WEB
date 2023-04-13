import asyncio
import os


async def gotGifts(purchasedGifts):
    for w in purchasedGifts:
        print(f"Got {w[0]}")
        await asyncio.sleep(w[2] / 100)


async def buyGifts(gifts, times, timeEnd=False):
    if not timeEnd:
        myTime = times[0]
        purchasedGifts = []

        while myTime > 0:
            for item in gifts:
                if item[1] + item[2] <= myTime:
                    myTime -= item[1] + item[2]
                    purchasedGifts.append(item)
                    gifts.remove(item)
                    print(f"Buy {item[0]}")
                    await asyncio.sleep(item[1] / 100)
                    break
            else:
                break

        await asyncio.gather(gotGifts(purchasedGifts))

    else:
        purchasedGifts = []
        while gifts != []:
            for item in gifts:
                print(f"Buy {item[0]}")
                await asyncio.sleep(item[1] / 100)
                purchasedGifts.append(item)
                gifts.remove(item)
                break

        await asyncio.gather(gotGifts(purchasedGifts))


async def main():
    times = []
    gifts = []

    time = input()
    while time != "":
        times.append(list(map(int, time.split(' '))))
        time = input()

    gift = input()
    while gift != "":
        gifts.append(
            list(map(lambda x: int(x) if x.isdigit() else x, gift.split(' '))))
        gift = input()

    gifts = sorted(gifts, key=lambda x: (-(x[1] + x[2]), x[0]))

    for t in range(len(times)):
        print(f"Buying gifts at {t + 1} stop")
        await buyGifts(gifts, times[t])
        print(f"Arrive from {t + 1} stop")

    if len(gifts) != 0:
        print("Buying gifts after arrival")
        await buyGifts(gifts, [], timeEnd=True)


if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
