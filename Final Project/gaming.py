import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")
def Specific(_conn):
    print("How would you like to search the games")
    print("By 1)price 2)date 3)genre 4)discount")
    specific=input()
    if specific.isalpha():
        print("error")
        Specific(_conn)
    if specific.isdigit():
        if int(specific)<5:
            if int(specific)==1:
                print("By How much")
                pricing=input()
                
                
                cur=_conn.cursor()
                cur.execute("""Select g_name,g_prices,g_date FROM Games where g_prices <= ?""",[pricing])
        
                rows = cur.fetchall()
                cNames = "{:>0}|\t\t\t\t{:>0}|\t{:>5}|\n".format("g_name", "g_prices", "g_date")
                print(cNames)
                for row in rows:
                    l = '{:>0}|\t\t\t\t{:>0}|{:>5}'.format(row[0], row[1],row[2])
                    print(l)
                print("Search Again?")
                Specific(_conn)
            if int(specific)==2:
                print("By what month")
                month=input()

                cur=_conn.cursor()
                cur.execute("""Select g_name,g_prices,g_date FROM Games where g_date LIKE ?""",["%"+month+"/%"])
        
                rows = cur.fetchall()
                cNames = "{:>0}|\t\t\t\t{:>0}|\t{:>5}|\n".format("g_name", "g_prices", "g_date")
                print(cNames)
                for row in rows:
                    l = '{:>0}|\t\t\t\t{:>0}|{:>5}'.format(row[0], row[1],row[2])
                    print(l)
                print("Search Again?")
                Specific(_conn)
            if int(specific)==3:
                print("By what genre")
                genre=input()

                cur=_conn.cursor()
                cur.execute("""Select g_name,g_prices,g_genre FROM Games where g_genre LIKE ?""",["%"+genre+"%"])
        
                rows = cur.fetchall()
                cNames = "{:>0}|\t\t\t\t{:>10}|{:>10}|\n".format("g_name", "g_prices", "g_genre")
                print(cNames)
                for row in rows:
                    l = '{:>0}|\t\t\t\t{:>10}|{:>10}'.format(row[0], row[1],row[2])
                    print(l)
                print("Search Again?")
                Specific(_conn)
            if int(specific)==4:
                print("What game or id would you like to see offers discount")
                discount=input()
                if discount.isdigit():
                    cur=_conn.cursor()
                    cur.execute("""SELECT g_prices-(g_prices*(s_discount/(100.0))) as total,s_name,g_name,s_discount
                                FROM Games,stores
                                WHERE g_id=s_gid and s_discount LIKE ? """,["%"+str(discount)+"%"+"%"])
        
                    rows = cur.fetchall()
                    cNames = "{:>0}| {:>0}|{:>0}|{:>0}  \n".format("total","s_name","g_name","s_discount")
                    print(cNames)
                    for row in rows:
                        l = '${:>0}|{:>0}|{:>0}|{:>0} '.format(row[0],row[1],row[2],row[3])
                        print(l)
                    print("Search Again?")
                    Specific(_conn)
                    
                
            
            
            
   
   
   
   
   
   
   
   
   
   
   
   
    
def INSERT(_conn):
    print("Add  name")
    name=str(input())
   
    print("Add prices")
    prices=input()
    while prices.isalpha():
        print("Bad user int only")
        print("Add prices")
        prices=input()
        
        
    
    
    print("Add units sold")
    sold=input()
    while sold.isalpha():
        print("Bad user int only")
        print("Add prices")
        sold=input()
        
    print("Add month int")
    month=input()
    while month.isalpha():
        print("add month")
        month=input()
    if month.isdigit():
        while int(month)>12 or int(month)<=0:
            print("add month")
            month=input()
            while month.isalpha():
                print("add month")
                month=input()
        
                    
        
    print("Add day int")
    day=input()
    while day.isalpha():
        print("day")
        day=input()
    if day.isdigit():
        while int(day)>31 or int(day)<=0:
            print("add day")
            day=input()
            while day.isalpha():
                print("add day")
                day=input()
    
    print("Add genre")
    genre=str(input())
    try:
        cursor=_conn.cursor()
        cursor.execute("""SELECT count(g_name) FROM GAMES""")
        _conn.commit()
        ids = cursor.fetchall()
        for id in ids:
            format(id)
        result = int(id[0])
        results=result+1
        cursor=_conn.cursor()
        cursor.execute("""INSERT INTO Games(g_name,g_id,g_prices,g_sold,g_date,g_genre)
        Values(?,?,?,?,?,?)""",(name,results,int(prices),float(sold),str(month)+"/"+str(day)+"| ",genre))
        _conn.commit()
        print("success")
        print("g_name,| g_id,| g_prices,| g_sold,| g_date,| g_genre")
        print(name,"\t|"+str(results)+"|",prices,"| "+str(sold),"| "+str(month)+"/"+str(day),genre)
    except Error as e:
        _conn.rollback()
        print(e)


