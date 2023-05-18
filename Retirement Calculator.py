# Create a program that determines how many years you have left until retirement and the year you can retire.

print("What is your current age? ")
current_age = int(input())
print("At what age would you like to retire? ")
retirement_age = int(input())
number_of_years = int(retirement_age - current_age)
print("What is the current year? ")
import datetime
today = datetime.date.today()
current_year = today.year
print(int(current_year))
print("What is the retirement")
retirement_year = current_year + number_of_years
print(int(retirement_year))
print("you have " + str(number_of_years) + " years left until you can retire.")
print("its " + str(current_year) + ", so you can retire in " + str(retirement_year)+".")
