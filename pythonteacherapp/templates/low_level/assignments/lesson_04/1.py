name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (in meters): "))

if age >= 18:
    print(name + ", you are old enough to vote.")
else:
    print(name + ", you are not old enough to vote.")

print("Your height is", height, "meters.")
