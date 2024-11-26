weight = float(input("Enter your weight : "))
unit = input("Kilograms or Pounds? (K or L):  ")
if unit == "K":
    weight *= 2.205
    unit = "Lbs."
elif unit == "L":
    weight /= 2.205
    unit = "Kgs."
else:
    print("f{unit} was not valid")
print(f"your weight is : round({weight},3)" + f"{unit}")