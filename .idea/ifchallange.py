name = input("Enter your name: ")
age = int(input("Please enter your age: "))

if (age >= 18) and (age <= 31):
    print("Welcome aboard {0}! Enjoy your stay with us." .format(name))

elif (age < 18):
    print("This is an adult's only hotel, come back in {0} years, {1}." .format(18 - age, name))

else:
    print("Your too old for this, {0}, we party too hard." .format(name))
