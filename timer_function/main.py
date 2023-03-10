#import datetime for clock
import datetime
import time
#define a yes/no list
yes_list = ['yes', 'yup', 'yeah', 'sure', 'y']
no_list = ['no', 'nope', 'nah', 'n']
#print hello and get a name
print ("Hello there!")
char_name= input("What is your name? ")
# Use name
print("Thank you, " + str(char_name).title())
#trying something I just learned floating a sleep from time
time.sleep(0.5)
#define how time should appear by providing a date
from datetime import date
today_1 = date.today()
d1 = today_1.strftime("%B %d, %Y")
print("Just to let you know, today is " + str(d1))
#did it again
time.sleep(2)
#searching list for response
answer_a = input("Would you like to start a small workout? ").lower()
if answer_a in yes_list:
    print ("Fantastic!")
else:
    exit()
activ = input("What will you do? ").upper()
#fun bits for the workout timer
def countdown(hr, min, sec):
    total_sec = hr * 3600 + min * 60 + sec
    #check to see if timer is out
    while total_sec > 0:
        cdown_t = datetime.timedelta(seconds = total_sec)
        time.sleep(1)
        total_sec -= 1
        print(cdown_t, end="\r")
        #reduced the count by one after printing a timer to repeat on an ended string
    print("Yo shorty, time's up!")
    time.sleep(0.5)
    print("I hope your " + activ + " was/were successful!")
# grab some inputs
time.sleep(1)
print("Please enter a number for hours, minutes, and seconds. If you would like to skip a time period, please type 0")
hr = input("Hours: ")
min = input("Minutes: ")
sec = input("Seconds: ")
print("Don't worry, you have 10 seconds to get ready.")
time.sleep(10)
countdown(int(hr), int(min), int(sec))
