age = int(input("Enter your age: "))

if age < 0:
    print("Please enter a valid age.")
elif age >= 100:
    print("Age exceed to 100+. Enter your age again!")
elif age >= 18:
    print("You are now signed up!")
else: 
    print("You must be 18+ to sign up!")