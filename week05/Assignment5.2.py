
"""
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter the numbers from the book for problem 5.1 and Match the sample output below. 
"""

#output:
#Invalid input
#Maximum is 7
#Minimum is 4

largest = None
smallest = None

while (True):
    value = input("Enter a number: ")
    if (value == "done"):
        break
    
    try:
        value = float(value)
    except:
        print("""Invalid input
Please input numeric number or the word `done`""")
        continue
    
    if (largest is None):
        largest = value
    elif (value > largest):
        largest = value
        
    if (smallest is None):
        smallest = value
    elif (value < smallest):
        smallest = value

print("Maximum is", largest)
print("Minimum is", smallest)
