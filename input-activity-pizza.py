greet = input("What is your name?: ")

print(f"Welcome to Pizza Shop, {greet}!")

item = input("What item do you want to purchase today? (Pepperoni, Hawaiian, or Vegetarian Pizza): ")

cost = print(f"{item} is ₱199.00.")

quantity = input(f"How many {item} do you want to purchase?: ")

quantity = int(quantity)

input(f"Thank you! You want to purchase {quantity} pc/s of {item}, is that correct?: ")

total = 199 * quantity

print(f"Your total is ₱ {total}")

print("Please come again next time! Thank you and God bless!")
