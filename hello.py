import random
import clipboard
import os 


def pass_generator(length):
    print('====================WELCOME TO_RANDOM_password=Generator===============')
    ABC = 'ABCDEFGHIKLMNOPQRSTVXYZ'.lower().upper()
    
    # abc = 'abcdefghijklmnopqrstuvwxyz'
    
    digits = '0123456789'
    s_letters = '!@#$%{^&*()_+{:"?||~><'
    
    password = ABC + digits + s_letters

    if 8 <= length <= 699:
        result = ''.join(random.choices(password, k=length))
        clipboard.copy(result)
        with open("demo.txt" , 'w') as f:
            f.write("the file is saved \n")
            f.write(f'Your  Password is : {result} \n ')

           
            print('\n')
        os.system('notepad demo.txt')
        print('============================================================')
    else:
        print("FUCk off")

    


pass_generator(33)