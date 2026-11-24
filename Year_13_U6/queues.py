# Linear Queue

global q, b, f, c

q = [None] * 10 
f = -1
b = 0

def enqueue(item):
    global q, b, f
    if b == 10:
        return
    q[b] = item
    b += 1

def dequeue():
    global q, b, f
    if f == 9:
        return
    f += 1
    return q[f]

print("Test 1")
[enqueue(i) for i in range(0, 11)]

print(q)

print("Test 2")
a = [dequeue() for i in range(0, 12)]

print(a)

# Circular Queue

q = [None] * 10 
f = -1
b = 0
c = 0

def cenqueue(item):
    global q, b, f, c
    if c == 10:
        return
    q[b] = item
    b = (b + 1) % 10
    c += 1

def cdequeue():
    global q, b, f, c
    if c == 0:
        return
    f  = (f + 1) % 10
    c -= 1
    return q[f]

print("Test 1")
[cenqueue(i) for i in range(0, 11)]

print(q)

print("Test 2")
a = [cdequeue() for i in range(0, 12)]

print(a)

print("Test 3")
[cenqueue(i) for i in range(0, 11)]
d = [cdequeue() for i in range(0, 3)]
[cenqueue(i) for i in range(10, 20)]
print(q)

print("Test 4")

[cdequeue() for i in range(0, 100)]
[cenqueue(i) for i in range(40, 80)]
g = [cdequeue() for i in range(0, 10)]

print(q)
print(g)

# Priority Queue

q = [[None, float("-inf")]] * 10
b = 0
c = 0

def penqueue(item, priority):
    global q, b, f, c
    if c == 10:
        return
    q[b] = [item, priority]
    c += 1
    b += 1
    q.sort(key=lambda x: x[1], reverse=True)

def pdequeue():
    global q, b, f, c
    if c == 0:
        return
    tmp = q[0]
    q[0] = [None, float("-inf")]
    q.sort(key=lambda x: x[1], reverse=True)
    c -= 1
    b -= 1
    return tmp

print("Test 1")
[penqueue(i, i) for i in range(0, 11)]

print(q)

print("Test 2")
a = [pdequeue() for i in range(0, 12)]

print(a)

print("Test 3")
[penqueue(i, i) for i in range(0, 10)]

print(q)

print("Test 4")
a = [pdequeue() for i in range(0, 10)]

print(a)

print("Test 5")
[penqueue(i, 5) for i in range(0, 10)]

print(q)

print("Test 6")
a = [pdequeue() for i in range(0, 10)]

print(a)

print("Test 7")
[penqueue(i, i) for i in range(0, 5)]
a = [pdequeue() for i in range(0, 3)]
[penqueue(i, i + 10) for i in range(5, 10)]

print(q)
print(a)

print("Test 8")
[pdequeue() for i in range(0, 100)]
[penqueue(i, i) for i in range(10, 20)]

print(q)