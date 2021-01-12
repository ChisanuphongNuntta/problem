Principal = float(input('Principal : '))
Interest = float(input('Interest : '))
Year = int(input('year : '))
Time = int(input('time : '))
Amount = 0

Amount = Principal*(1 + Interest / Time)**(Year * Time)

print('Total amount ',Amount)
print('Beginning Principal ',Principal)
print('Interest rate ',Interest)
print('Number_of_Tear ',Year)
print('Number_of_Time',Time)