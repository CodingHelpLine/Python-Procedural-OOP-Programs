'''
Simple Temperature conversion
'''

# Convert from Celsius to Fahrenheit
def cToF(celsius):
    return (celsius * 9.0/5.0) + 32


# function convert Fahrenheit to Celsius
def fToC(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0


# Function Celsius to Kelvin
def cToK(celsius):
    return celsius + 273.15


# Function to convert Kelvin to Celsius
def kToC(kelvin):
    return kelvin - 273.15


# Function Fahrenheit to Kelvin
def fToK(fahrenheit):
    return cToK(fToC(fahrenheit))


# Function to convert kelvin to Fahrenheit
def kToF(kelvin):
    return cToF(kToC(kelvin))


# Menu function - display menu and get user's choice
def menu():
    print("Welcome to Temperature Menu")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print('3. Celsius to Kelvin')
    print('4. Kelvin to Celsius')
    print('5. Fahrenheit to Kelvin')
    print('6. Kelvin to Fahrenheit')
    print('0. Exit')
    userChoice = -1

    while userChoice < 0 or userChoice > 6:
        userChoice = int(input("Enter choice: "))

        if userChoice < 0 or userChoice > 6:
            print("Invlaid input - enter 0-6")

    return userChoice


if __name__ == "__main__":

    choice = menu()

    while choice != 0:

        # Read input
        value = float(input("Enter temperature to convert: "))

        if choice == 1:
            # c to f
            print(f"{value:.2f} Celsius to Fahrenheit {cToF(value):.2f}")
        elif choice == 2:
            # f to c
            print(f"{value:.2f} Fahrenheit to Celsius {fToC(value):.2f}")
        elif choice == 3:
            # c to k
            print(f"{value:.2f} Celsius to Kelvin {cToK(value):.2f}")
        elif choice == 4:
            # k to c
            print(f"{value:.2f} Kelvin to Celsius {kToC(value):.2f}")
        elif choice == 5:
            # f to k
            print(f"{value:.2f} Fahrenheit to Kelvin {fToK(value):.2f}")
        elif choice == 6:
            # k to f
            print(f"{value:.2f} Kelvin to Fahrenheit {kToF(value):.2f}")
        else:
            print("GoodBye!......")

        print()

        choice = menu()