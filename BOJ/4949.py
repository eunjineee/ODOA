

while True:
    name = input()
    nameli = [] 
    if name == '.':
        break
    for i in name:
        if i == '(' or i == '[':
            nameli.append(i)
        elif i == ')':
            if len(nameli) != 0 and nameli[-1] == '(':
                nameli.pop()
            else:
                print('no')
                break
        elif i == ']':
            if len(nameli) != 0 and nameli[-1] == '[':
                nameli.pop()
            else:
                print('no')
                break
        if i == '.':
            if len(nameli) == 0:
                print('yes')
                break
            else:
                print('no')
                break