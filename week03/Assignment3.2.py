hours = input("How many hours did you work?\n")
rate = input("How much did you earn?\n")
try:
    hours = float(hours)
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

pay = hours * rate

if (hours > 40):
    pay = pay + (hours - 40) * rate * 0.5

print("Pay:", pay)
