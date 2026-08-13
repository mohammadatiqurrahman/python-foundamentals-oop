correct_pin = '1234'
max_attempt = 3
while True:
    pin = input()
    
    if pin==correct_pin:
        print('Access Granted')
        break
    else:
        if max_attempt == 1:
            print('Card Blocked')
            break
        else:
            max_attempt -= 1