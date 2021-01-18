money = int(input('Enter : '))
Bonus = 0
total = 0

if money > 2000:
    print('Youe receive bonus : 100')
    print('Your money : ',money)
    print('Total money : ',money+100)
elif money > 1000:
    print('Youe receive bonus : 50')
    print('Your money : ',money)
    print('Total money : ',money+50)
else:
    print('Youe receive bonus : 10')
    print('Your money : ',money)
    print('Total money : ',money+10)
