time = '18 : 35'

# solution1
if len(time) == 7:
    hour = int(time[:2]) - 12
    minute = int(time[5:7])
    print(str(hour) + ' : ' + str(minute))
else:
    print(time)

# solution2

hours, mins = time.split(':')

adjusted_h = hours if int(hours) == 12 else str(int(hours) % 12)

daytime = ['AM', 'PM'] [int(hours) >= 12]

print(adjusted_h + ' :' + mins + ' ' + daytime)

