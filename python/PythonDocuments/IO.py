def is_leap_year(year):
    if (year % 4 == 0):
        return True
    else:
        return False


# Take user input
year = int(input("Enter a year: "))

# Check if it's a leap year
if is_leap_year(year):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")

# Take user input
year = int(input("Enter a year: "))

if (year % 4 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is NOT a Leap Year.")