def UPDATE(_conn):
    print("Choose what needs to be updated")
    print("1.Price")
    print("2.Units sold")
    x=int(input())
    while x>1 and x>2:
        if x>1 and x>2:
            print("Error")
            print("Choose what needs to be updated")
            print("1.Price")
            print("2.Units sold")
            x=int(input())
    if x==1:
            print("What game name or id needs to be updated")
            game=input()
            
            print("What is their new price")
            price=float(input())
            if game.isdigit():
                
                try:
                    sql="UPDATE Games SET g_prices= ? WHERE g_id =?" 
                    _conn.execute(sql,[price,game])
                    _conn.commit()
                    
                except Error as e:
                    _conn.rollback()
                    print(e)
            
            else:
                try:
                    sql="UPDATE Games SET g_prices= ? WHERE g_name=?" 
                    _conn.execute(sql,[price,game])
                    _conn.commit()
                    
                except Error as e:
                    _conn.rollback()
                    print(e)
            
                 
    
    if x==2:
            print("What game needs to be updated")
            game=input()
            print("What is their new amount of units sold")
            sold=float(input())
            if game.isdigit():
                try:
                    sql="UPDATE Games SET g_sold= ? WHERE g_id=?" 
                    _conn.execute(sql,[sold,game])
                    _conn.commit()  
                
                except Error as e:
                    _conn.rollback()
                    print(e)
                
            else:    
                try:
                    sql="UPDATE Games SET g_sold= ? WHERE g_name=?" 
                    _conn.execute(sql,[sold,game])
                    _conn.commit()  
                
                except Error as e:
                    _conn.rollback()
                    print(e)
def DELETE(_conn):
    print("What table would you like to select:Select by number")
    print("1)Games, 2)console, 3)reviews, 4)stores, 5)developer")
    x=int(input())
    
    while x>0 and x>5:
        if x>0 and x>5:
            print("What table would you like to select:Select by number")
            print("1)Games, 2)console, 3)reviews, 4)stores, 5)developer")
            x=int(input())
            
    if x==1:
        print("What is the name or id of the game you like to delete")
        name=input()
        if name.isdigit():
            
            try:
                
                cursor=_conn.cursor()
                cursor.execute("""SELECT count(g_name) FROM GAMES""")
                _conn.commit()
                ids = cursor.fetchall()
                for id in ids:
                    format(id)
                result = int(id[0])
                results=result+1
                if results<=int(name):
                    print("You lose,You get nothing!!! Good day sir")
                    print("Search again?")
                    DELETE(_conn)
                sql="DELETE FROM  Games Where g_id=?"
                _conn.execute(sql,[name])
                _conn.commit
            
            except Error as e:
                    _conn.rollback()
                    print(e)
        else:
            try:
                sql="DELETE FROM  Games Where g_name=?"
                _conn.execute(sql,[name])
                _conn.commit
            
            except Error as e:
                _conn.rollback()
                print(e)
    
            
    
    if x==2:
        print("What is the name of the console name you like to delete")
        name=input()
        try:
            sql="DELETE FROM  console Where c_name=?"
            _conn.execute(sql,[name])
            _conn.commit
            DELETE(_conn)
        except Error as e:
                _conn.rollback()
                print(e)
    if x==3:
        print("What is the name of the review you like to delete")
        name=input()
        try:
            sql="DELETE FROM  reviews Where r_name=?"
            _conn.execute(sql,[name])
            _conn.commit
            DELETE(_conn)
        except Error as e:
                _conn.rollback()
                print(e)
    if x==4:
        print("What is the name of the store you like to delete")
        name=input()
        try:
            sql="DELETE FROM  stores Where s_name=?"
            _conn.execute(sql,[name])
            _conn.commit
            DELETE(_conn)
        except Error as e:
                _conn.rollback()
                print(e)
    if x==5:
        print("What is the name of the developer you like to delete")
        name=input()
        try:
            sql="DELETE FROM  developer Where d_name=?"
            _conn.execute(sql,[name])
            _conn.commit
            
        except Error as e:
                _conn.rollback()
                print(e)
    if x==0:
        main()
    print("DELETION SUCESSFUL")
    
    

