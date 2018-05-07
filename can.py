
import psycopg2
import menu
   
   
   
def cancel(socket,seatid):
    global price;
    socket.send(seatid + "\n")
    print "\n"
    print "**** Enter User ID ****"
    socket.send(raw_input() + "\n")
    print "**** Enter Password ****"
    socket.send(getpass.getpass() + "\n")
    #print "Your money" + price + "has been refunded"
    conn = None
    try:
            conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
            cur = conn.cursor()
               #print('Database Connection Open')
        #cur.execute("""select price from passenger where price=%s""",(price))
            print("Your money has been refunded",price)
            cur.execute("""delete from passenger where seatid = %s""", (seatid,))
            print("deleted")
       
             
            cur.close()
            conn.commit()
    
    except (Exception, psycopg2.DatabaseError) as error:
            print(error)
    menu.menu()
    return
    

