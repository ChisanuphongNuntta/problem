commission = int(input("Enter sale : "))
if commission > 2000 :
    if commission > 4000 :
        if commission > 6000 :
            print("Commission = .1")
        else:
            print("Commission = .07")
    else:
        print("Commission = .04")
else:
    print("commission = .02")