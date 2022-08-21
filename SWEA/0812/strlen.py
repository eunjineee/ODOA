def strlen(a):
    num = 0
    i = ''
    while i != '\0':
        for i in a:
            if i != '\0':
                num += 1
    print(num)
a = ['a','b','c','\0']
strlen(a)