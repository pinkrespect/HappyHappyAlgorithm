days = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
month, date = input().split(" ")
month, date = int(month), int(date)


passed_date = 0

for x in range(month - 1):
    if x + 1 in [1, 3, 5, 7, 8, 10, 12]:
        passed_date = passed_date + 31
    elif x + 1 is 2:
        passed_date = passed_date + 28
    else:
        passed_date = passed_date + 30

passed_date = passed_date + date

while passed_date != 0:
    passed_date = passed_date % 7
    print(days[passed_date - 1])
    passed_date = 0

