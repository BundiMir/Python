seconds = int(input('Seconds after midnight: '))

hours = seconds // 3600
adjusted_h = hours if hours == 12 else hours % 12
min = round((seconds % 3600) / 60)
mins = min if min > 10 else ('0' + str(min))
daytime = ['AM', 'PM'] [hours >= 12]
print(str(adjusted_h) + ' : ' + str(mins) + str(daytime))
