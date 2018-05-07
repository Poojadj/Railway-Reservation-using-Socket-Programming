#create table user_details(email_id varchar(30) primary key, password varchar(15) not null, name varchar(30) 
#not null, gender char(1) not null, age int not null, mobile varchar(14) not null, city varchar(20) not null,
#state varchar(25) not null,CHECK(gender='M' or gender='F'));
import psycopg2
import menu
#import user_booking
def user_details():
   email = raw_input("Enter your email id:")
   password = raw_input("Enter your password:")
   name = raw_input("Enter your name:")
   gender = raw_input("Enter your gender(M/F):")
   #age = raw_input("Enter your age:")
   mobile = raw_input("Enter your mobile no. :")
   city = raw_input("Enter your city:")
   state = raw_input("Enter your state:")
   conn = None
   try:
        conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
        cur = conn.cursor()
        print('Database Connection Open')
        cur.execute("""insert into user_details values(%s,%s,%s,%s,%s,%s,%s)""",
                                            (email,password,name,gender,mobile,city,state))
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
        conn.commit()

        #cur.execute("""insert into Media(ArticleID,MediaLink) values(%s,%s)""",(articleid,media_link))
        #cur.close()
        #conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
        print(error)
   
   #user_booking.user_booking()
   menu.menu()
   return
   
