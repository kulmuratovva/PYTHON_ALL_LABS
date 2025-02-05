import itertools

def permute(word):
    permut = itertools.permutations(word)
    for per in permut:
        print("".join(per))
        
w = input()
permute(w)
