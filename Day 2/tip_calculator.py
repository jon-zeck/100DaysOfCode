''' Day 2: Tip Calculator (American Version) '''

print("Welcome to the tip calculator")
total = float(input("What was your total? "))
tip = 0
while True:
    tip = float(input("How much of a tip would you like to give? 10, 12, or 15? "))
    if tip == 10 or tip == 12 or tip == 15:
        tip = 1 + tip / 100
        break
    else:
        print("Invalid amount, please try again.")
total *= tip
people = 0
while True:
    people = float(input("How many people are splitting the bill? "))
    if not people == 0:
        break
    else:
        print("Invalid amount, please try again.")

total_per_person = round(total / people, 2)
print(f"Each person has to pay £{total_per_person}.")

''' I went a bit above and beyond with the error case checking '''