def SEARCH(_conn):
    print("Press 0 to exit")
    print("What is the game name or id you would like to search?")
    print("press enter to see list")
    y=input()
    if y=="0":
        main()
    if y.isdigit():
        if int(y)>0: 
            cursor=_conn.cursor()
            cursor.execute("""SELECT count(g_name) FROM GAMES""")
            _conn.commit()
            ids = cursor.fetchall()
            for id in ids:
                format(id)
            result = int(id[0])
            results=result+1
            if results<=int(y):
                print("You lose,You get nothing!!! Good day sir")
                print("Search again?")
                SEARCH(_conn)
            cur=_conn.cursor()
            cur.execute("""Select * FROM Games where g_id=?""",[y])
        
            rows = cur.fetchall()
            cNames = "{:>0}|\t\t\t\t{:>0}|\t{:>5}|\t{:>5}|\t{:>5}|\t{:>5}\n".format("g_name", "g_id", "g_prices","g_sold","g_date","g_genre")
            print(cNames)
            for row in rows:
                l = '{:>0}|\t\t\t\t{:>0}|{:>5}|{:>5}|{:>5}|{:>5}'.format(row[0], row[1],row[2],row[3],row[4],row[5])
                print(l)
            print("Search Again?")
            SEARCH(_conn)
    else:
        cur=_conn.cursor()
        cur.execute("Select * FROM Games where g_name LIKE ?", ["%"+y+"%"])
        
        rows = cur.fetchall()
        cNames = "{:>0}|\t\t\t\t{:>0}|\t{:>5}|\t{:>5}|\t{:>5}|\t{:>5}\n\n".format("g_name", "g_id", "g_prices","g_sold","g_date","g_genre")
        print(cNames)
        for row in rows:
            l = '{:>0}|\t\t\t\t{:>0}|\t{:>5}|\t{:>5}|\t{:>5}|\t{:>5}\n'.format(row[0], row[1],row[2],row[3],row[4],row[5])
            print(l)
        print("Search Again?")
        SEARCH(_conn)
    
