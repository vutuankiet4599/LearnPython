days = {
    '': '',
    'Monday': 0,
    'Tuesday': 1,
    'Wednesday': 2,
    'Thursday': 3,
    'Friday': 4,
    'Saturday': 5,
    'Sunday': 6
}

def add_time(start, duration, day_of_week=''):
    new_time = ''
    new_start = start.replace(' ', ':').split(':')
    start_hour, start_minute, start_meridiem = int(new_start[0]), int(new_start[1]), new_start[2]
    
    new_duration = duration.split(':')
    duration_hour, duration_minute = int(new_duration[0]), int(new_duration[1])

    if start_meridiem == 'PM':
        start_hour += 12
    
    new_minute = start_minute + duration_minute
    new_hour = start_hour + duration_hour

    new_hour += new_minute // 60
    new_minute = new_minute - (new_minute // 60) * 60

    days_after = new_hour // 24
    total_hour = new_hour
    new_hour = new_hour % 24

    str_minute = ''

    if new_minute < 10:
        str_minute = '0' + str(new_minute)
    else:
        str_minute = str(new_minute)

    if total_hour % 12 == 0 and total_hour % 24 != 0:
        new_time = '12' + ':' + str_minute + ' PM'
    elif new_hour > 12:
        new_time = str(new_hour - 12) + ':' + str_minute + ' PM'
    elif new_hour == 0:
        new_time = '12' + ':' + str_minute + ' AM'
    else:
        new_time = str(new_hour) + ':' + str_minute + ' AM'

    if day_of_week:
        day_of_week = day_of_week.capitalize()
        day_value = (days[day_of_week] + days_after) % 7
        day = list(days.keys())[list(days.values()).index(day_value)]
        new_time += f', {day}'

    if days_after == 1:
        new_time += ' (next day)'
    if days_after > 1:
        new_time += f' ({days_after} days later)'

    return new_time

print(add_time('2:59 AM', '24:00', 'saturDay'))