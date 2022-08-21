source = "This is a book~!"
pattern = 'is'

def BruteForce(pattern, source):
    for idx in range(len(source)-len(pattern) + 1):
        for j in range(len(pattern)):
            if source[idx + j] != pattern[j]:
                break
        else:
            return idx
    else:
        return -1

print(BruteForce(pattern, source))