def REVIEW(_conn):
    print("press 0 to exit")
    print("What game would you like to see a review of:(by name or id)")
    print("Write select to see list of reviewers")
    y=input()
    if y=="0":
        main()
    if y=="Select"or y=="select":
        cur=_conn.cursor()
        cur.execute(""" Select *
                        from reviews
                        """)
        rows = cur.fetchall()
        cNames = "{:>0}|     {:>20}|{:>5}|\n".format("r_name", "r_id","founded")
        print(cNames)
        for row in rows:
            l = '{:>0}|     {:>10}|{:>5}|'.format(row[0], row[1],row[2])
            print(l)
        REVIEW(_conn)
    if y.isdigit():
        if int(y)>0:
            
            print("Any specific type of review would you like to find")
            print("1)Just all reviews on the game, 2) Specific article 3)avg score")
            z=input()
            while z=='':
                print("1)Just all reviews on the game, 2) Specific article 3)avg score")
                z=input()

            while z.isalpha():
                print("Any specific type of review would you like to find")
                print("1)Just all reviews on the game, 2) Specific article 3)avg score")
                z=input()
            if z.isdigit():
                while 3<int(z) or 0>=int(z):
                    print("error")
                    print("Any specific type of review would you like to find")
                    print("1)Just all reviews on the game, 2) Specific article 3)Avg score")
                    z=input()
                    while z.isalpha(): 
                        print("Any specific type of review would you like to find")
                        print("1)Just all reviews on the game, 2) Specific article 3)avg score")
                        z=input()
            
            
                
                
            if int(z)==1:
                cur=_conn.cursor()
                cur.execute(""" Select gr_id,g_name,gr_score,gr_reviewername,r_name
                        from Games,Gamereviews,reviews
                        where g_id=gr_gid and r_id=gr_rid and g_id=?""",[y])
        
                rows = cur.fetchall()
                cNames = "{:>0}\t|\t{:>20}|{:>5}|{:>5}|{:>5}|\n".format("gr_id", "g_name","gr_score","gr_reviewname","r_name")
                print(cNames)
                for row in rows:
                    l = '{:>0}\t|{:>10}|{:>5}|{:>5}|{:>5}|'.format(row[0], row[1],row[2],row[3],row[4])
                    print(l)
                print("Search Again?")
                REVIEW(_conn)
            if int(z)==2:
                print("What company would you like to search for")
                print("(Press any number to go back to review menu for list)")
                a=input()
                if a.isdigit():
                    REVIEW(_conn)
                cur=_conn.cursor()
                cur.execute(""" Select gr_id,g_name,gr_score,gr_reviewername,r_name
                        from Games,Gamereviews,reviews
                        where g_id=gr_gid and r_id=gr_rid and g_id=? and r_name LIKE ?""",[y,"%"+a+"%"])
        
                rows = cur.fetchall()
                cNames = "{:>0}|     {:>20}|{:>5}|{:>5}|{:>5}|\n".format("gr_id", "g_name","gr_score","gr_reviewname","r_name")
                print(cNames)
                for row in rows:
                    l = '{:>0}|     {:>10}|{:>5}|{:>5}|{:>5}|'.format(row[0], row[1],row[2],row[3],row[4])
                    print(l)
                print("Search Again?")
                REVIEW(_conn)
            if int(z)==3:
                cur=_conn.cursor()
                cur.execute(""" Select g_id, g_name, avg(gr_score) 
                        from Games,Gamereviews,reviews
                        where g_id=gr_gid and r_id=gr_rid and g_id=?""",[y])
        
                rows = cur.fetchall()
                cNames = "{:>0}|     {:>20}|{:>5}\n".format("g_id", "g_name","avg(score)")
                print(cNames)
                for row in rows:
                    l = '{:>0}|     {:>10}|{:>5}'.format(row[0], row[1],row[2])
                    print(l)
                print("Search Again?")
                REVIEW(_conn)

    else:
        
        print("Any specific type of review would you like to find")
        print("1)Just all reviews on the game, 2) Specific article 3)avg score")
        z=input()
        while z=='':
            print("1)Just all reviews on the game, 2) Specific article 3)avg score")
            z=input()
            
            
        while z.isalpha():
                
            print("Any specific type of review would you like to find")
            print("1)Just all reviews on the game, 2) Specific article 3)avg score")
            z=input()
        if z.isdigit():
            while 3<int(z) or int(z)<=0:
                print("error")
                print("Any specific type of review would you like to find")
                print("1)Just all reviews on the game, 2) Specific article 3)Avg score")
                z=input()
                while z.isalpha(): 
                    print("Any specific type of review would you like to find")
                    print("1)Just all reviews on the game, 2) Specific article 3)avg score")
                    z=input()
                    
        if int(z)==1:
            cur=_conn.cursor()
            cur.execute(""" Select gr_id,g_name,gr_score,gr_reviewername,r_name
                    from Games,Gamereviews,reviews
                    where g_id=gr_gid and r_id=gr_rid and g_name LIKE ?""",["%"+y+"%"])
        
            rows = cur.fetchall()
            cNames = "{:>0}|     {:>20}|{:>5}|{:>5}|{:>5}|\n".format("gr_id", "g_name","gr_score","gr_reviewname","r_name")
            print(cNames)
            for row in rows:
                l = '{:>0}|     {:>10}|{:>5}|{:>5}|{:>5}|'.format(row[0], row[1],row[2],row[3],row[4])
                print(l)
            print("Search Again?")
            REVIEW(_conn)
        if int(z)==2:
            print("What company would you like to search for")
            print("(Press any number to go back to review menu for list)")
            a=input()
            if a.isdigit():
                REVIEW(_conn)
            cur=_conn.cursor()
            cur.execute(""" Select gr_id,g_name,gr_score,gr_reviewername,r_name
                    from Games,Gamereviews,reviews
                    where g_id=gr_gid and r_id=gr_rid and g_name LIKE ? and r_name LIKE ?""",["%"+y+"%","%"+a+"%"])
        
            rows = cur.fetchall()
            cNames = "{:>0}|     {:>20}|{:>5}|{:>5}|{:>5}|\n".format("gr_id", "g_name","gr_score","gr_reviewname","r_name")
            print(cNames)
            for row in rows:
                l = '{:>0}|     {:>10}|{:>5}|{:>5}|{:>5}|'.format(row[0], row[1],row[2],row[3],row[4])
                print(l)
            print("Search Again?")
            REVIEW(_conn)
        if int(z)==3:
                cur=_conn.cursor()
                cur.execute(""" Select g_id, g_name, avg(gr_score) 
                        from Games,Gamereviews,reviews
                        where g_id=gr_gid and r_id=gr_rid and g_name LIKE ?""",["%"+y+"%"])
        
                rows = cur.fetchall()
                cNames = "{:>0}|     {:>20}|{:>5}\n".format("g_id", "g_name","avg(score)")
                print(cNames)
                for row in rows:
                    l = '{:>0}|     {:>10}|{:>5}'.format(row[0], row[1],row[2])
                    print(l)
                print("Search Again?")
                REVIEW(_conn)
        
