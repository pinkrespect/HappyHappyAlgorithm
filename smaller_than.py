from sys import stdin as read

number, compare = list(map(int, read.readline().split()))
a = map(int, read.readline().split())
b = ''
for x in a:
    if x > compare:
        b = b + str(x) + ' '

print(b[0:len(b)-1])
