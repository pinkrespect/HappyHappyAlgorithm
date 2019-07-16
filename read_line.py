from sys import stdin as read

List = [read.readline().rstrip().split(" ") for i in range(int(input()))]

for a in range(len(List)):
    print(int(List[a][0]) + int(List[a][1]))
