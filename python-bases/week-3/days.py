from datetime import datetime, date

# Convert string to date
someone_birthday = "2002-04-19"
converted_date = datetime.strptime(someone_birthday, "%Y-%m-%d").date()

# Subtract the converted date from today
days_difference = (date.today() - converted_date).days
print("Days Difference:", days_difference)

