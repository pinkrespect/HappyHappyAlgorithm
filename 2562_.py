array = list()
max = 0

for x in range(9):
    array.append(int(input()))
    if max < array[x]:
        max = array[x]

print(max)
print(array.index(max))
