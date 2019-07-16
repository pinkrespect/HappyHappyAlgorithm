def get_average(List):
    average = sum(List) / (len(List))
    return average

def over_average(List):
    average = get_average(List)
    over_person = 0
    for i in List:
        if i > average:
            over_person = over_person + 1
    return over_person / (len(List)) * 100


tests = int(input())

for x in range(tests):
    temp = input().split(" ")
    person = int(temp[0])
    scores = [int(x) for x in temp[1:]]
    print("%0.3f" % over_average(scores) + '%')