def ABOUT(_conn):
    print("What game or id would you like to know more about")
    y=input()
    if y=="0":
        main()
    if y.isdigit():
        if int(y)>0:
            print("1)Show all info?, 2)Developer info, 3) Company Ownership")
            z=input()
            while z=='':
                print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                z=input()
            while z.isalpha():
                print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                z=input()
                while z=='':
                    print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                    z=input()
            if z.isdigit():
                while 3<int(z)or int(z)<=0:
                    print("ERROR BRO FR STOP")
                    print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                    z=input()
                    while z=='':
                        print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                        z=input()
                    while z.isalpha():  
                        print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                        z=input()
                
                
                
                
            
            if int(z)==1:
                cur=_conn.cursor()
                cur.execute(""" SELECT g_name,b_name,b_ceo,b_revenue,d_name,d_head
                                FROM Games,business,dg_id,developer
                                WHERE b_key=d_bkey and dg_dkey=d_key and dg_id=g_id and g_id=? """,[y])
        
                rows = cur.fetchall()
                cNames = "{:>0} |{:>10} |{:>10} |{:>10} |{:>10} |{:>10}\n".format("g_name", "b_name","b_ceo","b_revenue","d_name","d_head")
                print(cNames)
                for row in rows:
                    l = '{:>0} |{:>10} |{:>10} |{:>10} |{:>10} |{:>10}'.format(row[0], row[1],row[2],row[3],row[4],row[5])
                    print(l)
                print("Search Again?")
                ABOUT(_conn)
            if int(z)==2:
                cur=_conn.cursor()
                cur.execute(""" SELECT g_name,d_name,d_head
                                FROM Games,business,dg_id,developer
                                WHERE b_key=d_bkey and dg_dkey=d_key and dg_id=g_id and g_id=? """,[y])
        
                rows = cur.fetchall()
                cNames = "{:>0} |{:>10} |{:>10} \n".format("g_name","d_name","d_head")
                print(cNames)
                for row in rows:
                    l = '{:>0} |{:>10} |{:>10}'.format(row[0], row[1],row[2])
                    print(l)
                print("Search Again?")
                ABOUT(_conn)
            if int(z)==3:
                cur=_conn.cursor()
                cur.execute(""" SELECT g_name,b_name,b_ceo,b_revenue
                                FROM Games,business,dg_id,developer
                                WHERE b_key=d_bkey and dg_dkey=d_key and dg_id=g_id and g_id=? """,[y])
        
                rows = cur.fetchall()
                cNames = "{:>0} |{:>10} |{:>10} |{:>10}\n".format("g_name", "b_name","b_ceo","b_revenue(billions)")
                print(cNames)
                for row in rows:
                    l = '{:>0} |{:>10} |{:>10} |{:>10} '.format(row[0], row[1],row[2],float(row[3]))
                    print(l)
                print("Search Again?")
                ABOUT(_conn)
    else:
        
        print("1)Show all info?, 2)Developer info, 3) Company Ownership")
        z=input()
        while z=='':
            print("1)Show all info?, 2)Developer info, 3) Company Ownership")
            z=input()
        while z.isalpha():
            print("1)Show all info?, 2)Developer info, 3) Company Ownership")
            z=input()
            while z=='':
                print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                z=input()
        if z.isdigit():
            while 3<int(z)or int(z)<=0:
                print("ERROR BRO FR STOP")
                print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                z=input()
                while z=='':
                    print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                    z=input()
                while z.isalpha():  
                    print("1)Show all info?, 2)Developer info, 3) Company Ownership")
                    z=input()
        
        if int(z)==1:
            cur=_conn.cursor()
            cur.execute(""" SELECT g_name,b_name,b_ceo,b_revenue,d_name,d_head
                                FROM Games,business,dg_id,developer
                                WHERE b_key=d_bkey and dg_dkey=d_key and dg_id=g_id and g_name LIKE ? """,["%"+y+"%"])
        
            rows = cur.fetchall()
            cNames = "{:>0} |{:>10} |{:>10} |{:>10} |{:>10} |{:>10}\n".format("g_name", "b_name","b_ceo","b_revenue(billions)","d_name","d_head")
            print(cNames)
            for row in rows:
                l = '{:>0} |{:>10} |{:>10} |{:>10} |{:>10} |{:>10}'.format(row[0], row[1],row[2],row[3],row[4],row[5])
                print(l)
            print("Search Again?")
            ABOUT(_conn)
        if int(z)==2:
            cur=_conn.cursor()
            cur.execute(""" SELECT g_name,d_name,d_head
                                FROM Games,business,dg_id,developer
                                WHERE b_key=d_bkey and dg_dkey=d_key and dg_id=g_id and g_name LIKE ? """,["%"+y+"%"])
        
            rows = cur.fetchall()
            cNames = "{:>0} |{:>10} |{:>10} \n".format("g_name","d_name","d_head")
            print(cNames)
            for row in rows:
                l = '{:>0} |{:>10} |{:>10}'.format(row[0], row[1],row[2])
                print(l)
            print("Search Again?")
            ABOUT(_conn)
        if int(z)==3:
            cur=_conn.cursor()
            cur.execute(""" SELECT g_name,b_name,b_ceo,b_revenue
                                FROM Games,business,dg_id,developer
                                WHERE b_key=d_bkey and dg_dkey=d_key and dg_id=g_id and g_name LIKE ? """,["%"+y+"%"])
        
            rows = cur.fetchall()
            cNames = "{:>0} |{:>10} |{:>10} |{:>10} \n".format("g_name", "b_name","b_ceo","b_revenue(billion)")
            print(cNames)
            for row in rows:
                l = '{:>0} |{:>10} |{:>10} |{:>10} '.format(row[0], row[1],row[2],row[3])
                print(l)
            print("Search Again?")
            ABOUT(_conn)
        
