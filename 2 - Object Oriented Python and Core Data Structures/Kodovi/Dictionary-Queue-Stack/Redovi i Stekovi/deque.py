from collections import deque
 
queue = deque() # Prazan red
 
queue.append("Task 1")
 
queue.append("Task 2")
 
queue.append("Task 3")
 
# Uklanjanje elemenata iz reda (FIFO)

print(queue)
 
print(queue.popleft())  # Output: Task 1 - Uklanja sa leve strane (od prvog na dalje)
 
print(queue.popleft())  # Output: Task 2

