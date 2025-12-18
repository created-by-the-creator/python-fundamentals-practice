age = int(input("Enter your age: "))

if age <= 18 and age >= 12:
    print("Adolescense")
elif age <= 11 and age >= 6:
    print("Middle Childhood")
elif age <= 5 and age >= 3:
    print("Early/Preschool")
else:
    print("Possibly, Infant or a toodler at the moment.")


