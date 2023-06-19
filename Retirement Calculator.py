# Create a program that determines how many years you have left until retirement and the year you can retire.

current_age = int(input("What is your current age? "))
retirement_age = int(input("At what age would you like to retire? "))
number_of_years = int(retirement_age - current_age)
print("What is the current year? ")
import datetime
today = datetime.date.today()
current_year = today.year
print(int(current_year))
print("What is the year of retirement")
retirement_year = current_year + number_of_years
print(int(retirement_year))
print(f"you have {number_of_years} years left until you can retire.")
print(f"its {current_year}, so you can retire in {retirement_year}.")
