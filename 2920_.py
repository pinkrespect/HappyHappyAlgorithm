numbers = list(map(int, input().split()))
ascending_flag = 0
descending_flag = 0
mixed_flag = 0

for x in range(1, 8):
    if numbers[x] - 1 == numbers[x-1]:
        ascending_flag += 1
    elif numbers[x] + 1 == numbers[x-1]:
        descending_flag += 1
    else:
        mixed_flag += 1
        break

if ascending_flag == 7:
    print("ascending")
elif descending_flag == 7:
    print("descending")
else:
    print("mixed")

