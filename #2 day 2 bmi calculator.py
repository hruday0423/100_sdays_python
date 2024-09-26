height = float(input('enter your height in CM:'))/100
weight = float(input('enter your weight in KG'))
bmi = round(weight/height**2, 2)
print(f'Your bmi is:{bmi}')