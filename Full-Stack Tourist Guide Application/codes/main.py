from admin import *
from places import *
from sys import exit
while True:
    a=input("""\nSelect:\n
'A' if you are an admin

'C' if you are a customer

'Q' to quit:""").upper()
    if a=='A':
        ask()
        admin_menu()
        
    elif a=='C':
        A=main()
        if A=='BYE!':
            pass
    elif a=='Q':
        print('BYE!')
        exit()
    
    else:
        print('Enter again')
