import sys
import random
import time

gap=1
MAX=100
dieface=6

e_snakes={
    15:7,
    35:13,
    24:19,
    42:23,
    66:17,
    97:79
    }

e_ladders={
    4:25,
    8:26,
    14:32,
    27:69,
    56:86,
    78:95,
    37:59,
    44:88,
    64:82
    }

m_snakes={
    25:6,
    32:16,
    45:18,
    58:26,
    67:33,
    76:38,
    93:46,
    96:54
    }

m_ladders={
    3:36,
    7:15,
    22:37,
    31:69,
    43:61,
    56:78,
    75:92
    }

h_snakes={
    24:2,
    35:16,
    47:32,
    50:15,
    58:21,
    66:3,
    74:10,
    79:44,
    82:41,
    99:13
    }

h_ladders={
    5:17,
    12:46,
    43:86,
    20:55,
    27:64
    }

player_turn_text = [
    "Come on buddy!",
    "Let us win it.",
    "Never give up.",
    "May the best one win!",
]

snake_bite = [
    "sssssssssss.........",
    "OMG!!",
    "Snake bite!!",
    "Noo!!!!!!!.",
]
    
ladder_climb = [
    "Yasssss!!!!",
    "Boom!!!",
    "OH YES!!!!!!",
    "Yes,yes,YES!!",
]    


def T_and_C():
    msg = """
    Welcome to Snake and Ladder Game. 
    
    TERMS AND CONDITIONS:
    
      1.KINDLY READ THE INSTRUCTIONS.
      
      2.IF YOU HAVE ANY IDEAS PLEASE SHARE IT WITH US PERSONALLY.
      
      3.DO SUGGEST THIS GAME TO YOUR FRIENDS AND RELATIVES.
      
      4.ONCE THE GAME STARTS, YOU CANNOT PAUSE THE GAME.
      """
    print(msg)

def rules():
    rul="""

                                                                      <<< RULES OR INSTRUCTIONS >>>

                                                 1.FIRST REGISTER YOUR ACTUAL AND PROPER NAME. SPECIAL CHARACTERS ARE NOT ALLOWED.

                                                 2.CHOOSE THE NUMBER OF PLAYERS YOU WANT.
        
                                                 3.TAKE TURNS TO ROLL THE DIE (PRESS 'ENTER' KEY TO ROLL THE DIE).

                                                 4.YOU CAN ALSO CHOOSE THE DIFFICULTY LEVEL.

      ======================================================== <<< ALL THE BEST TO WIN ALL THE 3 LEVELS >>> ========================================================
      
    """
    print(rul)


def die_val():
    time.sleep(gap)
    die_val=random.randint(1,dieface)
    print("\n" +">>>>>" + "It's a " + str(die_val))
    return die_val

def attack(oldval, val, player):
    print("\n" + random.choice(snake_bite).upper()+' ~~~~~~~~~~~~~~')
    print("\n" + player + ' was attacked!! Goes down from ' + str(oldval) + ' to ' + str(val))

def jump(oldval, val, player):
    print("\n" + random.choice(ladder_climb).upper()+' #################')
    print("\n" + player + ' stepped on a ladder!! Leaps from ' + str(oldval) + ' to ' + str(val))

def snake_ladder_easy(player, val, die_val,level):
    time.sleep(gap)
    oldval=val
    val=val+die_val

    if val > MAX:
        print('You need' + str(MAX - oldval) + 'to win this game. Try!!!!')
        return oldval

    print("\n" + player + " moved from " + str(oldval) + " to " + str(val))

    print("\n" + " =======> " + player + " is currently at " + str(val) )

    if level=='1':
        if val in e_snakes:
            fin_val=e_snakes.get(val)
            attack(val, fin_val, player)

        elif val in e_ladders:
            fin_val=e_ladders.get(val)
            jump(val, fin_val, player)
        else:
            fin_val=val
    elif level=='2':
        if val in m_snakes:
            fin_val=m_snakes.get(val)
            attack(val, fin_val, player)

        elif val in m_ladders:
            fin_val=m_ladders.get(val)
            jump(val, fin_val, player)

        else:
            fin_val=val
    elif level=='3':
        if val in h_snakes:
            fin_val=h_snakes.get(val)
            attack(val, fin_val, player)

        elif val in h_ladders:
            fin_val=h_ladders.get(val)
            jump(val, fin_val, player)

        else:
            fin_val=val

    return fin_val


def win_check(player, position):
    time.sleep(gap)
    if MAX == position:
        print("\n\n\n JACKPOT \n\n" + player + "! You made it, champ!!")
        print("Cheers" + player)
        while True:
            reply=input("\nDo you want to play again? [YES/NO]")
            if reply in ['YES','yes','Y','y']:
                start()
            if reply in ['NO','no','N','n']:
                print("\nThanks for playing the world's No.1 game.")
                sys.exit('Have a good day!!!')
            else:
                print('Is it a yes or a no??')

