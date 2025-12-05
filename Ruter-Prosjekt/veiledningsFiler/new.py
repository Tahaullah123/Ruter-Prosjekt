from datetime import datetime

# Define the date/time string
date_string = "2025-11-19 11:10:00"

# Define the format code string matching the date_string
# %Y for full year, %m for month, %d for day,
# %H for hour (24-hour), %M for minute, %S for second
format_code = "%Y-%m-%d %H:%M:%S"

# Parse the string into a datetime object
datetime_object = datetime.strptime(date_string, format_code)

# Print the resulting datetime object
print(datetime_object)