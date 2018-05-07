import psycopg2
import user_booking
import user
import booking_history
import cancellation
import booking_history
import train_status
import waiting

def menu():
	print("Menu:\n")
	print("1. Make a Booking\n")
	print("2. Cancel a Booking\n")
	print("3. Booking History\n")
	print("4. Check PNR status\n")
	print("5. Sign - up\n")
	print("6. Display the train status based on train_id\n")
	print("7. Exit\n")
	print("\n")
	opt = int(raw_input("Enter your option:"))
  
	if(opt == 1):
		user_booking.user_booking()
	elif(opt == 2):
		cancellation.cancel()
	elif(opt == 3):
		booking_history.booking_history()
	elif(opt == 4):
		waiting.user_booking()
	elif(opt == 5):
		user.user_details()
	elif(opt == 6):
   		train_status.train_stat()
	
	
	else:
		exit(0)
	return
   
