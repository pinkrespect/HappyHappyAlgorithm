def split(List):
    index_no = len(List)
    half = int(index_no/2)
    print(half)
    left_List = List[0:half]
    right_List = List[half:index_no]

    return left_List, right_List


split(split([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
