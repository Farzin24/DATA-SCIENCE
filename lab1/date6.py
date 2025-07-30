from datetime import datetime

# Input format: DD-MM-YYYY
date1_str = input("Enter the first date (DD-MM-YYYY): ")
date2_str = input("Enter the second date (DD-MM-YYYY): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date1_str, "%d-%m-%Y")
date2 = datetime.strptime(date2_str, "%d-%m-%Y")

# Compare dates
if date1 < date2:
    print(f"{date1_str} is earlier than {date2_str}")
elif date2 < date1:
    print(f"{date2_str} is earlier than {date1_str}")
else:
    print("Both dates are the same.")

