# python3

import os
import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    
    unique_nodes = []
    for i in range(n):
        if parents[i] not in unique_nodes:
            unique_nodes.append(parents[i])
    
    max_height = len(unique_nodes)

    return max_height


def main():
    input_type = input()
    if input_type[:1] == 'I':
        n = int(input())
        parents_input = input()
        parents = numpy.array(list(map(int, parents_input.split())))
        height = compute_height(n, parents)
        print(height)

    elif input_type[:1] == 'F':
        file_name = input()

        if "test/" not in file_name:
            file_name = "test/" + file_name
        
        if not os.path.isfile(file_name) or os.path.getsize(file_name) == 0:
            print("Error: Invalid input file")
            return
        if ".a" in file_name:
            return
        
        with open(file_name, 'r') as file:
            n = int(file.readline())
            parents = numpy.array(list(map(int, file.readline().split())))
            height = compute_height(n, parents)
            print(height)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()