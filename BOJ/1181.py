n = int(input())
words = {}
for i in range(n):
    do = input()
    words[do]=len(do) 

word = list(words.items())
word.sort()
word.sort(key=lambda x:x[1])
for i in word:
    print(i[0])