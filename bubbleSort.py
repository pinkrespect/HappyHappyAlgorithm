from random import randint


def bubbleSort(data_list):
    local_list = data_list.copy() 
    for x in range(len(local_list)):
        for y in range(len(local_list)):
            if ((len(local_list)-1) is not y) and (local_list[x] < local_list[y]):
                local_list[y], local_list[x] = local_list[x], local_list[y]
    return local_list

def insertSort(data_list):
    local_list = data_list.copy()
    for index in range(len(local_list)):
        for y in range(index):
            if local_list[y] > local_list[index]:
                local_list.insert(y, local_list.pop(index))
        print(local_list)
    return local_list

def selectionSort(data_list):
    local_list = data_list.copy()
    for index in range(len(local_list) - 1):
        minimum = len(local_list) - 1
        for y in range(index + 1, len(local_list)):
            if local_list[minimum] > local_list[y]:
                minimum = y
            print(local_list)
        local_list[index], local_list[minimum] = local_list[minimum], local_list[index]
    return local_list    




test_list = [randint(1, 30) for x in range(10)]
sorted_list = sorted(test_list)
# insert_list = insertSort(test_list)
# test_list = bubbleSort(test_list)
select_list = selectionSort(test_list)

print("unsorted: ", test_list)
print("sorted: ", sorted_list)

# print("bubble sorted: ", test_list)
# print("insert sorted: ", insert_list)
print("selection sorted: ", select_list)
if sorted_list == select_list:
    print("true")
