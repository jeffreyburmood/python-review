"""Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock."""

def timeConversion(s:str) -> str:
    ampm = s[-2:]
    time = s[2:8]
    hour = int(s[0:2])
    if(ampm == 'AM'):
        if(hour == 12):
            newHour = '00'
        else:
            newHour = s[0:2]
        newTime = newHour + time

    else:
        if(hour < 12):
            hour += 12
        newHour = str(hour)
        newTime = newHour + time

    return newTime

print(timeConversion('12:01:00PM'))
print(timeConversion('01:01:00PM'))
print(timeConversion('01:23:23AM'))
print(timeConversion('12:01:01AM'))