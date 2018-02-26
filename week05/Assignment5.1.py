total = 0
count = 0

while (True):
    num = input("Enter a number: ")
    if (num == "done"):
        break
        
    try:
        num = float(num)
    except:
        print("""bad data
Invalid input""")
        continue
        
    total = total + num
    count = count + 1

print(total, count, total/count)
        