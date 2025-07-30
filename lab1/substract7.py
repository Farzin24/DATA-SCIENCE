from datetime import datetime, timedelta

# Get current date
today = datetime.today()

# Subtract 5 days
new_date = today - timedelta(days=5)

# Print results
print("Today's Date:", today.strftime("%d-%m-%Y"))
print("Date 5 Days Ago:", new_date.strftime("%d-%m-%Y"))

