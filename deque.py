from  collections import deque

q = deque([1,2,3,4,5],5)
q.append(6)
print(q.popleft())

# linxu tail cmd

def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q

for line in tail(5):
    print(line, end='')

