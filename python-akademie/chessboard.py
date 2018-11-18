lenght = 5
char = ('#',' ')
desk = []

for l in range(lenght):
    line = []

    for r in range(lenght):
        i = (l+r) % len(char)
        line.append(char[i])
    
    desk.append(''.join(line))

print('\n'.join(desk))


    




