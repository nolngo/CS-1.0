print("Continental US Time Zone Calculator (Pacific Users Only)") #This is the title of the program that greets the user
print("Currently supported time zone inputs: Eastern, Central, Mountain")

time_zone = input("Please choose your time zone (as listed above)")
hours = int(input("What is the current hour?"))
minutes = int(input("What is the current minutes?"))

if time_zone == "Eastern":
    hours = (hours + 3) % 12
if time_zone == "Central":
    hours = (hours + 2) % 12
if time_zone == "Mountain":
    hours = (hours + 1) % 12

if hours == 0:
    hours = 12
print(f"The current {time_zone} Daylight Time is {hours}:{minutes}")