def start():
    rules()
    time.sleep(gap)
    menu="""
   

                                                                     ---- SNAKES AND LADDERS ----

                                                                          1) HAVE IT 'EASY'!

                                                                          2) PLAYING 'MEDIUM' -_-

                                                                          3) THE 'HARD' GAME! 

                                                                          4) TERMS 'n' CONDITIONS

                                                                          5) 'EXIT' --->
                                                       
           ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ """
    print(menu)
    print(end='')
    while True:
        inp=input('Select a number from 1-5 to choose what you want to do:')
            
        if inp=='1' or inp=='2' or inp=='3':
            print('PLEASE WAIT......')

            time.sleep(0.5)

            print('LOADING......')

            time.sleep(0.5)

            print('Done!')

            def mul_ply():
                
                pl=input('\nPlease input the number of players:')
                if not pl.isnumeric():
                    mul_ply()
                pl=int(pl)
                if pl not in [2,3,4]:
                    print("You can't play with more than 4 players nor can you play alone")
                    time.sleep(1)
                    mul_ply()
                    
                elif pl==2 or pl==3 or pl==4:
                    print('Initializing..........')
                    time.sleep(1)
                    print('All set!')
                    
                    def player1_name():
                        P1Name=None
                        P3Name=None
                        P4Name=None
                       
                        def check_splchar(sname):  #FUNCTION TO CHECK SPECIAL CHARACTERS IN NAMES
                            if sname=="":
                                return True
                                
                            list1=[]
                            list2=[]
                            specialchar="@_!#$%^&*()<>?/\|}{~:)`+=-*,."
                            list1 = list(specialchar)
                            list2 = list(sname)
                        
                            for i in range(0,len(list1)):
                                for j in range(0,len(list2)):
                                    if list1[i]==list2[j]:
                                        return True
                                        break
                            else:   
                                return False

                        for i in range(0,pl,1):
                            if (i==0):
                                scheck=True
                                while  not P1Name or (scheck==True):
                                    if scheck==True or (P1Name==None):
                                        P1Name = input("\nEnter a valid name for player 1 : ").strip()
                                        if P1Name!="":
                                            scheck= check_splchar(P1Name) 
                                        else:
                                            scheck=True
                                    else:
                                        break
                                
                            elif (i==1):
                                scheck=True
                                while  (scheck==True)  or (P2Name ==P1Name):
                                    if scheck==True or (P2Name ==P1Name) or P2Name==None:
                                        P2Name = input("\nEnter a valid name for player 2 : ").strip()
                                        scheck= check_splchar(P2Name) 
                                    else:
                                        break

                            elif (i==2):
                                scheck=True
                                while  scheck==True:
                                    if (scheck==True) or (P3Name in(P1Name,P2Name)) or P3Name==None :
                                        P3Name = input("\nEnter a valid name for player 3 : ").strip()
                                        scheck= check_splchar(P3Name) 
                                    else:
                                        break
                                
                            elif (i==3):
                                scheck=True
                                while  scheck==True:
                                    if (scheck==True) or (P4Name in(P1Name,P2Name,P3Name)) or P4Name==None :
                                        P4Name = input("\nEnter a valid name for player 4 : ").strip()
                                        scheck= check_splchar(P4Name) 
                                    else:
                                        break

                        if pl==2:
                            print("\nMatch will be played between '" + P1Name + "'and '" + P2Name + "'\n")
                            
                        elif pl==3:
                            print("\nMatch will be played between '" + P1Name + "' , '" + P2Name + "' and '" + P3Name + "'\n")

                        elif pl==4:
                            print("\nMatch will be played between '" + P1Name + "' , '" + P2Name + "' , '" + P3Name + "' and '" + P4Name + "'\n")

                        return P1Name,P2Name,P3Name,P4Name
                    P1Name,P2Name,P3Name,P4Name=player1_name()  
                        
                    time.sleep(gap)
                    P1_position = 0
                    P2_position = 0

                    while True:
                        time.sleep(gap) 
                        
                        input_1 = input("\n" + P1Name + ": " + random.choice(player_turn_text) + " Hit the 'enter' to roll the die: ")
                        print("\nRolling the die...")
                        dice_value = die_val()
                        time.sleep(gap)
                        print(P1Name + " moving....")
                        P1_position = snake_ladder_easy(P1Name, P1_position, dice_value,inp)
                        win_check(P1Name, P1_position)

                        input_2 = input("\n" + P2Name + ": " + random.choice(player_turn_text) + " Hit the 'enter' key to roll the die: ")
                        print("\nRolling the die...")
                        dice_value = die_val()
                        time.sleep(gap)
                        print(P2Name + " moving....")
                        P2_position = snake_ladder_easy(P2Name, P2_position, dice_value,inp)
                        win_check(P2Name, P2_position)

                        if pl>=3:
                            P3_position = 0
                            input_3 = input("\n" + P3Name + ": " + random.choice(player_turn_text) + " Hit the 'enter' key to roll the die: ")
                            print("\nRolling the die...")
                            dice_value = die_val()
                            time.sleep(gap)
                            print(P2Name + " moving....")
                            P3_position = snake_ladder_easy(P3Name, P3_position, dice_value,inp)
                            win_check(P3Name, P3_position)

                        if pl==4:
                            P4_position = 0
                            input_4 = input("\n" + P4Name + ": " + random.choice(player_turn_text) + " Hit the 'enter' key to roll the die: ")
                            print("\nRolling the die...")
                            dice_value = die_val()
                            time.sleep(gap)
                            print(P4Name + " moving....")
                            P4_position = snake_ladder_easy(P4Name, P4_position, dice_value,inp)
                            win_check(P4Name, P4_position)

            mul_ply()

            

        elif inp=='4' or inp=='RULES':
            T_and_C()
            time.sleep(0.5)
            while True:
                option=input('Press M (or m) to go to the menu or E (or e) to exit the game: ')
                if option == 'M' or option == 'm':
                    start()
                elif option == 'E' or option == 'e':
                    print('Exiting.....')
                    time.sleep(0.5)
                    print()
                    sys.exit('Have a good day!!!')
                else:
                    print('Enter again!')

        elif inp=='5' or inp=='EXIT':
            time.sleep(0.5)
            print('Exiting.....')
            time.sleep(0.5) 
            sys.exit('Have a good day!!!')

        else:
            print('Invalid input! Enter again!')

start()
