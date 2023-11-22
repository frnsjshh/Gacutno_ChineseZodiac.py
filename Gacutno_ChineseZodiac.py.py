year = int(input("Enter your Birth year: "))
zodiac = year % 12

if zodiac == 0:
    print("Your Zodiac Sign is Monkey")
elif zodiac == 1:
    print("Your Zodiac Sign is Rooster")
elif zodiac == 2:
    print("Your Zodiac Sign is Dog")
elif zodiac == 3:
    print("Your Zodiac Sign is Pig")
elif zodiac == 4:
    print("Your Zodiac Sign is Rat")
elif zodiac == 5:
    print("Your Zodiac Sign is Ox")
elif zodiac == 6:
    print("Your Zodiac Sign is Tiger")
elif zodiac == 7:
    print("Your Zodiac Sign is Rabbit")
elif zodiac == 8:
    print("Your Zodiac Sign is Dragon")
elif zodiac == 9:
    print("Your Zodiac Sign is Snake")
elif zodiac == 10:
    print("Your Zodiac Sign is Horse")
elif zodiac == 11:
    print("Your Zodiac Sign is Goat")
else:
    print("Invalid input for the year")


"monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon", "snake", "horse", "sheep"