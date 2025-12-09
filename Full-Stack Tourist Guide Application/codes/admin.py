#admin module
import pandas as pd
import mysql.connector as sql
from texttable import Texttable
from sys import exit
con=sql.connect(host='localhost', user='root', passwd='admin',database='tourism')
cur=con.cursor()

def ask():
    key='n'
    while key=='n':
        username=input('Enter the username:')
        password=input('Enter the password:')
        if (username =='Prajwal' and password == 'pr2903') or (username =='Kailash' and password =='msdcr7'):
            key='y'
            print('Accepted!')
            continue
        else:
            print('Invalid username/password! Enter again!')
            
'--------------------------------------------------------------------------------------------------------------------------------------'

def duplicate_chk(state,city,place=''):#checks if duplicate record exists in state master, called before inserting into tables.
    if city=='':
        q="SELECT STATE FROM STATES WHERE STATE='{}' AND TYPE='S'".format(state)
    elif city !='' and place=='' :
        q="SELECT STATE FROM STATES WHERE STATE='{}' and city='{}'".format(state,city)
    elif place !='' :
        q='SELECT STATE FROM PLACES WHERE STATE="{}" and city="{}" and place="{}"'.format(state,city,place)
    cur.execute(q)
    d=cur.fetchall()
    data=cur.rowcount
    return data
'--------------------------------------------------------------------------------------------------------------------------------------'

def table(field):
    if field=='S':
        cur.execute('select state from states where type="S"')
        data=cur.fetchall()
        l=[['STATE']]
        l1=[list(data[i]) for i in range(len(data))]
        t=Texttable()
        t.add_rows(l+l1)
        print(t.draw())

    elif field=='C':
        cur.execute('select state,city from states where type="C"')
        data=cur.fetchall()
        l=[['STATE','CITY']]
        l1=[list(data[i]) for i in range(len(data))]
        t=Texttable()
        t.add_rows(l+l1)
        print(t.draw())

    elif field=='P':
        cur.execute('select * from places')
        data=cur.fetchall()
        l=[['STATE','CITY','PLACE','DESCRIPTION']]
        l1=[list(data[i]) for i in range(len(data))]
        t=Texttable()
        t.add_rows(l+l1)
        print(t.draw())

    else:
        print('Invalid value entered!')
        
'--------------------------------------------------------------------------------------------------------------------------------------'
def edit_place(state,city):
    a=input('Do you want to edit place (P) or description (D) or both (PD)?').upper()
    if a=='P':
        o_pl=input('Enter old name of place:')
        pl=input('Enter new name of place:').upper()
        q='update places set place="{}" where state="{}" and city="{}" and place="{}"'.format(pl,state,city,o_pl)
        cur.execute(q)
        con.commit()
    elif a=='D':
        pl=input('Enter name of place:')
        desc=input('Enter description:')
        q='update places set description="{}" where state="{}" and city="{}" and place="{}"'.format(desc,state,city,pl)
        cur.execute(q)
        con.commit()
    elif a=='PD':
        o_pl=input('Enter old name of place:')
        pl=input('Enter new name of place:').upper()
        desc=input('Enter description:')
        q='update places set place="{}",description="{}" where state="{}" and city="{}" and place="{}"'.format(pl,desc,state,city,o_pl)
        cur.execute(q)
        con.commit()
    else:
        print('Invalid input!')
        edit_place(state,city)
'--------------------------------------------------------------------------------------------------------------------------------------'

def chk_city(city,state):
    sql_str="SELECT STATE FROM STATES WHERE STATE='{}' and CITY='{}' and type='C'".format(state,city)
    cur.execute(sql_str)
    res = cur.fetchall()
    data=cur.rowcount
    return data

'--------------------------------------------------------------------------------------------------------------------------------------'

