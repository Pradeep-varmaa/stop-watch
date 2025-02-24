import time
from playsound import playsound

def clock(minutes):
    mins = minutes
    sec = 60
    true = True
    while true:
        if mins>=0:
            sec-=1
            if sec == 0:
                mins-=1
                sec= 60
        time.sleep(1)
        print(f"Mins: {mins:02} Sec: {sec:02}")


        if mins==0 and sec ==1:
            print("Wake up!")
            true= False

    playsound("Edit the File Path")




clock(0)
