while True:
    name, age, ton = input().split()
    if name == '#':
        break
    if int(age) > 17 or int(ton) >= 80:
        print(name + ' Senior')
    else:
        print(name + ' Junior')