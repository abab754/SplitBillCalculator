print("welcome to the tip calculator")

total = float(input("What was the total bill? $"))
people = int(input("How many people are splitting the bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))

bill = (total*(1+(tip/100)))/people
final = "{:.2f}".format(bill)
print(final+" per person")