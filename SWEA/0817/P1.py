def push(item, size):
	global top
	top += 1
	if top == size:
		print('overflow!')
	else:
		stack[top] = item
		print(stack[top])
def pop():
	global top
	if top == -1:
		print('underflow!')
		return 0
	else:
		top -= 1
		print(stack[top+1])

stack = [0] * 10
top = -1
push(1,4)
push(2,4)
push(3,4)
pop()
pop()
pop()