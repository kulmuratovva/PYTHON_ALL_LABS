def solve(numheads, numlegs):
    for i in range(1, numheads):
        if i*2 + (numheads-i)*4 == numlegs:
            return f"chicken {i}, rabbit {numheads-i}"

print(solve(35, 94))