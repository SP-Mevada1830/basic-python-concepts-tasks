'''Task 5: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.'''
 
def factorial(x):
    if(x<2):
        return 1
    else:
        return(x * factorial(x-1))
    
x =int(input("Enter the no: ")) 
Result = factorial(x)
print(f"Factorial of {x} is:  ",Result)    