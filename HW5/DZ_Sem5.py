def f(a, b):
    if b == 0:
        return 1
    return f(a, b - 1) * a

n = int(input())
m = int(input())
print(f(n, m))






def sum(a, b):
    if b == 0:
        return a
    return sum(a, b - 1) + 1

n = int(input())
m = int(input())
print(sum(n, m))