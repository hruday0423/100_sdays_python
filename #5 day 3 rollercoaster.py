print('welcome to rollercoaster ride')
height = int(input('enter your height in CMS:'))
bill= 0
if height>= 120:
    print('you can have a ride')
    age = int(input('enter your age:'))
    if age<=12:
        bill += 5
    elif age<=18:
        bill+=8
    elif 45<age<55:
        print('enjoy your free ride')
    else:
        bill+=12
    wants_photo = input('do you want a photo?, Y, N').upper()
    if wants_photo =='Y':
        bill+=3
    print(f'your total bill is {bill}')
else:
    print('sorry you cant ride this,please enjoy our other rides')
