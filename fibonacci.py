#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)


#take input
def userin():
  u_in = 0
  while (u_in < 1):
    try:
        # Prompt the user for a number
        u_in = int(input("enter valid fib input: "))
        if u_in < 1:
            print("Invalid input. Please enter a valid number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
  return u_in

#fib sequence
def fibonacci(x):
    fib_seq = []
    number1, number2 = 0, 1
    for _ in range(x):
        fib_seq.append(number1)
        number1, number2 = number2, number1 + number2
        
    return fib_seq

#print
def print(x):
  print()

print(fibonacci(userin()))

