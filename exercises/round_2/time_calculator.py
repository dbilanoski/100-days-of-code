'''
CHALLENGE: Time Calculator

## DESCRIPTION

Write a function named add_time that takes in two required parameters and one optional parameter:

    a start time in the 12-hour clock format (ending in AM or PM)
    a duration time that indicates the number of hours and minutes
    (optional) a starting day of the week, case insensitive

The function should add the duration time to the start time and return the result.

If the result will be the next day, it should show (next day) after the time. If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

## EXAMPLES

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)

Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.

'''

def add_time(start,duration,weekday=False):
  '''
    s - start
    d - duration
    t - total
    n - new

  ''' 
  # Gotten time variables
  s_hour, s_minute, s_meridian = tuple(start.replace(":"," ").split())
  d_hour, d_minute = tuple(duration.split(":"))

  # New time variables
  n_hour = 0
  n_minute = 0
  n_meridian = ""

  # Weekdays
  weekdays = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

  # Set hour to 24 hour format
  if s_meridian.lower() == "pm":
    s_hour = int(s_hour) + 12
  else:
    s_hour = int(s_hour)
  
  # Set totals and count days
  d_days = 0
  t_hour = s_hour + int(d_hour)
  t_minute = int(s_minute) + int(d_minute)

  # Set minutes
    # If minutes are more than 60, add one hour
  if t_minute > 60:
    t_hour += 1
    t_minute -= 60

    # If minutes are single digit number, add 0
  if t_minute < 10:
    n_minute =f"0{t_minute}"
  else:
    n_minute = t_minute

  # Set days
  d_days = t_hour // 24

  # Fix hours once days are counted, see what remains
  n_hour = t_hour % 24

  # If remainder is bigger than 12, meridian becomes PM
  # Fixing the 12 hours style
  # Case where hour is 0 we need 12 AM
  if n_hour == 0:
    n_hour = 12
    n_meridian = "AM"
  elif n_hour < 12:
  # Case where hour is < 12 we need current hour and AM
    n_meridian = "AM"
  elif n_hour == 12:
  # Case where hour is 12 we need PM
    n_meridian = "PM"
  else:
  # Case where hour is > 12 we need current hour - 12 and PM
    n_meridian = "PM"
    n_hour -= 12

  # Time statement
  days_passed = ""
  if d_days < 1:
    pass
  elif d_days == 1:
    days_passed = "(next day)"
  else:
    days_passed = f"({d_days} days later)"
  
  # Weekday clause & exit statiement
  if weekday != False:
    s_day_index = weekdays.index(weekday.lower())
    n_day_index = (s_day_index + d_days) % 7
    n_day = weekdays[n_day_index].capitalize()
    return f"{n_hour}:{n_minute} {n_meridian}, {n_day} {days_passed}".rstrip()
  else:
    return f"{n_hour}:{n_minute} {n_meridian} {days_passed}".rstrip()
   

# print(add_time("11:30 AM", "2:32", "Monday"))
# print(add_time("3:00 PM", "3:10"))
# print(add_time("10:10 PM", "3:30"))
# print(add_time("11:43 PM", "24:20", "tueSday"))
# print(add_time("11:40 AM", "0:25"))
# print(add_time("3:30 PM", "2:12", "Monday"))