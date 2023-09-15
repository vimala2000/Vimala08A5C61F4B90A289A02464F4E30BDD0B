years = ["Not a leap year", "Leap year"]
year = int(input("Enter a year: "))
result = years[(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
print(f"{year} is a {result}.")
