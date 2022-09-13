def checker():
    x = int(input())
    A = set(map(int, input().split()))
    y = int(input())
    B = set(map(int, input().split()))

    s = []

    for i in A:
        if i in B:
            s.append(i)
    s = set(s)

    if s == A:
        print("True")
    else:
        print("False")

t = int(input())
for i in range(t):
    checker()