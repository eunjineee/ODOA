s = list(input())
s1 = s[:]

for a in range(len(s1)//2):
    s1[-a-1],s1[a] = s1[a],s1[-a-1]

if s == s1:
    print('true')
else:
    print('false')
