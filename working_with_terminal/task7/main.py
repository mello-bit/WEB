import schedule
import datetime


def print_cu():

    time = datetime.datetime.now().minute
    if time not in rn:
        if time > 12:
            time -= 12
        print(message * time)


message = input("Что вы хотите вывести? ")
shut_up = input("Когда молчать(вводить в формате 00-07)? ")
try:
    rn = range(int(shut_up.split('-')[0]), int(shut_up.split('-')[1]))
except Exception:
    print("Неверный формат ввода")
    quit()

if len(shut_up) != 5:
    print("Неправильный формат ввода")
    quit()


# schedule.every().hour.do(print_cu)
schedule.every().minute.at(":00").do(print_cu)

while True:
    schedule.run_pending()