def STORES(_conn):
    print("What game id or name is on sale")
    y=input()
    if y=="0":
        main()
    if y.isdigit():
        cur=_conn.cursor()
        cur.execute("""SELECT s_name,s_discount,g_name
                    FROM Games,stores
                    WHERE g_id=s_gid and g_id=? """,[y])
        
        rows = cur.fetchall()
        cNames = "{:>0} |{:>10} |{:>10} \n".format("s_name", "g_discount","g_name")
        print(cNames)
        for row in rows:
            l = '{:>0} |{:>10} |{:>10} '.format(row[0], row[1],row[2])
            print(l)
        print("Search Again?")
        STORES(_conn)
    else:
        cur=_conn.cursor()
        cur.execute("""SELECT s_name,s_discount,g_name
                    FROM Games,stores
                    WHERE g_id=s_gid and g_name LIKE ? """,["%"+y+"%"])
        
        rows = cur.fetchall()
        cNames = "{:>0} |{:>10} |{:>10} \n".format("s_name", "g_discount","g_name")
        print(cNames)
        for row in rows:
            l = '{:>0} |{:>10} |{:>10} '.format(row[0], row[1],row[2])
            print(l)
        print("Search Again?")
        STORES(_conn)

def CONSOLES(_conn):
    print("What game or id is available on which system.")
    print("Write select if you want games only for that system")
    y=input()
    if y=="0":
        main()
    
    if y.isdigit():
        if int(y)>0:
            cur=_conn.cursor()
            cur.execute("""SELECT c_name,g_name
                        from Games,Consolegame,console
                        where cg_gid=g_id and cg_cid=c_id and g_id=? """,[y])
           
        
            rows = cur.fetchall()
            for row in rows:
                pass
            f = '{:>0} '.format(row[1])
            print(f)
            print("------------------")
            cNames = "{:>0}\n".format("c_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
            
            
            print("Search Again?")
            CONSOLES(_conn)

    if y=="select" or y=="SELECT" or y=="Select":
        print("press a number to choose what system")
        print("1)Nintendo Switch")
        print("2)Windows/pc")
        print("3)PS4")
        print("4)PS5")
        print("5)XBOX ONE")
        print("6)XBOX ONE S")
        print("7)XBOX SERIES X")
        print("8)XBOX SERIES S")
        print("9)MAC")
        print("10)STEAM DECK")
        print("11)GOOGLE STADIA")
        c=input()
        while c=='':
            print("press a number to choose what system")
            print("1)Nintendo Switch")
            print("2)Windows/pc")
            print("3)PS4")
            print("4)PS5")
            print("5)XBOX ONE")
            print("6)XBOX ONE S")
            print("7)XBOX SERIES X")
            print("8)XBOX SERIES S")
            print("9)MAC")
            print("10)STEAM DECK")
            print("11)GOOGLE STADIA")
            c=input()
        while c.isalpha():
            print("press a number to choose what system")
            print("1)Nintendo Switch")
            print("2)Windows/pc")
            print("3)PS4")
            print("4)PS5")
            print("5)XBOX ONE")
            print("6)XBOX ONE S")
            print("7)XBOX SERIES X")
            print("8)XBOX SERIES S")
            print("9)MAC")
            print("10)STEAM DECK")
            print("11)GOOGLE STADIA")
            c=input()
            
            c=input()
            while c=='':
                print("press a number to choose what system")
                print("1)Nintendo Switch")
                print("2)Windows/pc")
                print("3)PS4")
                print("4)PS5")
                print("5)XBOX ONE")
                print("6)XBOX ONE S")
                print("7)XBOX SERIES X")
                print("8)XBOX SERIES S")
                print("9)MAC")
                print("10)STEAM DECK")
                print("11)GOOGLE STADIA")
                c=input()
        if c.isdigit():
            while 11<int(c) or int(c)<=0:
                print("ERROR STOP PLAYING MAN DO IT AGAIN")
                print("press a number to choose what system")
                print("1)Nintendo Switch")
                print("2)Windows/pc")
                print("3)PS4")
                print("4)PS5")
                print("5)XBOX ONE")
                print("6)XBOX ONE S")
                print("7)XBOX SERIES X")
                print("8)XBOX SERIES S")
                print("9)MAC")
                print("10)STEAM DECK")
                print("11)GOOGLE STADIA")
                c=input()
                while c.isalpha():
                    print("press a number to choose what system")
                print("1)Nintendo Switch")
                print("2)Windows/pc")
                print("3)PS4")
                print("4)PS5")
                print("5)XBOX ONE")
                print("6)XBOX ONE S")
                print("7)XBOX SERIES X")
                print("8)XBOX SERIES S")
                print("9)MAC")
                print("10)STEAM DECK")
                print("11)GOOGLE STADIA")
                c=input()
                while c=='':
                    print("press a number to choose what system")
                    print("1)Nintendo Switch")
                    print("2)Windows/pc")
                    print("3)PS4")
                    print("4)PS5")
                    print("5)XBOX ONE")
                    print("6)XBOX ONE S")
                    print("7)XBOX SERIES X")
                    print("8)XBOX SERIES S")
                    print("9)MAC")
                    print("10)STEAM DECK")
                    print("11)GOOGLE STADIA")
                    c=input()
        
        
        
        
        if int(c)==1:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                    from Viewconsole
                    where c_name= 'Nintendo Switch' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'Nintendo Switch'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                    l = '{:>0} '.format(row[0])
                    print(l)
                    print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==2:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where  c_name= 'Windows' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'Windows'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==3:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where  c_name= 'PS4' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'PS4'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
          
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==4:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where  c_name= 'PS5' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'PS5'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==5:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where  c_name= 'XBOX ONE' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'XBOX ONE'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==6:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where c_name= 'XBOX ONE S' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'XBOX ONE S'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==7:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where  c_name= 'XBOX Series X' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'XBOX Series X'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==8:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where c_name= 'XBOX Series S' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'XBOX Series S'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
           
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==9:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where  c_name= 'Mac' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'Mac'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
         
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==10:
            cur=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where c_name= 'Steam Deck' """)
            curr=_conn.cursor()
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'Steam Deck'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+":Total units sold(million):",business[2])
                print(l)
                print("--------")
            rows = cur.fetchall()
            
            print("------------------")
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        if int(c)==11:
            cur=_conn.cursor()
            curr=_conn.cursor()
            cur.execute("""SELECT g_name
                        from Viewconsole
                        where c_name= 'Google Stadia' """)
            curr.execute(""" SELECT c_name ,b_name,c_units
                            From Console,business
                            WHERE b_key=c_bid and c_name = 'Google Stadia'
                                    """)
            businesses=curr.fetchall()
            for business in businesses:
                l = '{:>0} {:>0} {:>0}'.format(business[0]+":",business[1]+": Total units system sold(million):",business[2])
                print(l)
                print("--------")
           
        
            rows = cur.fetchall()
            
            cNames = "{:>0}\n".format("g_name")
            print(cNames)
            
            for row in rows:
                l = '{:>0} '.format(row[0])
                print(l)
                print("--------")
            
            
            print("Search Again?")
            CONSOLES(_conn)
        
    else:    
        cur=_conn.cursor()
        cur.execute("""SELECT distinct(g_name),c_name
                        from Games,Consolegame,console
                        where cg_gid=g_id and cg_cid=c_id and g_name LIKE ? """,["%"+y+"%"])
           
        
        rows = cur.fetchall()
        for row in rows:
            pass
        f = '{:>0} '.format(row[1])
        print(f)
        print("------------------")
        cNames = "{:>0}\n".format("c_name")
        print(cNames)
            
        for row in rows:
            l = '{:>0} '.format(row[0])
            print(l)
            
            
        print("Search Again?")
        CONSOLES(_conn)
             
        
    
    
    
    
    
def main():
    database = r"Gamenew.db"
    print("Press 0 to exit")
    print("1)INSERT New game ")
    print("2)UPDATE Games")
    print("3)DELETE")
    print("4)SEARCH for a Game")
    print("5)REVIEWS")
    print("6)About Game")
    print("7)Best offers today")
    print("8)What system to play Games 2022")
    print("9)Specific Search by")
    x=input()
    if x=='':
        print("empty")
        main()
    
    if x.isalpha():
                print("no bad")
                main()

    while int(x)>0 and int(x)>9:
        if int(x)>0 and int(x)>9:
            print("ERROR.TRY AGAIN >:(")
            print("Press 0 to exit")
            print("1)INSERT New Game")
            print("2)UPDATE a Game")
            print("3)DELETE from tables")
            print("4)SEARCH for a Game")
            print("5)REVIEWS")
            print("6)About Game")
            print("7)Best offers today")
            print("8)What system to play Games 2022")
            print("9)Specific Search by")
            x=input()
            if x.isalpha():
                print("no bad")
                main()
    
    # create a database connection
    conn = openConnection(database)
    if x.isdigit():
        with conn:
            if int(x)==0:
                exit()
            if int(x)==1:
                INSERT(conn)
            if int(x)==2:
                UPDATE(conn)
            if int(x)==3:
                DELETE(conn)
            
            if int(x)==4:
                SEARCH(conn)
            if int(x)==5:
                REVIEW(conn)
            if int(x)==6:
                ABOUT(conn)
            if int(x)==7:
                STORES(conn)
            if int(x)==8:
                CONSOLES(conn)
            if int(x)==9:
                Specific(conn)
        
        

    closeConnection(conn, database)
    main()
    

if __name__ == '__main__':
    main()