import schedule
import datetime


def print_cu():
    time = datetime.datetime.now().hour
    if time > 12:
        time -= 12
    print("Ky" * time)


# schedule.every().hour.do(print_cu)
schedule.every().hour.at(":00").do(print_cu)

while True:
    schedule.run_pending()
