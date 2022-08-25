from ntpath import join
import pyautogui as pyg
import webbrowser
import time
import click
import utils
import datetime
def join_zoom_meeting(zoom_link,meeting_date,meeting_time):
    #"date of the meeting in the format DD-MM-YYYY"
    #"time of the meeting in the format HH-MM-SS"
    #time of meeting is in the 24 hour format
    #you have to allow access to chrome
    #change zoom settings to automatically mute mic and turn video off
    #change zoom settings to automatically join with computer audio
    #allow chrome to always open zoom 
    formatted_meeting_date = utils.format_date(meeting_date)
    formatted_meeting_time = utils.format_time(meeting_time)
    formatted_required_datetime = utils.given_datetime(formatted_meeting_date, formatted_meeting_time)

    # pyg.displayMousePosition()

    #finding the time between the time at present vs the time of the meeting
    current_time = datetime.datetime.now().replace(microsecond=0)
    print("Current time is " + str(current_time))
    print("Meeting time is " + str(formatted_required_datetime))
    wait_time_sec = (formatted_required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print("Your ZOOM meeting starts in " + str(wait_time_sec/60) + " min")
    time.sleep(wait_time_sec)

    

    webbrowser.get(using='Chrome').open(zoom_link, new=2) #this opens zoom link in a new chrome window
    
join_zoom_meeting("https://us05web.zoom.us/j/6721595024?pwd=c1B5VWV5RXI4YXFWNkRYdGNCWkV2QT09","24-08-2022","22-10-00")