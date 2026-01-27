from datetime import date

today = date.today()

day_of_year = today.strftime("%j")
week_number = today.strftime("%W")

print(f"Day of the year: {day_of_year}")
print(f"Week number: {week_number}")
