import psycopg2
import menu
def train_stat():
	trainID=raw_input("Enter train_id")
	#trainID=19020
	conn = None
	try:
        	conn = psycopg2.connect(host="localhost",database="try1",user="pooja",password="pwd")
        	cur = conn.cursor()
        	print('Database Connection Open')

		cur.execute("""SELECT s.train_id , s.available_date, 
 s.available_seat from train_status s where train_id=('19020')""")
		#row = cur.fetchone()
		row = cur.fetchone()
		while row is not None:
			print(row)
			row = cur.fetchone()
	
        	conn.commit()

        
   	except (Exception, psycopg2.DatabaseError) as error:
        	print(error)
   
   	menu.menu()
   	return
