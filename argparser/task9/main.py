import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--per-day', type=int, default=0)
parser.add_argument('--per-week', type=int, default=0)
parser.add_argument('--per-month', type=int, default=0)
parser.add_argument('--per-year', type=int, default=0)
parser.add_argument('--get-by', type=str, default='day',
                    choices=['day', 'month', 'year'])

items = parser.parse_args()
get_by = items.get_by
day = items.per_day
week = items.per_week
month = items.per_month
year = items.per_year


if get_by == 'day':
    print(int(day + (week / 7) + (month / 30) + (year / 360)))
elif get_by == 'month':
    print(int(day * 30 + (week * 30 / 7) + month + year / 12))
else:
    print(int(day * 360 + (week * 360 / 7) + month * 12 + year))
