print('welcome to pizza delovery')
size = input('enter the size of pizza you want, S,M,L').upper()
pepperoni = input('do you want pepporini?, y or N').upper()
cheese = input('do you want extra cheese? y or N').upper()
bill = 0
if size == 'S':

    print('you orderes a small pizza')
    bill+= 15
elif size==('M'):
    print('you ordered a medium pizza')
    bill+=20
elif size=='L':
    print('you ordered a large pizza')
    bill+=25
else:
    print('enter a valid size')
if pepperoni == 'Y':
    if size == 'S':
        bill+=2
    else:
        bill+=3
if cheese == 'Y':
     bill+= 1
print(f'your final bill is {bill}')


