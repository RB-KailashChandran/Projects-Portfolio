import mysql.connector as sql
from texttable import Texttable
con=sql.connect(host='localhost', user='root', passwd='admin',database='tourism')
cur=con.cursor()

def table(T):
    '''CREATES A TABLE USING THE GIVEN 2-D LIST'''
    t=Texttable()
    t.add_rows(T)
    print(t.draw())

def ret_rec(query):
    '''COUNTS THE NUMBER OF ROWS OBTAINED FROM THE QUERY'''
    cur.execute(query)
    data=cur.fetchall()
    count=cur.rowcount
    return count

def Index(dataset):
    n=len(dataset)
    c=[i+1 for i in range(n)]
    for i in range(n):
        dataset[i].insert(0,c[i])
    return dataset

def state():
    '''FETCHES THE STATE ENTERED'''
    cur.execute("select state from states where type='S';")
    r=cur.fetchall()
    L=[['NO.','STATE']]
    no=[i+1 for i in range(len(r))]
    l=[list(r[i]) for i in range(len(r))]
    c=Index(l)
    table(L+c)
    return L+c

def city(state):
    '''FETCHES THE ENTERED CITY IN THE STATE'''
    print('CITIES IN',state.upper())
    s='select city from states where state="{}" and type="c"'.format(state)
    cur.execute(s)
    d=cur.fetchall()
    C=[['CITY']]
    c=[list(d[i]) for i in range(len(d))]
    table(C+c)
    return c

def place(city,state):
    '''FETCHES THE ENTERED PLACE'''
    print('PLACES IN',city.upper())
    p='select place from places where city="{}" and state="{}"'.format(city,state)
    count=ret_rec(p)
    if count==0:
        return count
    else:
        cur.execute(p)
        m=cur.fetchall()
        P=[['PLACE']]
        p=[list(m[i]) for i in range(len(m))]
        table(P+p)
    return p,count

def state_menu():
    s=state()
    while True:
        State=input('Enter state:').upper()
        q='select state from states where type="S" and state="{}"'.format(State)
        cur.execute(q)
        data=cur.fetchall()
        count=ret_rec(q)
        if count==0:
            print('State not found! Enter again\n')
        else:
            break
    return State

def city_menu(S):
    b=city(S)
    while True:
        City=input('Enter a city:').upper()
        q='select city from states where city="{}" and state="{}"'.format(City,S)
        cur.execute(q)
        data=cur.fetchall()
        count=ret_rec(q)
        if count==0:
            print('City not found! Enter again')
        else:
            break
    return City

def place_menu(C,S):
    x=place(C,S)
    if x==0:
        print('Nothing!')
    else:
        while True:
            Place=input('Enter place:')
            q='select place from places where place="{}" and city="{}" and state="{}"'.format(Place,C,S)
            count=ret_rec(q)
            if count==0:
                print('Place not found! Enter again')
            else:
                break
        return Place

def main():
    while True:
        a=state_menu()
        d=city_menu(a)
        k=place_menu(d,a)
        ret='select description from places where state="{}" and city="{}" and place="{}"'.format(a,d,k)
        cur.execute(ret)
        d=cur.fetchall()
        l=[list(i) for i in d]
        d=[['DESCRIPTION']]
        table(d+l)
        q=input('Do you want to continue? (y/n)').upper()
        if q=='N':
            print('Thank you!')
            break
        elif q=='Y':
            continue
        else:
            print('Invalid input!')
    
if __name__=='__main__':
    print('This is a module and it is not imported')
