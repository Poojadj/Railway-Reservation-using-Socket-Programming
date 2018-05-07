#create table train_status(train_id int, available_date varchar(20), booked_seats int,
#available_seats int, primary key(train_id,available_date),foreign key(train_id) references train(train_id) 
 #on update cascade on delete cascade);
import psycopg2
def cancel():
   
   email = raw_input("Enter your email id:")
   password = raw_input("Enter your password:")
   #source = raw_input("Enter the source_id:")
   #destination = raw_input("Enter the destination_id:")
   #train = raw_input("Train_id")
   #no_of_seats = int(raw_input("Enter the required number of seats:"))
   conn = None
   try:
        conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
        cur = conn.cursor()
        print('Database Connection Open')
	cur.execute("""SELECT email_id,train_id,no_of_seats from user_bookings b,user_details u where u.email_id = %s and u.password = %s and b.email_id = %s""",(email,password,email))
    seats = int(raw_input("Enter the nuber of seats you want to delete"))  
	cur.execute("""SELECT train_id from user_bookings b,user_details u where u.email_id = %s and u.password = %s and b.email_id = %s""",(email,password,email))
	train_id = cur.fetchone()
	cur.execute("""SELECT available_seat FROM train_status where train_id = %s""",(train_id))
    avail = cur.fetchone()
	avail = avail[0] + seats
	cur.execute("""SELECT booked_seats FROM train_status""")
	booked = cur.fetchone()
    booked = booked[0] - seats
	cur.execute("""UPDATE train_status SET available_seat = %s, booked_seats = %s where train_id = %s""",(str(avail),str(booked),train_id))	
    cur.execute("""SELECT no_of_seats from user_bookings b,user_details u where u.email_id = %s and u.password = %s and b.email_id = %s""",(email,password,email))
 	booked_seats = cur.fetchone()
	booked_seats = int(booked_seats)
	seat = seats - booked_seats
	if(seat == 0):
		cur.execute("""DELETE * from user_bookings b,user_details u where u.email_id = %s and u.password = %s and b.email_id = %s""",(email,password,email))
    else:
		seat = str(seat)
        cur.execute(""" update user_bookings set no_of_seats = %s where user_details.email_id = %s and user_details.password = %s and user_bookings.email_id = %s""",(seat,email,password,email))    
		conn.commit()

    
   except (Exception, psycopg2.DatabaseError) as error:
        print(error)
   return
 
