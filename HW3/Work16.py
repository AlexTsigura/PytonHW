n = int(input())
list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)
count = 0
k = int(input())
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)