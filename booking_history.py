import psycopg2
import menu
import user_booking
def booking_history():
   email = raw_input("Enter your email id:")
   password = raw_input("Enter your password:")
   
   conn = None
   try:
        conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
        cur = conn.cursor()
        print('Database Connection Open')
        
	print("Booking History:")
	cur.execute("""Select b.email_id,train_id,no_of_seats from user_bookings b,user_details u where u.email_id = %s and u.password = %s and b.email_id = %s""",(email,password,email))
	row = cur.fetchone()
	while row is not None:
		print(row)
		row = cur.fetchone()
	
        conn.commit()

        
   except (Exception, psycopg2.DatabaseError) as error:
        print(error)
   
   menu.menu()
   return
   
