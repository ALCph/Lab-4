#1.)
# Bug collecting
total_bugs = 0

# Day range and inputs
for day in range(1, 6):
    bugs_caught = int(input(f"Enter the number of bugs collected on day {day}: "))
# Totals
    total_bugs += bugs_caught

# Display the total number of bugs collected
print(f"You have collected: {total_bugs} bug(s)")
#-----------------------------------------------------------------

#2.)
# calorie counting
calorie_rate = 4.2
min_range = [10, 15, 20, 25, 30]

# Minutes range
for minutes in min_range:
    calorie_burn = calorie_rate * minutes
# How many have you burned
    print(f"After {minutes} minutes you have burned: {calorie_burn:.2f} calories")
#-----------------------------------------------------------------

#3.)
# Budgets
savedup = float(input('Enter your budget: '))
totalexp = 0
while True:
    expenses = input('Enter and expense or press "n" to stop: ')
    if expenses == 'n':
        break
    
    totalexp += float(expenses)
# The budget output
if totalexp < savedup:
    print(f"You are ${savedup - totalexp:.2f} under your budget")
elif totalexp > savedup:
    print(f"You are ${totalexp - savedup:.2f} over your budget")
else:
    print("You have spent exactly your budget.")
#-----------------------------------------------------------------

#4.)
# Trains
speed = int(input('Enter the speed of the train (in mph): '))
time = int(input('Enter the number of hours the train has traveled for: '))

# Distance outputs
# Was trying to do this as a While statement but it got too messy 
for hour in range(1, time + 1):
    distance = speed * hour
    print(f"{hour}\t{distance:.2f} miles")
#-----------------------------------------------------------------

#5.)
# Rainfall variables
total_rain = 0
total_month = 0
total_years = int(input('Enter the number of years: '))
# Rainfall limiters
for year in range(1, total_years +1):
    print(f'Year {year} rain values')
    # Months
    for month in range(1, 13):
        rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
        total_rain += rainfall
        total_month += 1
        
# Average formula
avg_rainfall = total_rain / total_month
# Rain outputs
print(f"\nNumber of months: {total_month}")
print(f"Total inches of rain: {total_rain:.2f}")
print(f"Average rain per month: {avg_rainfall:.2f}")
#-----------------------------------------------------------------

#6.)
# Temperature tables
for celcius in range(1, 21):
    faren = (9/5 * celcius) + 32
    print(f'{celcius} degree Celcius = {faren:.2f} degrees Farenheight')
#-----------------------------------------------------------------

#7.)
# A penny a day
totalpay = 0
dailyrate = 1
days = int(input('Enter the amount of days of work: '))
#the For statement
for i in range(1, days +1):
    payment = (0.01 * dailyrate)
    print(f'On day {i} you earned ${payment:.2f}')
    totalpay += payment
    dailyrate *= 2
# Total earnings
print(f'You have earned ${totalpay:,.2f} total')
#-----------------------------------------------------------------

#8.)
# Counting numbers
numtotal = 0
num = int(input('Enter the a positive number to continue, or a negative to end: '))
while True:
    if num > 0:
        numtotal += num
        num = int(input('Enter the a positive number to continue, or a negative to end: '))
    else:
        print(f'Total: {numtotal:,.2f}')
        break
#-----------------------------------------------------------------

#9.)
# The ocean is rising
ocean_rate = 1.6
total_rise = 0
for years in range (1, 26):
    total_rise += ocean_rate
    print(f'During year {years} the ocean level will have risen by {total_rise:,.2f} millimeters total.')
#-----------------------------------------------------------------

#10.)
# College tuition
#Semester variables
semester = 8000
interest = 0.03
# Calculating interests
for years in range (1, 6):
    year_cost = semester * (1 + interest)** years
    print(f'During year {years} the estimated cost of tuition for a semester will be {year_cost:,.2f}.')
