import random
attempts = 7

print('Im thinking of a number between 1 and 100...')
print(f'YOU HAVE {attempts}')

a = random.randint(1,100)

while attempts > 0:
    num =int(input("enter number Mf ?"))
    attempts -=1
    if(num == a):
        print("you Gussed right")
    elif(num>a):
        print("To high" , a)
        attempts -=1
    elif(num<a):
        print("to low")
        attempts -=1
    else:
        print("Wrong guess ")
    attempts -=1
    print(f'attempts left {attempts}\n')

if attempts == 0:
    print(f"Sorry, you lost! The correct number was: {a}")
