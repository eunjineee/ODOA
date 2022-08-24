N = 3
q = [0]*N
front = -1
rear = -1

rear = (rear + 1) % N
q[rear] = 10

rear = (rear + 1) % N
q[rear] = 20

rear = (rear + 1) % N
q[rear] = 30

rear = (rear + 1) % N
q[rear] = 40

front = (front +1 ) % N
print(q[front])

front = (front +1 ) % N
print(q[front])

front = (front +1 ) % N
print(q[front])