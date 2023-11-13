from datetime import datetime, date

# Convert string to date object
someone_birthday = "1995-04-19"
converted_date = datetime.strptime(someone_birthday, "%Y-%m-%d").date()

# Print the converted date
print("Converted Date:", converted_date)

# Subtract the converted date from today
days_difference = (date.today() - converted_date).days
print("Days Difference:", days_difference)