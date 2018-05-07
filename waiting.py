#create table train_status(train_id int, available_date varchar(20), booked_seats int,
#available_seats int, primary key(train_id,available_date),foreign key(train_id) references train(train_id) 
 #on update cascade on delete cascade);
import psycopg2
import menu
def user_booking():
   
   email = raw_input("Enter your email id:")
   source = raw_input("Enter the source_id:")
   destination = raw_input("Enter the destination_id:")
   train = raw_input("Train_id")
   no_of_seats = int(raw_input("Enter the required number of seats:"))
   conn = None
   try:
        conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
        cur = conn.cursor()
        print('Database Connection Open')
	print("Station codes:")
	cur.execute("""select * from station""")
	row = cur.fetchone()
	while row is not None:
		print(row)
		row = cur.fetchone()
	print("Train codes:")
	cur.execute("""select train_id,train_name from train""")
	row = cur.fetchone()
	while row is not None:
		print(row)
		row = cur.fetchone()
	cur.execute("""SELECT available_seat FROM train_status""")
        #print("The number of parts: ", cur.rowcount)
	##print("hello")
        avail = cur.fetchone()
	##print("hii")

	##print(type(avail))
	if(avail[0]==0):
		p = str(no_of_seats)
		cur.execute("""insert into waiting_list values(%s,%s,%s,%s, %s)""",
                                            (email,source,destination,train,no_of_seats))
		print('you are added to the waiting list')
		print('The number of users already in waiting list are')
		cur.execute("""select * from waiting_list """)
		row = cur.fetchone()
		while row is not None:
			print(row)
			row = cur.fetchone()
	else :
        	avail = avail[0] - no_of_seats
  		cur.execute("""SELECT booked_seats FROM train_status""")
        	#print("The number of parts: ", cur.rowcount)
        	booked = cur.fetchone()
        	booked = booked[0] + no_of_seats
		p = str(no_of_seats)
        	cur.execute("""insert into user_bookings values(%s,%s,%s,%s, %s)""",
                                            (email,source,destination,train,no_of_seats))
	
		cur.execute("""UPDATE train_status SET available_seat = %s, booked_seats = %s """,(str(avail),str		(booked)))									
        	conn.commit()

        #cur.execute("""insert into Media(ArticleID,MediaLink) values(%s,%s)""",(articleid,media_link))
        #cur.close()
        #conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
        print(error)
   
   menu.menu()   
   return
 
