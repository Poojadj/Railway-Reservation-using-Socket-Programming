import psycopg2
import menu
#import user_booking
def booking_history():
   email = raw_input("Enter your email id:")
   password = raw_input("Enter your password:")
   
   conn = None
   try:
        conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
        cur = conn.cursor()
        print('Database Connection Open')
        
	print("Booking History:")
	cur.execute("""select * from station where email = %s and password = %s""",(email,password))
	row = cur.fetchone()
	while row is not None:
		print(row)
		row = cur.fetchone()
	
        conn.commit()

        #cur.execute("""insert into Media(ArticleID,MediaLink) values(%s,%s)""",(articleid,media_link))
        #cur.close()
        #conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
        print(error)
   
   menu.menu()
   return
   
