def histogram(nums):
    for i in nums:
        for j in range(i):
            print('*', end="")
        print()

n = list(map(int, input().split()))

histogram(n)