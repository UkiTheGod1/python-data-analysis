queue = []  # Initializing the queue as an empty list

# Adding elements to the queue
queue.append("TV")
 
queue.append("Monitor")

queue.append("Camera")
 
print(f"Queue after adding items: {queue}")


# Removing the first element
next_item = queue.pop(0)  
 
print(f"Processed item: {next_item}")
 
print(f"Queue after removal: {queue}")


# Checking if the queue is empty
if queue:                    # Komanda "if lista:" postavlja uslov "ako lista JESTE" - postoji nevidljivo "is True", znaci ako sadzi elemente
    print("Queue has items") 
else:
    print("Queue is empty")   

# Peek at the first element without removing it 
if queue:
    first_item = queue[0]
    print(f'The first item in the queue is {first_item}')
else:
    print('The queue is empty')

# Peek at the last element without removing it 
if queue:
    last_item = queue[-1]
    print(f'The last item in the queue is {last_item}')
else:
    print('The queue is empty')

