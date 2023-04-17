# Write your solution here
#yyyy-mm-dd
from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birth = datetime(year, month, day)
mil = datetime(1999, 12, 31)
result = mil - birth
if birth > mil:
    print("You weren't born yet on the eve of the new millennium.")
else:
    print(f"You were {result.days} days old on the eve of the new millennium.")





