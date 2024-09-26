def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return(n1-n1)

def multiply(n1,n2):
    return(n1*n2)

def divide(n1,n2):
    return(n1/n2)

operands ={
    "+" : add,
    "-" : subtract,
    "*": multiply,
    "/":divide
}
num1 = float(input('enter your first number'))
calculate= True
while calculate:

    for symbol in operands:
        print(symbol)
    operation = input('enter the operation to be performed:')
    num2 = float(input('enter second numer:'))
    answer = operands[operation](num1,num2)
    print(f" {num1}  {operation} {num2}= {answer}")
    cont= input('enter "y" to continue with result, enter "n" to calculate new numbers:')
    if cont=='y':
        num1= answer
    else:
        print("\n"*20)



