number = input()

A = list()
for x in range(int(number)):
    A.append(int(input()))

A.sort()

for x in range(int(number)):
    print(A[x])
