number = int(input())
stars = list()

for y in range(number):
    stars.append("")
    for x in range(number):
        if x >= y:
            stars[y] += "*"
    print(stars[y])
