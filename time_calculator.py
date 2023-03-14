def add_time(start,duration,day_of_week=None):
    #Setting some variables
    days_passed = 0
    days_of_the_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    current_day_index = 0
    le_day = ''
    if day_of_week != None:
        today = day_of_week.title()

    # Fetching the starting time and additional time data
    start_temp = start.split(' ')
    start = start_temp[0].split(':')
    start.append(start_temp[1])
    start_time_hours = int(start[0])
    start_time_minutes = int(start[1])
    start_meridiem = start[2]
    le_meridiem = ''
    # Converting to a 24 hour format
    if start_meridiem == 'PM':
        start_time_hours += 12
    # Fetching the duration time data
    duration = duration.split(':')
    duration_hours = int(duration[0])
    duration_minutes = int(duration[1])

    # Adding the hours
    new_hours = start_time_hours + duration_hours
    new_minutes = start_time_minutes + duration_minutes
    # Calculating excess new minutes (above 60)
    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60

    # Calculating days passed
    if new_hours >= 24:
        days_passed += (new_hours // 24)
        new_hours = (new_hours % 24)
    if new_hours == 0:
        new_hours += 24


    # Calculating the meridiem
    if new_hours < 12:
        le_meridiem = 'AM'
    if new_hours >= 12:
        le_meridiem = 'PM'
    if new_hours == 24:
        le_meridiem = 'AM'


    #Converting the time format back to 12 hours
    if new_hours > 12:
        new_hours -= 12



    # Converting the results into strings
    str_hours = str(new_hours)
    if new_minutes < 10:
        str_minutes = f'''0{new_minutes}'''
    else:
        str_minutes = str(new_minutes)
    if days_passed == 0:
        str_days_passed = ''
    if days_passed == 1:
        str_days_passed = ' (next day)'
    if days_passed > 1:
        str_days_passed = f''' ({days_passed} days later)'''

    #Calculating the correct day
    if day_of_week != None:
        if today == 'Monday':
            current_day_index = 0
        if today == 'Tuesday':
            current_day_index = 1
        if today == 'Wednesday':
            current_day_index = 2
        if today == 'Thursday':
            current_day_index = 3
        if today == 'Friday':
            current_day_index = 4
        if today == 'Saturday':
            current_day_index = 5
        if today == 'Sunday':
            current_day_index = 6
        if (days_passed % 7)!= 6:
            le_day = days_of_the_week[current_day_index + (days_passed % 7)]
        else:
            le_day = days_of_the_week[0]


    if day_of_week != None:
        time = f'''{str_hours}:{str_minutes} {le_meridiem}, {le_day}{str_days_passed}'''
    else:
        time = f'''{str_hours}:{str_minutes} {le_meridiem}{str_days_passed}'''

    return time
