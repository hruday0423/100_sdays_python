bill = int(input(('enter bill amount: $')))
tip = int(input('enter tip percentage:'))
number_of_people = int(input('enter no of people:'))
total_tip = round(bill*tip/100, 2)
total_bill = bill+total_tip
split_per_person = round(total_bill/number_of_people,2)
print(f'total bill is: {total_bill} and each person share is:{split_per_person}')