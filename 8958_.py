_ = input()
a = []

for x in range(int(_)):
    a.append(input())

for x in a:
    z = 0
    flag = 0
    for y in x:
        if y == 'O':
            z += 1 + flag
            flag += 1
        else:
            flag = 0
    print(z)
