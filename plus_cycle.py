number = int(input())
split = str(number)
split1 = 0
split2 = 1
flag = 0

while True:
    for x in range(len(split)):
        split1 = int(split[1])
        split2 = int(split[0]) + int(split[1])
        split = str(split1) + str(split2)
        print(split)

    flag = flag + 1
    if number == int(split):
        break

print(flag)
