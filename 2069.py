def minimum(x, y):
    if x < y: x, y = y, x
    if y == 0: return x
    if x % y == 0: return y
    else: return minimum(y, x % y)

input1, input2 = [int(x) for x in input().split()]
#input2 = [int(x) for x in input().split()]

mini = minimum(input1, input2)

print(mini)
print(int(input1 * input2 / mini))

