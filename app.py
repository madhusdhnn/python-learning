from os import remove

from restaurant.multi_cuisine import MultiCuisineChef
from restaurant.non_vegetarian import NonVeganChef
from restaurant.vegetarian import VeganChef
from utils.pair_utils import create_pair

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

f = input("Enter first number: ")
s = input("Enter second number: ")
print(float(f) + float(s))

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
    print("Stay healthy by drinking more water")
elif 20 < temperature <= 35:
    print("Normal day")
elif 10 < temperature <= 20:
    print("Cold")
else:
    print("Very cold")
print("Done")

i = 0
while i <= 20:
    print(i)
    i += 1
print("Loop Done")

for j in range(10, 20, 3):
    print(f"j: {j}")

list_var = [1, 2, 3, 4]
print(f"List {list_var}")

tuple_var = (1, 2, 3)
print(f"Immutable list {tuple_var}")

dictionary = {"a": 'dsf', "b": 'dfs', "c": "bye"}
print(f"Dictionary {dictionary}")
print(f"Values of a dictionary {dictionary.values()}")


def predict_key_value(dictionary_var, key):
    print("Thank God" if dictionary_var.get(key) is not None else "Oops")


def greet_message(username):
    return f"Hey, {username}. What's up?"


predict_key_value(dictionary, "a")
predict_key_value(dictionary, "d")

print(greet_message("TheTechMaddy"))


def simple_interest_calculator():
    rate_of_interest = 11.4
    try:
        principle = float(input("Input principle amount: "))
        no_of_years = int(input("Input number of years: "))
        simple_interest = principle * (1 + (rate_of_interest / 100) * no_of_years)
        print(f"Simple interest for {principle} amount to pay in {no_of_years} year(s) is {simple_interest}")
    except ValueError:
        print("Inputs should be only numbers")


simple_interest_calculator()

p1 = create_pair(1, 2)
p2 = create_pair(0, 2)
print(f"first={p1.first}, second={p1.second}")
print(f"first={p2.first}, second={p2.second}")


def safe_remove_file():
    try:
        remove("top_students.txt")
    except FileNotFoundError:
        pass


safe_remove_file()


def extract_top_students(input_file, output_file):
    try:
        top_students = open(output_file, "a")
        text_file = open(input_file, "r")

        for line in text_file.readlines():
            if int(line.split("-")[1]) > 80:
                top_students.write(f"{line}")

        text_file.close()
        top_students.close()
    except FileNotFoundError as e:
        print(e)


extract_top_students("students.txt", "top_students.txt")

chef_one = MultiCuisineChef("Chandler")
chef_one.make_sandwitch()
chef_one.make_chicken()
chef_one.make_veg_burger()

chef_two = VeganChef("Phoebe")
chef_two.make_sandwitch()
chef_two.make_veg_meal()

chef_three = NonVeganChef("Joey")
chef_three.make_sandwitch()
chef_three.make_bbq()
