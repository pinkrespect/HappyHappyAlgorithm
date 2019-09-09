from math import pi

_ = input()

for x in range(int(_)):
    x1, y1, r1, x2, y2, r2 = input().split()

    x1, y1, r1, x2, y2, r2 = int(x1),int(y1),int(r1), int(x2),int(y2), int(r2)
    
    print(x1, y1, r1, x2, y2, r2)

    X_1 = x2 - x1 + r1
    X_2 = x2 - x1 - r1
    Y_1 = y2 - y1 + r2
    Y_2 = y2 - y1 - r2

    print(X_1, X_2, Y_1, Y_2)

    # if x < y or y < x:
    #     print(2)
    # elif x == y:
    #     print(1)
    # else:
    #     print(0)

