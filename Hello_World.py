numbers = []
while len(numbers) < 5:
    x = input("Please enter input number: ")
    try:
        x = int(x)
    except ValueError:
        print("that's not a vaild number. please enter a number")
    numbers.append(x)
print("The list of numbers is: ", numbers)
animals = []
while len(animals) < 5:
    x = input("Please enter an animal name: ")
    animals.append(x)
print("The list of animals you entered is: ", animals)
