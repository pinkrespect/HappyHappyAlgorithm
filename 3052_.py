a = []
b = []

for x in range(10):
    a.append(int(input())%42)

for x in range(10):
    try:
        if a[0:x].index(a[x]) == True:
            pass
    except ValueError:
        b.append(a[x])

print(len(b))