def state_city(para):
    sqlstr=''
    ask_S=input('Enter state:').upper()
    if ask_S=='':
        state_city(para)
    if para=='C':
        while 1==1:
            ask_C=input('Enter city:').upper()
            if ask_C!='':
                1==2
                nCount = duplicate_chk(ask_S,ask_C)
                s="INSERT INTO STATES VALUES ('{}','{}','C')".format(ask_S,ask_C)
                cur.execute(s)
                con.commit()
                #con.close()
                while 1!=2:
                    confirm=input("Would you like to add another city?(Y/N) ").upper()
                    if confirm=='Y':
                        state_city(para)
                    elif confirm=='N':
                        print('Saved successfully')
                        break
                    else:
                        print('Enter again.')
                return True
            else:
                print('City field cannot be blank. Enter again!')
                
    elif para=='S':
        nCount = duplicate_chk(ask_S,"")
        if nCount==0:
            sqlstr="insert into states values('{}','','S')".format(ask_S)
            cur.execute(sqlstr)
            con.commit()
            #con.close()
            while 3==3:
                confirm=input("Would you like to add another state?(Y/N) ").upper()
                if confirm=='Y':
                    state_city(para)
                elif confirm=='N':
                    print('Saved successfully')
                    return True
                else:
                    print('Enter again')
    elif para=='P':
        while True:
            ask_C=input('Enter city:').upper()
            if ask_C=='':
                print('City field cannot be blank. Enter again!')
                return 'BLANK'
            else:
                nCount= chk_city(ask_C,ask_S)# checks if entered city and state exists
                if nCount==0: #Either state or city doesn't exist
                    print("City should exist before adding a place!\n")
                    return 'NON-EXISTENT'
                else:
                    ask_P=input("Enter place:").upper()
                    ask_Desc=input("Enter a description (OPTIONAL):")
                    if ask_P=='':
                        print('Enter place!')
                    else:
                        nCount = duplicate_chk(ask_S,ask_C,ask_P)
                        if nCount==0:
                            s='INSERT INTO PLACES VALUES ("{}","{}","{}","{}")'.format(ask_S,ask_C,ask_P,ask_Desc)
                            cur.execute(s)
                            con.commit()
                            #con.close()
                            confirm=input("Would you like to add another place for the same city ?(Y/N) ").upper()
                            if confirm=='Y':
                                state_city(para)
                            elif confirm=='N':
                                1==2
                                print('\nSaved successfully\n')
                                return True
                            else:
                                print('Enter again.')
                        else:
                            print("Duplicate entry - cannot save!")

'--------------------------------------------------------------------------------------------------------------------------------------'

def del_state_city(cond):
    ask_D=input('Enter the state to be deleted:')
    if cond=='S':
        if ask_D!='':
            sql_city="SELECT STATE FROM STATES WHERE TYPE='C' AND STATE='{}'".format(ask_D)
            cur.execute(sql_city)
            data=cur.fetchall()
            res=cur.rowcount
            if res>0:
                print('Cannot delete this state. City exists!')
            elif res==0:
                D="DELETE FROM STATES WHERE STATE='{}' AND TYPE='S'".format(ask_D)
                cur.execute(D)
                con.commit()
            else:
                print('Enter again!')
        else:
            print('Enter again!')

    elif cond=='C':
        1==2
        while 2==2:
            ask_cD=input('Enter the city to be deleted:')
            if ask_cD=='' and ask_D=='':
                print('Enter state/city again!')
            else:
                sqlQ="SELECT STATE,CITY,PLACE FROM PLACES WHERE STATE='{}' AND CITY='{}' AND PLACE=''".format(ask_D,ask_cD)
                cur.execute(sqlQ)
                data=cur.fetchall()
                res=cur.rowcount
                if res>0:
                    print('Cannot delete city!')
                elif res==0:
                    delete="DELETE FROM STATES WHERE STATE='{}' AND CITY='{}'".format(ask_D,ask_cD)
                    cur.execute(delete)
                    con.commit()
                    print('Successfully deleted')
                    break
                else:
                    print('Enter again')
    elif cond=='P':
        1==2
        while 2==2:
            ask_cdel=input('Enter the city:')
            ask_pdel=input('Enter the place to be deleted:')
            if ask_cdel=='' or ask_pdel=='':
                print('Enter all the details!')
            else:
                Del="DELETE FROM PLACES WHERE STATE='{}' AND CITY='{}' AND PLACE='{}'".format(ask_D,ask_cdel,ask_pdel)
                cur.execute(Del)
                con.commit()
                print('Successfully deleted!')
                break
    else:
        print('Enter again!\n')
        
'--------------------------------------------------------------------------------------------------------------------------------------'

