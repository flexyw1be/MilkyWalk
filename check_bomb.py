n = int(input())
a = b = int(1)
k = int()
j = str()
n -= 2

while n > 0:
    c = a + b
    k = c
    a = b
    b = c
    n -= 1
    j = j + " " + str(k)

print("0 1" + j)
