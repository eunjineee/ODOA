s = ['a','l','g','o','r','i','t','h','m']
#1
s[::-1]
#2
s[-1::-1]
#3
list1 = list(s)
list1.reverse
reverse_s = ' '.join(list1)
#4
for idx in range(len(s)-1,-1,-1):
    reverse_s =reverse_s + s[idx]
print(reverse_s)
#5
for a in range(len(s)//2):
    s[-a-1],s[a] = s[a],s[-a-1]
print(s)