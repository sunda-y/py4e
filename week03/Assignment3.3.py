"""
3.3 Write a program to prompt the user for a score using raw_input. Print out a letter grade based on the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85. 
"""
# output:
#B

score = input("Please input your score\n")
try:
    score = float(score)
except:
    print("""Error, 
please enter numeric input in the range of 0 to 1""")
    quit()

if (score > 1.0):
    print("out of range")
    quit()
elif (score >= 0.9):
    res = 'A'
elif (score >= 0.8):
    res = 'B'
elif (score >= 0.7):
    res = 'C'
elif (score >= 0.6):
    res = 'D'
elif (score < 0.6):
    res = 'F'

print("Letter grade:", res)