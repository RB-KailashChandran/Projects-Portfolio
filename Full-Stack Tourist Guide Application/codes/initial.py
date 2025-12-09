import mysql.connector as sql
con=sql.connect(host='localhost',user='root',passwd='admin')
cur=con.cursor()

cur.execute('create database tourism')
con.commit()
cur.execute('use tourism')
cur.execute("""create table states(
                                   state char(25) NOT NULL,
                                   city char(25) NOT NULL,
                                   type char(1) NOT NULL,
                                   PRIMARY KEY(state,city)
                                   )
            """)
con.commit()
cur.execute("""create table places(
                                   STATE char(25) NOT NULL,
                                   CITY char(25) NOT NULL,
                                   PLACE varchar(40) NOT NULL,
                                   DESCRIPTION blob,
                                   PRIMARY KEY(STATE,CITY,PLACE)
                                   )
            """)
con.commit()


