'''Task 8: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.'''

first_text = input("Enter text to write to the file: ")
with open("output.txt","w") as file:
    file.write(first_text + "\n")
    print("Data successfully written to output.txt.")

append_text = input("Enter additional text to append:  ")
with open("output.txt","a") as file:
    file.write(append_text + "\n")
    print("Data succesfully appended.")
    
with open("output.txt","r") as file:
    content = file.read()
    print("\nFinal content of output.txt: ")
    print(content)    
    
    