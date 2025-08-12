'''Task 7: Read a File and Handle Errors 
Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist.'''

try:
    # File open in read mode
    with open("sample.txt","r") as file:
        print("Reading file content:")
        line_number = 1
        for line in file:
            print(f'Line {line_number}: {line.strip()}')
            line_number += 1
            
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found. ")            