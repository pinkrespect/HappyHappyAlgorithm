a = int(input())
b = int(input())
c = int(input())
answer = a * b * c
array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for x in str(answer):
    array[int(x)] += 1

for x in array:
    print(x)
