# Using a list as a queue

queue = []

# Enqueue operations
queue.append(10)  # Add 10 to the queue
queue.append(20)  # Add 20 to the queue
queue.append(30)  # Add 30 to the queue

print("After enqueue operations:")
print("Queue:", queue)

# Dequeue operation
if len(queue) > 0:
    dequeued_item = queue.pop(0)  # Remove the front element
    print("\nDequeued item:", dequeued_item)
else:
    print("\nQueue is empty!")

print("After dequeue operation:")
print("Queue:", queue)

# Check queue size
queue_size = len(queue)
print("\nQueue size:", queue_size)

# Check if queue is empty
is_empty = len(queue) == 0
print("Is the queue empty?:", is_empty)
