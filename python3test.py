sugar = int(input())

sugar_5 = sugar/5
sugar_3 = sugar/3

if sugar_5 < 2:
    print("1", int(sugar_3))

elif sugar_5 - int(sugar_5) > 0:
    sugar_5_list = [x * 5 for x in range(int(sugar_5))]
    sugar_3_list = [x * 3 for x in range(int(sugar_3))]
    for x, y in range(len(sugar_5_list)), range(len(sugar_3_list)):
        if sugar_5_list[x] + sugar_3_list[y] == sugar:
            print(x + y)
            break
        elif ( (sugar_5 + sugar_3) - (int(sugar_5) + int(sugar_3))> 1):
            print(-1)
