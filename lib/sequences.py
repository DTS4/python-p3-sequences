#!/usr/bin/env python3

def print_fibonacci(length):
     
    if length <= 0:
        print([])  
        return

    elif length == 1:
        print([0])
        return
    
    elif length == 2:
        print([0, 1])
        return

    fibonacci_sequence = [0, 1]
    
    for i in range(2, length):
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)
    
    print(fibonacci_sequence)

print_fibonacci(9)   
