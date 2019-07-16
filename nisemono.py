N = int(input())
sum = 0
grade = list(map(int, input().split()))
M = max(grade)
for i in range(N):
    grade[i] = grade[i]/M*100
    sum += grade[i]
print('%.2f' % (sum/N))
