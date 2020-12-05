#first commit
speed = int(input('what speed?: '))
hours = int(input('what hours?: '))
start_speed = 1

print('Время (час)\tРасстояние km')
print('____________________________')

for hours in range(start_speed,hours+1):
    distance = hours*speed
    print(hours, '\t\t', distance)
print('ИТОГО: за ',hours,'часов, пройдено ',distance,'километров')

