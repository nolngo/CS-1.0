print("Continental US Time Zone Calculator (Pacific Users Only)")  #This is the title of the program that greets the user.
print("Currently supported time zone inputs: Eastern, Central, Mountain")  #Shows the user a list of time zones they can use.

time_zone = input("Please choose your time zone (as listed above)") #
hours = int(input("What is the current hour?"))  #User is first asked for their current hour of their time. Since I will be doing operations on this, I converted it to an integer.
minutes = input("What is the current minutes?")  #User is then asked for the current minutes.

if time_zone == "Eastern":
    hours = (hours + 3) % 12
if time_zone == "Central":
    hours = (hours + 2) % 12
if time_zone == "Mountain":
    hours = (hours + 1) % 12
else:
    print("input error, please choose from listed time zones.")

if hours == 0:
    hours = 12
#In a 12-hour clock, there is no 0 hour, 0 is 12. The modulus does not include 12 because there is no remainder when remainder=modulus.

print(f"The current {time_zone} Daylight Time is {hours}:{minutes}")
#I used an F string to concatenate the time zone selected, with the hours and minutes in the correct standard format of time.