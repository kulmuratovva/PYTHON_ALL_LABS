def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return
    for i in range(len(s)):
        permute(s[:i] + s[i+1:], answer + s[i])

w = input("Enter the word: ")
permute(w)
