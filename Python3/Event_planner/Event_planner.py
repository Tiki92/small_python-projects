"""A Calendar that the user can interact with from command line, 
Calendar functionality: View the Calendar, Add an event to the Calendar, Update and existing event, Delete an existing event"""
from time import sleep, strftime

USER_FIRST_NAME = input("Enter your name: ")
calendar = {}
def welcome():
  print("Welcome %s." % (USER_FIRST_NAME))
  print("The Calendar is Starting!")
  sleep(1)
  print("Today is: " + strftime("%A %B %d, %Y"))
  print("Current time: " + strftime("%X"))
  sleep(1)
  print("What would you like to do?")
  
def start_calendar():
  welcome()
  start = True
  
  while start == True:
    user_choice = input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print ("Calendar empty.")
      else:
        print (calendar)
    elif user_choice == "U":
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print("The Calendar had been Succesfuly Updated!")
      print (calendar)
    elif user_choice == "A":
      event = input("Enter event: ")
      date = raw_input("Enter date(MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))) or int(date[:2]) > 12 or int(date[3:5]) > 31:
        print("An invalid date was entered!")
        try_again = input("Try Again? Y for Yes, N for No: ")
        try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print("The calendar was updated Succesfuly")
        print(calendar)
    elif user_choice == "D":
      if len(calendar.keys()) < 1:
        print("The calendar is empty!")
      else:
        event = input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print("The event had been Succesfuly Deleted!")
            print(calendar)
          else:
            print("An incorrect event was specified!")
    elif user_choice == "X":
      start = False
    else:
      print("An invalid command was entered!")
            
start_calendar()  
        
        

