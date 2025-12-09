import mysql.connector as sql
import pandas as pd
from tabulate import tabulate
con=sql.connect(host='localhost', user='root', passwd='admin',database='tourism')
cur=con.cursor()

L=[]
cur.execute('select state,city,place from places')
d=cur.fetchall()
for i in range(len(d)):
    d[i]=list(d[i])
    d[i].insert(0,i+1)
    L.append(d[i])

df=pd.DataFrame(L,columns=['NO','STATE','CITY','PLACE'])
df=df.set_index('NO')
df.to_csv('report.csv',header=None)
print(tabulate(df,headers='keys',tablefmt='grid'))

print('\nNumber of places:',len(d))
cur.execute('select distinct city from places')
x=cur.fetchall()
print('\nNumber of cities:',len(x))
cur.execute('select distinct state from states')
l=cur.fetchall()
print('\nNumber of states:',len(l)) 


f=open('report.txt','r')
print('\n\nCONTENTS OF FILE:\n\n')
a=f.read()
print(a)
