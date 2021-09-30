from time import sleep

#do not change - define the sleep key, i want to keep it was sleep(1) - sleep(0.0001) or stuff like that.

def add(x,y):
    return x+y
    
def subtract(x,y):
    return x-y
    
def multiply(x,y):
    return x*y
    
def divide(x,y):
    return x/y

def power(x,y):
    return x^y

print('_________________________')   
print('What do you want to do?')
print('Addition')
print('subtraction')
print('multiplication')
print('division')
print('power')
print('_________________________')  

while True:
    choice=input('Choose either + (addition) or - (subtraction) or * (multiplication) or / (division) or ^ (power)|')
    print('_________________________')
    
    if choice in('+','-','*','/','^'):
        num1 = float(input('Type first number: '))
        num2 = float(input('Type second number: '))
        
        if choice == '+':
            print(num1, '+', num2, '=', add(num1, num2))
            
        elif choice == '-':
            print(num1, '-', num2, '=', subtract(num1, num2))
            
        elif choice == '*':
            print(num1, '*', num2, '=', multiply(num1, num2))
            
        elif choice == '/':
            print(num1, '/', num2, '=', divide(num1, num2))
            
        elif choice == '^':
            print(num1, '^', num2, '=', add(num1, num2))
            
        next_calculation = input('Want to ask another quetion? (yes/no)')
        if next_calculation == 'no':
            next_calculation = input('Do you want to determine a factorial then? (ok/no)')
            if next_calculation == 'ok':
                num = int(input("Enter a number: "))


                factorial = 1

                if num < 0:
                    print("Sorry, factorial does not exist for negative numbers")
                elif num == 0:
                    print("The factorial of 0 is 1")
                else:
                    for i in range(1,num + 1):
                        factorial = factorial*i
                print("The factorial of",num,"is",factorial)
                
            if next_calculation == 'no':
                break
        
        
        
else:
    print('invalid')




        elif choice == '-':
            print(num1, '-', num2, '=', subtract(num1, num2))
            
        elif choice == '*':
            print(num1, '*', num2, '=', multiply(num1, num2))
            
        elif choice == '/':
            print(num1, '/', num2, '=', divide(num1, num2))
            
        elif choice == '^':
            print(num1, '^', num2, '=', add(num1, num2))
            
        next_calculation = input('Want to determine a factorial? (yes/no)')
        if next_calculation == 'no':
            break
        
        
    else:
        print('invalid')


