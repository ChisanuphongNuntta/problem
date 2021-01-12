hours = 0
pay_rate = 0
grosspay = 0


def read():
    global hours
    global pay_rate
    hours = int(input("Enter hours : "))
    pay_rate = int(input("Enter payrate : "))

def cal(pay_rate,hours):
    return pay_rate * hours

def print_0(resul):
    global hours
    global pay_rate

    print(cal(pay_rate,hours))

def main():
    s = 'y'
    while s.lower() == 'y':
        read()
        print_0()
        s = input('Do you want to cal again : ')
        
main()
