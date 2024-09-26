# for numbers from 1 to 100
# if number is divisible by 3 then it should give fizz instead of number
# if number is divisible by 5 then it should return buzz instead of number
# if number is divisible by both 3 and 5 then it should return FizzBuzz

for i in range(1,101):
    if i%3==0 and i%5==0:
        print('FizzBuzz')
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print('Buzz')
    else:
        print(i)