def edit_state_city(para):
    global cur,con
    ask_S=input('Enter state:').upper()
    if ask_S=='':
        edit_state_city(para)
    if para=='C':
        while 1==1:
            ask_c=input('\nEnter old city name:').upper()
            ask_C=input('\nEnter new city name:').upper()
            if ask_C!='':
                1==2
                nCount = duplicate_chk(ask_S,ask_C)
                s="UPDATE STATES SET CITY='{}' WHERE STATE='{}' AND CITY='{}' AND TYPE='C'".format(ask_C,ask_S,ask_c)
                cur.execute(s)
                con.commit()
                while 1!=2:
                    confirm=input("\nWould you like to update?(Y/N) ").upper()
                    if confirm=='Y':
                        edit_state_city(para)
                    elif confirm=='N':
                        1==2
                        print('Saved successfully!')
                        break
                    else:
                        print('Enter again!')
                break
            else:
                print('City field cannot be blank. Enter again!')
                
    if para=='S':
        nCount = duplicate_chk(ask_S,"")
        if nCount==1:
            ask_ns=input('Enter new name:')
            sqlstr="update states set state='{}' where type='S' and state='{}'".format(ask_ns,ask_S)
            con=sql.connect(host='localhost', user='root', passwd='admin',database='tourism')
            cur=con.cursor()
            cur.execute(sqlstr)
            con.commit()
            while 3==3:
                confirm=input("Would you like to update anything else?(Y/N) ").upper()
                if confirm=='Y':
                    state_city(para)
                elif confirm=='N':
                    3==4
                    print('Change succesfully made!')
                    break
                else:
                    print('Enter again')

    if para=='P':
        ask_city=input('Enter city:')
        edit_place(ask_S,ask_city)

'--------------------------------------------------#main function--------------------------------------------------'
#ask()
def admin_menu():
    k='n'
    d=[
        ['FIELD','KEY'], 
        ['CITIES','C'],
        ['PLACES','P'],
        ['STATES','S'],
        ['LIST','L'],
        ['QUIT','Q']
      ]
    t=Texttable()
    t.add_rows(d)
    print(t.draw())
    while k=='n':
        sModule=input('WHICH FIELD DO YOU WANT TO CHOOSE [PRESS THE KEY] : ').upper()
        if sModule=='Q':
            a=input('Sure you want to quit? (y/n)')
            if a=='y':
                print('BYE!')
                exit()
            #con.close()
        elif sModule=='L':
            D={'No.':['STATE','CITY','PLACE']}
            con=sql.connect(host='localhost', user='root', passwd='admin',database='tourism')
            cur=con.cursor()
            cur.execute('select state,city,place from places')
            d=cur.fetchall()
            for i in range(len(d)):
                d[i]=list(d[i])
                for j in range(len(d)):
                    D[i+1]=d[i]
            col=['STATE','CITY','PLACE']
            df=pd.DataFrame(data=D).T

            df.to_csv('report.csv',header=False,encoding='utf-8',index=False)

            data=pd.read_csv('report.csv')
            print(data)
            print('\n')
        
        elif (sModule=='S' or sModule=='C' or sModule=='P') and sModule!='Q':
            sOpt=''
            con=sql.connect(host='localhost', user='root', passwd='admin',database='tourism')
            cur=con.cursor()
            table(sModule)
            con.close()
            while True:
                l=[
                    ['OPERATION','KEY'],
                    ['BACK','B'],
                    ['ADD','A'],
                    ['DELETE','D'],
                    ['EDIT','E']
                    ]
                T=Texttable()
                T.add_rows(l)
                print(T.draw())
                a=input('Press the key for the operation:' ).upper()
                if a=='A':
                    print('\n')
                    state_city(sModule)
                    print('\n')
                    admin_menu()
                elif a=='D':
                    print('\n')
                    del_state_city(sModule)
                    print('\n')
                    admin_menu()
                elif a=='E':
                    print('\n')
                    edit_state_city(sModule)
                    print('\n')
                    admin_menu()
                elif a=='B':
                    print('\n')
                    admin_menu()
                else:
                    print('\nInvalid input\n')
        else:
            print('\nInvalid input. Enter again!\n')

if __name__=='__main__':
    print('This is a module and it is not imported')
