string = input()

for x in range(len(string)):
    if x % 10 == 0:
        print(string[:10])
        string = string[10:]
    elif len(string) < 10:
        print(string[0:])
        break

