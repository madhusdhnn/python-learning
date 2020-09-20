print("Hello world")

int_var = 24
print(int_var)

float_var = 24.00343423
print(float_var)

string_var = "A String. Wow"
print(string_var)

bool_var = False
print(bool_var)

name = input("Enter your name: ")
print("Hey " + name)

birth_year = input("Enter your birth year to find age: ")
age = 2020 - int(birth_year)
print(age)

first = input("Enter first number: ")
second = input("Enter second number: ")
print(float(first) + float(second))

string_var = "an advertisement banner title"
print(string_var.upper())

print(string_var.find("an"))

string_var = "Replace for with number"
print(string_var.replace("for", "4"))

print("Replace" in string_var)

price = float(input("Enter the amount: "))
print(price > 10 or price < 20)
print(price > 0 and price >= 20)
print(not price > 0)

temperature = float(input("Enter your city's temperature: "))
if temperature > 35:
    print("It's a hot day")
    print("Stay healthy by driking more water")
elif 20 < temperature <= 35:
    print("Normal day")
elif 10 < temperature <= 20:
    print("Cold")
else:
    print("Very cold")
print("Done")
