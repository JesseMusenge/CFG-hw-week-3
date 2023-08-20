from collections import deque

queue = deque()

with open('hw3_q1.txt') as f:
    for line in f:
        command, name = line.split()
        
        if command == 'JUMP':
            queue.appendleft(name)
        elif command == 'JOIN':
            queue.append(name)

print(list(queue))

""" For Time Complexity:
Looping through the file line by line, splitting and appending to the deque. 
These are all O(1) operations because each line consists of a constant number of operations. 
So the total time complexity is O(N) where N is the number of lines in the input file.
Converting the deque to a list: O(N), where N is the number of elements in the deque.

For Space Complexity:
The space complexity of the above solution is O(n), where n is the number of people in the queue. 
This is because the program has to store all the people in the queue, and each person takes constant space to store. 
In the worst case, all the people might be in the queue simultaneously.
Other variables: O(1), because they only take constant space.

Assumptions:
The input file format is well-formatted, so each line exactly consists of only 2 words: the commands "JOIN"/"JUMP" and the person's name.
There are no extra spaces or characters in the input file that would cause the splitting process to fail.
The names of the people in the queue are unique. """