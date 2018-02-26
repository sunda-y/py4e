"""3.1 Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay. 
Award time-and-a-half for the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
You should use raw_input to read a string and float() to convert the string to a number.
Do not worry about error checking the user input - assume the user types numbers properly. 
"""

#output:
#498.75
hours = input("how many hours did you work?\n")
rate = input("how much do you earn per hour?\n")
pay = float(hours) * float(rate)

if (float(hours) > 40):
    pay = pay + (float(hours) - 40) * float(rate) * 0.5
    
print("Pay", pay)