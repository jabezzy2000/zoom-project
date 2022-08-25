from ntpath import join
import pyautogui as pyg
import webbrowser
import time
import click
import utils
import datetime
zoom_meetings_for_today = []
status = True
count =1
print("Enter number of classes you have today: ")
num_of_classes = int(input())
for i in range(num_of_classes):
    print("Please enter the details of zoom meetings in order of occurence")
    zoom_details = []
    print ("Enter zoom link for class " + str(count) )
    zoom_link = str(input())
    print("Enter date for class " + str(count) + "in format DD-MM-YYYY")
    zoom_date = str(input())
    print("Enter the time for class " + str(count) + "in format HH-MM-SS")
    zoom_time = str(input())
    zoom_details.append(zoom_link)
    zoom_details.append(zoom_date)
    zoom_details.append(zoom_time)
    if count == 1:
        zoom_details.append("1st")
    elif count == 2:
        zoom_details.append("2nd")
    elif count == 3:
        zoom_details.append("3rd")
    else:
        zoom_details.append(str(count) + "th")
    zoom_meetings_for_today.append(zoom_details)
    count +=1

def join_zoom_meeting(zoom_link,meeting_date,meeting_time):
    formatted_meeting_date = utils.format_date(meeting_date)
    formatted_meeting_time = utils.format_time(meeting_time)
    formatted_required_datetime = utils.given_datetime(formatted_meeting_date, formatted_meeting_time)

    #finding the time between the time at present vs the time of the meeting
    current_time = datetime.datetime.now().replace(microsecond=0)
    # print("Current time is " + str(current_time))
    # print("Meeting time is " + str(formatted_required_datetime))
    wait_time_sec = (formatted_required_datetime - datetime.datetime.now().replace(microsecond=0)).total_seconds()
    print(f"Your ZOOM meeting starts in " + str(wait_time_sec/60) + " min")
    time.sleep(wait_time_sec)

    webbrowser.get(using='Chrome').open(zoom_link, new=2) #this opens zoom link in a new chrome window
    
#join_zoom_meeting("https://us05web.zoom.us/j/6721595024?pwd=c1B5VWV5RXI4YXFWNkRYdGNCWkV2QT09","24-08-2022","23-10-00")
for zoom_meetings in zoom_meetings_for_today:
    link = zoom_meetings[0]
    zoom_date = zoom_meetings[1]
    zoom_time = zoom_meetings[2]
    join_zoom_meeting(link,zoom_date,zoom_time)