"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def convert_to_fahrenheit():
    return celsius * 9.0 / 5 + 32


def convert_to_celsius():
    return 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = convert_to_fahrenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        fahrenheit = float(input("Fahrenheit: "))
        celsius = convert_to_celsius()
        print("Result: {:.2f} F".format(celsius))
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")


