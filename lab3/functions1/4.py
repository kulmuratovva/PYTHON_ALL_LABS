def fltr_prm(nums):
    p = []
    for i in nums:
        if i < 2:
            continue
        else:
            cnt = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    cnt += 1
            if cnt == 2:
                p.append(i)
    if len(p) == 0:
        return "There are no primes here"
    return p
            

nums = list(map(int, input().split()))

prime_nums = fltr_prm(nums)

print(prime_nums)