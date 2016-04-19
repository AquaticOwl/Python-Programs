import time
import winsound

work_time_minutes = 0 #Starting time worked is 0 minutes

def count_up():
    global work_time_minutes #This func can use work_time_minutes
    while True: #Continuously runs this code
        try:
            time.sleep(60) #Waits a minute before executing the next 2 lines
            work_time_minutes += 1 #1 minute has been added to the amount of time spent working
            print(work_time_minutes) #Gives the user a tally of the time spent working
        except KeyboardInterrupt: #If the program is stopped using Ctrl + C, it runs these lines
            print('You worked for ' + str(work_time_minutes) + ' minutes!') #Prints total
            return #Stops counting
    
def count_down(): #Very similar to count_up
    global work_time_minutes
    while True:
        try:
            time.sleep(60) 
            work_time_minutes -= 1
            print(work_time_minutes)
        except KeyboardInterrupt:
            print('You need to work for ' + str(-work_time_minutes) + ' minutes!' + ' Good luck!')
            return


