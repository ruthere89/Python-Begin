world_message = "Good Day to you all!"
# world message meant to be for everyone, not specifically for you
print(world_message)
print("Today is:")
# pulling date and time
from datetime import date
today_date = date.today()
print(today_date)
# user input
response_q1 = input("Are you doing well? Yes or No?")

if: response_q1 =='Yes','yes','Y','y'
    print("That is GREAT!")
else:
    print("Go get you some MILK")