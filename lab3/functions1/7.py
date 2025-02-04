def has_33(n):
    t = 0
    for i in range(len(n) - 1):
        if n[i] == 3 and n[i + 1] == 3:
            t += 1
    if t > 0:
        print(True)
    else:
        print(False)

n = list(map(int, input().split()))

has_33(n)