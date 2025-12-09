def tip_calculator():
    print("Welcome to the Tip Calculator")
    bill = float(input("What was the total bill? \n$"))
    tip = float(input("What percentage tip would you like to give? \n")) * bill / 100
    people = int(input("How many people to split the bill? "))
    pay = (bill + tip)/people
    print(f"Each person should pay: ${pay:.2f}")


tip_calculator()