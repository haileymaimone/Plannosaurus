from sdates import StartingDates
import config
from kivymd.uix.list import OneLineAvatarIconListItem
from kivy.uix.image import AsyncImage, Image
import psycopg2
import psycopg2.extras
import datetime
from datetime import *
from kivy.uix.screenmanager import ScreenManager
from kivy.storage.jsonstore import JsonStore

img_1 = config.img_1
img_2 = config.img_2
citrusIMG1 = config.citrusIMG1
citrusIMG2 = config.citrusIMG2
origIMG1 = config.origIMG1
origIMG2 = config.origIMG2
pinkIMG1 = config.pinkIMG1
pinkIMG2 = config.pinkIMG2


class WindowManager(ScreenManager):
    def init_load(self, root):
        curr_day = datetime.today()

        if curr_day.weekday() == 6:
            first_day = curr_day
            second_day = (curr_day + timedelta(days = 1))
            third_day = (curr_day + timedelta(days = 2))
            fourth_day = (curr_day + timedelta(days = 3))
            fifth_day = (curr_day + timedelta(days = 4))
            sixth_day = (curr_day + timedelta(days = 5))
            seventh_day = (curr_day + timedelta(days = 6))

        elif curr_day.weekday() == 0:
            second_day = curr_day
            first_day = (curr_day - timedelta(days = 1))
            third_day = (curr_day + timedelta(days = 1))
            fourth_day = (curr_day + timedelta(days = 2))
            fifth_day = (curr_day + timedelta(days = 3))
            sixth_day = (curr_day + timedelta(days = 4))
            seventh_day = (curr_day + timedelta(days = 5))

        elif curr_day.weekday() == 1:
            third_day = curr_day
            second_day = (curr_day - timedelta(days = 1))
            first_day = (curr_day - timedelta(days = 2))
            fourth_day = (curr_day + timedelta(days = 1))
            fifth_day = (curr_day + timedelta(days = 2))
            sixth_day = (curr_day + timedelta(days = 3))
            seventh_day = (curr_day + timedelta(days = 4))

        elif curr_day.weekday() == 2:
            fourth_day = curr_day
            third_day = (curr_day - timedelta(days = 1))
            second_day = (curr_day - timedelta(days = 2))
            first_day = (curr_day - timedelta(days = 3))
            fifth_day = (curr_day + timedelta(days = 1))
            sixth_day = (curr_day + timedelta(days = 2))
            seventh_day = (curr_day + timedelta(days = 3))

        elif curr_day.weekday() == 3:
            fifth_day = curr_day
            fourth_day = (curr_day - timedelta(days = 1))
            third_day = (curr_day - timedelta(days = 2))
            second_day = (curr_day - timedelta(days = 3))
            first_day = (curr_day - timedelta(days = 4))
            sixth_day = (curr_day + timedelta(days = 1))
            seventh_day = (curr_day + timedelta(days = 2))

        elif curr_day.weekday() == 4:
            sixth_day = curr_day
            fifth_day = (curr_day - timedelta(days = 1))
            fourth_day = (curr_day - timedelta(days = 2))
            third_day = (curr_day - timedelta(days = 3))
            second_day = (curr_day - timedelta(days = 4))
            first_day = (curr_day - timedelta(days = 5))
            seventh_day = (curr_day + timedelta(days = 1))

        else:
            seventh_day = curr_day
            sixth_day = (curr_day - timedelta(days = 1))
            fifth_day = (curr_day - timedelta(days = 2))
            fourth_day = (curr_day - timedelta(days = 3))
            third_day = (curr_day - timedelta(days = 4))
            second_day = (curr_day - timedelta(days = 5))
            first_day = (curr_day - timedelta(days = 6))

        theDays = StartingDates(first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day)
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        #self.ids.currMonth.text = str(months[date.today().month - 1])

        # highlight the current day

        if first_day == datetime.today():
            self.ids.day1.text = "[color=#42f58d]"+ theDays.day1.strftime("%d") +"[/color]"
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif second_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = "[color=#42f58d]"+ theDays.day2.strftime("%d") +"[/color]"
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif third_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = "[color=#42f58d]"+ theDays.day3.strftime("%d") +"[/color]"
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif fourth_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = "[color=#42f58d]"+ theDays.day4.strftime("%d") +"[/color]"
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif fifth_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = "[color=#42f58d]"+ theDays.day5.strftime("%d") +"[/color]"
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = theDays.day7.strftime("%d")

        elif sixth_day == datetime.today():
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = "[color=#42f58d]"+ theDays.day6.strftime("%d") +"[/color]"
            self.ids.day7.text = theDays.day7.strftime("%d")

        else:
            self.ids.day1.text = theDays.day1.strftime("%d")
            self.ids.day2.text = theDays.day2.strftime("%d")
            self.ids.day3.text = theDays.day3.strftime("%d")
            self.ids.day4.text = theDays.day4.strftime("%d")
            self.ids.day5.text = theDays.day5.strftime("%d")
            self.ids.day6.text = theDays.day6.strftime("%d")
            self.ids.day7.text = "[color=#42f58d]"+ theDays.day7.strftime("%d") +"[/color]"

        return "main_sc"



    def event_add(self, root, time):
        timesArr = ["6 AM", "7 AM", "8 AM", "9 AM", "10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM", "4 PM", "5 PM", "6 PM", "7 PM", "8 PM", "9 PM"]
        militaryArr = ["06:00", "07:00", "08:00", "09:00", "10:00", "11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00", "19:00", "20:00", "21:00"]
        index = timesArr.index(time)
        timeObj = datetime.strptime(militaryArr[index], '%H:%M').strftime("%H:%M")

        if index == 0:
            messageText = self.ids.contentEvent.text
            self.ids.contentEvent.disabled = True
            self.ids.add6AM.disabled = True
        elif index == 1:
            messageText = self.ids.sevenAM.text
            self.ids.sevenAM.disabled = True
            self.ids.add7AM.disabled = True
        elif index == 2:
            messageText = self.ids.eightAM.text
            self.ids.eightAM.disabled = True
            self.ids.add8AM.disabled = True
        elif index == 3:
            messageText = self.ids.nineAM.text
            self.ids.nineAM.disabled = True
            self.ids.add9AM.disabled = True
        elif index == 4:
            messageText = self.ids.tenAM.text
            self.ids.tenAM.disabled = True
            self.ids.add10AM.disabled = True
        elif index == 5:
            messageText = self.ids.elevenAM.text
            self.ids.elevenAM.disabled = True
            self.ids.add11AM.disabled = True
        elif index == 6:
            messageText = self.ids.noon.text
            self.ids.noon.disabled = True
            self.ids.add12PM.disabled = True
        elif index == 7:
            messageText = self.ids.onePM.text
            self.ids.onePM.disabled = True
            self.ids.add1PM.disabled = True
        elif index == 8:
            messageText = self.ids.twoPM.text
            self.ids.twoPM.disabled = True
            self.ids.add2PM.disabled = True
        elif index == 9:
            messageText = self.ids.threePM.text
            self.ids.threePM.disabled = True
            self.ids.add3PM.disabled = True
        elif index == 10:
            messageText = self.ids.fourPM.text
            self.ids.fourPM.disabled = True
            self.ids.add4PM.disabled = True
        elif index == 11:
            messageText = self.ids.fivePM.text
            self.ids.fivePM.disabled = True
            self.ids.add5PM.disabled = True
        elif index == 12:
            messageText = self.ids.sixPM.text
            self.ids.sixPM.disabled = True
            self.ids.add6PM.disabled = True
        elif index == 13:
            messageText = self.ids.sevenPM.text
            self.ids.sevenPM.disabled = True
            self.ids.add7PM.disabled = True
        elif index == 14:
            messageText = self.ids.eightPM.text
            self.ids.eightPM.disabled = True
            self.ids.add8PM.disabled = True
        elif index == 15:
            messageText = self.ids.ninePM.text
            self.ids.ninePM.disabled = True
            self.ids.add9PM.disabled = True
        

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()

        if config.store.exists('account'):
            config.userid = config.store.get('account')['userid']
        
        c.execute("INSERT INTO events(dateID, timestamp, time, messageBody, userID, sticker, color) VALUES (%s, %s, %s, %s, %s, %s, %s)", (config.dateID, timeObj, time, time + " - " + messageText, config.userid, 'circle-outline', 'default'))
        conn.commit()
        conn.close()


    def overview_images(self, root, image1, image2):
        global img_1
        global img_2
        global citrusIMG1
        global citrusIMG2
        global origIMG1
        global origIMG2
        global pinkIMG1
        global pinkIMG2

        self.ids.float.remove_widget(img_1)
        self.ids.float.remove_widget(img_2)
        self.ids.float.remove_widget(citrusIMG1)
        self.ids.float.remove_widget(citrusIMG2)
        self.ids.float.remove_widget(origIMG1)
        self.ids.float.remove_widget(origIMG2)
        self.ids.float.remove_widget(pinkIMG1)
        self.ids.float.remove_widget(pinkIMG2)
        
        self.ids.float.add_widget(image1)
        self.ids.float.add_widget(image2)
        

    def colorChanger(self, root, style):
        global img_1
        global img_2
        global citrusIMG1
        global citrusIMG2
        global origIMG1
        global origIMG2
        global pinkIMG1
        global pinkIMG2

        if style == "OG":
            self.ids.contentEventMain.fill_color = [.5,1,.5,0.6]
            self.ids.contentEventMain._set_fill_color([.5,1,.5,0.6])
        
            self.ids.contentTODOMain.fill_color = [.5,.5,.8,0.6]
            self.ids.contentTODOMain._set_fill_color([.5,.5,.8,0.6])
        
            self.ids.addToDo.md_bg_color = [0, 1, 0, .5]
            self.ids.addTask.md_bg_color = [0, 1, 0, .5]
            
            #Change colors of add event screen (left side)
            self.ids.contentEvent.fill_color = (0,.5,.2,.5)
            self.ids.contentEvent._set_fill_color([0,.5,.2,.5])
            self.ids.sevenAM.fill_color = (0,.5,.35,.5)
            self.ids.sevenAM._set_fill_color([0,.5,.35,.5])
            self.ids.eightAM.fill_color = [0,.5,.4,.5]
            self.ids.eightAM._set_fill_color([0,.5,.4,.5]) 
            self.ids.nineAM.fill_color = [0,.5,.45,.5]
            self.ids.nineAM._set_fill_color([0,.5,.45,.5]) 
            self.ids.tenAM.fill_color = [0,.5,.5,.5]
            self.ids.tenAM._set_fill_color([0,.5,.5,.5]) 
            self.ids.elevenAM.fill_color = [0,.5,.55,.5]
            self.ids.elevenAM._set_fill_color([0,.5,.55,.5]) 
            self.ids.noon.fill_color = [0,.5,.6,.5]
            self.ids.noon._set_fill_color([0,.5,.6,.5]) 
            self.ids.onePM.fill_color = [0,.5,.65,.5]
            self.ids.onePM._set_fill_color([0,.5,.65,.5]) 
            #Change colors of add event screen (right side)
            self.ids.twoPM.fill_color = (0,.5,.2,.5)
            self.ids.twoPM._set_fill_color([0,.5,.2,.5]) 
            self.ids.threePM.fill_color = (0,.5,.35,.5)
            self.ids.threePM._set_fill_color([0,.5,.35,.5]) 
            self.ids.fourPM.fill_color = [0,.5,.4,.5]
            self.ids.fourPM._set_fill_color([0,.5,.4,.5]) 
            self.ids.fivePM.fill_color = [0,.5,.45,.5]
            self.ids.fivePM._set_fill_color([0,.5,.45,.5]) 
            self.ids.sixPM.fill_color = [0,.5,.5,.5]
            self.ids.sixPM._set_fill_color([0,.5,.5,.5]) 
            self.ids.sevenPM.fill_color = [0,.5,.55,.5]
            self.ids.sevenPM._set_fill_color([0,.5,.55,.5]) 
            self.ids.eightPM.fill_color = [0,.5,.6,.5]
            self.ids.eightPM._set_fill_color([0,.5,.6,.5]) 
            self.ids.ninePM.fill_color = [0,.5,.65,.5]
            self.ids.ninePM._set_fill_color([0,.5,.65,.5])
            # Changes colors of buttons on Add Event Screen
            self.ids.add6AM.md_bg_color=[0, 1, 0, .5]
            self.ids.add7AM.md_bg_color=[0, 1, 0, .5]
            self.ids.add8AM.md_bg_color=[0, 1, 0, .5]
            self.ids.add9AM.md_bg_color=[0, 1, 0, .5]
            self.ids.add10AM.md_bg_color=[0, 1, 0, .5]
            self.ids.add11AM.md_bg_color=[0, 1, 0, .5]
            self.ids.add12PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add1PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add2PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add3PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add4PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add5PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add6PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add7PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add8PM.md_bg_color=[0, 1, 0, .5]
            self.ids.add9PM.md_bg_color=[0, 1, 0, .5]
            
            
        
            self.overview_images(root, origIMG1, origIMG2)
        elif style == "CITRUS":
            self.ids.contentEventMain.fill_color = [1, 1, 0, .5]
            self.ids.contentEventMain._set_fill_color([1, 1, 0, .5])
        
            self.ids.contentTODOMain.fill_color = [1, .5, 0, .5]
            self.ids.contentTODOMain._set_fill_color([1, .5, 0, .5])
        
            self.ids.addToDo.md_bg_color = [1, .5, 0, .8]
            self.ids.addTask.md_bg_color = [1, .5, 0, .8]
            
            #Change colors of add event screen (left side)
            self.ids.contentEvent.fill_color = [1, .3, 0, .5]
            self.ids.contentEvent._set_fill_color([1, .3, 0, .5]) 
            self.ids.sevenAM.fill_color = [1, .4, 0, .5]
            self.ids.sevenAM._set_fill_color([1, .4, 0, .5]) 
            self.ids.eightAM.fill_color = [1, .5, 0, .5]
            self.ids.eightAM._set_fill_color([1, .5, 0, .5]) 
            self.ids.nineAM.fill_color = [1, .6, 0, .5]
            self.ids.nineAM._set_fill_color([1, .6, 0, .5]) 
            self.ids.tenAM.fill_color = [1, .7, 0, .5]
            self.ids.tenAM._set_fill_color([1, .7, 0, .5]) 
            self.ids.elevenAM.fill_color = [1, .8, 0, .5]
            self.ids.elevenAM._set_fill_color([1, .8, 0, .5]) 
            self.ids.noon.fill_color = [1, .9, 0, .5]
            self.ids.noon._set_fill_color([1, .9, 0, .5]) 
            self.ids.onePM.fill_color = [1, 1, 0, .5]
            self.ids.onePM._set_fill_color([1, 1, 0, .5]) 
            #Change colors of add event screen (right side)
            self.ids.twoPM.fill_color = [1, .3, 0, .5]
            self.ids.twoPM._set_fill_color([1, .3, 0, .5]) 
            self.ids.threePM.fill_color = [1, .4, 0, .5]
            self.ids.threePM._set_fill_color([1, .4, 0, .5]) 
            self.ids.fourPM.fill_color = [1, .5, 0, .5]
            self.ids.fourPM._set_fill_color([1, .5, 0, .5]) 
            self.ids.fivePM.fill_color = [1, .6, 0, .5]
            self.ids.fivePM._set_fill_color([1, .6, 0, .5]) 
            self.ids.sixPM.fill_color = [1, .7, 0, .5]
            self.ids.sixPM._set_fill_color([1, .7, 0, .5]) 
            self.ids.sevenPM.fill_color = [1, .8, 0, .5]
            self.ids.sevenPM._set_fill_color([1, .8, 0, .5]) 
            self.ids.eightPM.fill_color = [1, .9, 0, .5]
            self.ids.eightPM._set_fill_color([1, .9, 0, .5]) 
            self.ids.ninePM.fill_color = [1, 1, 0, .5]
            self.ids.ninePM._set_fill_color([1, 1, 0, .5]) 
            # Changes colors of buttons on Add Event Screen
            self.ids.add6AM.md_bg_color=[1, .5, 0, .8]
            self.ids.add7AM.md_bg_color=[1, .5, 0, .8]
            self.ids.add8AM.md_bg_color=[1, .5, 0, .8]
            self.ids.add9AM.md_bg_color=[1, .5, 0, .8]
            self.ids.add10AM.md_bg_color=[1, .5, 0, .8]
            self.ids.add11AM.md_bg_color=[1, .5, 0, .8]
            self.ids.add12PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add1PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add2PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add3PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add4PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add5PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add6PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add7PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add8PM.md_bg_color=[1, .5, 0, .8]
            self.ids.add9PM.md_bg_color=[1, .5, 0, .8]

            self.overview_images(root, citrusIMG1, citrusIMG2)
        elif style == "PINK":
            self.ids.contentEventMain.fill_color = [1, 0, .1, .5]
            self.ids.contentEventMain._set_fill_color([1, 0, .1, .5])
        
            self.ids.contentTODOMain.fill_color = [.8, 0, .5, .5]
            self.ids.contentTODOMain._set_fill_color([.8, 0, .5, .5])
        
            self.ids.addToDo.md_bg_color = [1, 0, 0, .8]
            self.ids.addTask.md_bg_color = [1, 0, 0, .8]
            
            #Change colors of add event screen (left side)
            self.ids.contentEvent.fill_color = [.8, 0, .5, .5]
            self.ids.contentEvent._set_fill_color([.8, 0, .5, .5]) 
            self.ids.sevenAM.fill_color = [.85,0,.45,0.5]
            self.ids.sevenAM._set_fill_color([.85,0,.45,0.5]) 
            self.ids.eightAM.fill_color = [.85,0,.4,0.5]
            self.ids.eightAM._set_fill_color([.85,0,.4,0.5]) 
            self.ids.nineAM.fill_color = [.9,0,.4,0.5]
            self.ids.nineAM._set_fill_color([.9,0,.4,0.5]) 
            self.ids.tenAM.fill_color = [.9,0,.3,0.5]
            self.ids.tenAM._set_fill_color([.9,0,.3,0.5]) 
            self.ids.elevenAM.fill_color = [.95,0,.3,0.5]
            self.ids.elevenAM._set_fill_color([.95,0,.3,0.5]) 
            self.ids.noon.fill_color = [1,0,.2,0.5]
            self.ids.noon._set_fill_color([1,0,.2,0.5]) 
            self.ids.onePM.fill_color = [1, 0, .1, .5]
            self.ids.onePM._set_fill_color([1, 0, .1, .5]) 
            #Change colors of add event screen (right side)
            self.ids.twoPM.fill_color = [.8, 0, .5, .5]
            self.ids.twoPM._set_fill_color([.8, 0, .5, .5]) 
            self.ids.threePM.fill_color = [.85,0,.45,0.5]
            self.ids.threePM._set_fill_color([.85,0,.45,0.5]) 
            self.ids.fourPM.fill_color = [.85,0,.4,0.5]
            self.ids.fourPM._set_fill_color([.85,0,.4,0.5]) 
            self.ids.fivePM.fill_color = [.9,0,.4,0.5]
            self.ids.fivePM._set_fill_color([.9,0,.4,0.5]) 
            self.ids.sixPM.fill_color = [.9,0,.3,0.5]
            self.ids.sixPM._set_fill_color([.9,0,.3,0.5]) 
            self.ids.sevenPM.fill_color = [.95,0,.3,0.5]
            self.ids.sevenPM._set_fill_color([.95,0,.3,0.5]) 
            self.ids.eightPM.fill_color = [1,0,.2,0.5]
            self.ids.eightPM._set_fill_color([1,0,.2,0.5]) 
            self.ids.ninePM.fill_color = [1, 0, .1, .5]
            self.ids.ninePM._set_fill_color([1, 0, .1, .5]) 
            # Changes colors of buttons on Add Event Screen
            self.ids.add6AM.md_bg_color=[1, 0, 0, .8]
            self.ids.add7AM.md_bg_color=[1, 0, 0, .8]
            self.ids.add8AM.md_bg_color=[1, 0, 0, .8]
            self.ids.add9AM.md_bg_color=[1, 0, 0, .8]
            self.ids.add10AM.md_bg_color=[1, 0, 0, .8]
            self.ids.add11AM.md_bg_color=[1, 0, 0, .8]
            self.ids.add12PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add1PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add2PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add3PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add4PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add5PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add6PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add7PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add8PM.md_bg_color=[1, 0, 0, .8]
            self.ids.add9PM.md_bg_color=[1, 0, 0, .8]
            
            self.overview_images(root, pinkIMG1, pinkIMG2)
        elif style == "Spooky":
            self.ids.contentEventMain.fill_color = [.8,0,.8,0.6]
            self.ids.contentEventMain._set_fill_color([.8,0,.8,0.6])
        
            self.ids.contentTODOMain.fill_color = [.8,.7,.8,0.3]
            self.ids.contentTODOMain._set_fill_color([.8,.7,.8,0.3])
        
            self.ids.addToDo.md_bg_color = [1, 0, 1, .5]
            self.ids.addTask.md_bg_color = [1, 0, 1, .5]
            
            # Changes colors of Add Event Screen
            self.ids.contentEvent.fill_color = [.8,.7,.8,0.6]
            self.ids.contentEvent._set_fill_color([.8,.7,.8,0.6]) 
            self.ids.sevenAM.fill_color = [.8,.6,.8,0.6]
            self.ids.sevenAM._set_fill_color([.8,.6,.8,0.6]) 
            self.ids.eightAM.fill_color = [.8,.5,.8,0.6]
            self.ids.eightAM._set_fill_color([.8,.5,.8,0.6]) 
            self.ids.nineAM.fill_color = [.8,.4,.8,0.6]
            self.ids.nineAM._set_fill_color([.8,.4,.8,0.6]) 
            self.ids.tenAM.fill_color = [.8,.3,.8,0.6]
            self.ids.tenAM._set_fill_color([.8,.3,.8,0.6]) 
            self.ids.elevenAM.fill_color = [.8,.2,.8,0.6]
            self.ids.elevenAM._set_fill_color([.8,.2,.8,0.6]) 
            self.ids.noon.fill_color = [.8,.1,.8,0.6]
            self.ids.noon._set_fill_color([.8,.1,.8,0.6]) 
            self.ids.onePM.fill_color = [.8,0,.8,0.6]
            self.ids.onePM._set_fill_color([.8,0,.8,0.6]) 
            self.ids.twoPM.fill_color = [.8,.7,.8,0.6]
            self.ids.twoPM._set_fill_color([.8,.7,.8,0.6]) 
            self.ids.threePM.fill_color = [.8,.6,.8,0.6]
            self.ids.threePM._set_fill_color([.8,.6,.8,0.6]) 
            self.ids.fourPM.fill_color = [.8,.5,.8,0.6]
            self.ids.fourPM._set_fill_color([.8,.5,.8,0.6]) 
            self.ids.fivePM.fill_color = [.8,.4,.8,0.6]
            self.ids.fivePM._set_fill_color([.8,.4,.8,0.6]) 
            self.ids.sixPM.fill_color = [.8,.3,.8,0.6]
            self.ids.sixPM._set_fill_color([.8,.3,.8,0.6]) 
            self.ids.sevenPM.fill_color = [.8,.2,.8,0.6]
            self.ids.sevenPM._set_fill_color([.8,.2,.8,0.6]) 
            self.ids.eightPM.fill_color = [.8,.1,.8,0.6]
            self.ids.eightPM._set_fill_color([.8,.1,.8,0.6]) 
            self.ids.ninePM.fill_color = [.8,0,.8,0.6]
            self.ids.ninePM._set_fill_color([.8,0,.8,0.6]) 
            # Changes colors of buttons on Add Event Screen
            self.ids.add6AM.md_bg_color=[1, 0, 1, .5]
            self.ids.add7AM.md_bg_color=[1, 0, 1, .5]
            self.ids.add8AM.md_bg_color=[1, 0, 1, .5]
            self.ids.add9AM.md_bg_color=[1, 0, 1, .5]
            self.ids.add10AM.md_bg_color=[1, 0, 1, .5]
            self.ids.add11AM.md_bg_color=[1, 0, 1, .5]
            self.ids.add12PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add1PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add2PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add3PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add4PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add5PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add6PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add7PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add8PM.md_bg_color=[1, 0, 1, .5]
            self.ids.add9PM.md_bg_color=[1, 0, 1, .5]
            
    
            self.overview_images(root, img_1, img_2)

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        
        c = conn.cursor()
        query = "SELECT * FROM colors WHERE userID = %s"
        c.execute(query, (config.userid,))
        records = c.fetchall()
        
        if records:
            c.execute("UPDATE colors SET style = %s, userid = %s", (style, config.userid))
        else:
            c.execute("INSERT INTO colors (style, userid) VALUES (%s, %s)", (style, config.userid))

        conn.commit()
        conn.close()

    def postEvents(self, root):

        if config.store.exists('account'):
            config.userid = config.store.get('account')['userid']

     #   self.ids.contentEventMain.text = '' # reset textfield to be blank

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM events WHERE userID = %s AND dateID = %s"
        c.execute(query, (config.userid, config.dateID,))
        records = c.fetchall()
        records.sort(key = lambda date: datetime.strptime(date[2], "%H:%M"))

        # RED 1, 0, 0, 1
        # GREEN 0, 1, 0, 1
        # YELLOW 1, 1, 0, 1
        # BLUE 0, 0, 1, 1
        # PURPLE 1, 0, 1, 1
        # DEFAULT 0, 0, 0, 1
        self.ids['eventContainer'].clear_widgets()
        if records:
            for items in records:
                self.ids['eventContainer'].add_widget(EventItemWithCheckbox(text= '[b]' + items[4] + '[/b]'))
                self.ids['eventContainer'].children[0].ids['eventIcon'].icon = items[6]

                if items[7] == "RED":
                    self.ids['eventContainer'].children[0].ids['eventIcon'].text_color = 1, 0, 0, 1
                    self.ids['eventContainer'].children[0].ids['eventIcon'].set_text_color([1, 0, 0, 1])
                elif items[7] == "GREEN":
                    self.ids['eventContainer'].children[0].ids['eventIcon'].text_color = 0, 1, 0, 1
                    self.ids['eventContainer'].children[0].ids['eventIcon'].set_text_color([0, 1, 0, 1])
                elif items[7] == "YELLOW":
                    self.ids['eventContainer'].children[0].ids['eventIcon'].text_color = 1, 1, 0, 1
                    self.ids['eventContainer'].children[0].ids['eventIcon'].set_text_color([1, 1, 0, 1])
                elif items[7] == "BLUE":
                    self.ids['eventContainer'].children[0].ids['eventIcon'].text_color = 0, 0, 1, 1
                    self.ids['eventContainer'].children[0].ids['eventIcon'].set_text_color([0, 0, 1, 1])
                elif items[7] == "PURPLE":
                    self.ids['eventContainer'].children[0].ids['eventIcon'].text_color = 1, 0, 1, 1
                    self.ids['eventContainer'].children[0].ids['eventIcon'].set_text_color([1, 0, 1, 1])
                else:
                    self.ids['eventContainer'].children[0].ids['eventIcon'].text_color = 0, 0, 0, 1
                    self.ids['eventContainer'].children[0].ids['eventIcon'].set_text_color([0, 0, 0, 1])

        
        # easiest way to do things on pageload

        # load colors data
        query = "SELECT * FROM colors WHERE userID = %s"
        c.execute(query, (config.userid,))
        records = c.fetchall()
        
        if records:
            self.colorChanger(self, records[0][0])
        else:
            self.colorChanger(self, "OG")
        
        conn.commit()
        conn.close()
        

        
    
    def delete_eventFromAdd(self, root, time, the_event_item):
        deleteItem = ''
        
        if the_event_item.text[0:3] == '[b]':
            deleteItem = the_event_item.text.split('[b]')[1].split('[/b]')[0]
        else:
            deleteItem = the_event_item.text.split('[s][b]')[1].split('[/b][/s]')[0]

        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "DELETE FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (config.userid, deleteItem,))
        
        conn.commit()
        conn.close()
        
        # if records:
        #     for items in records:
        #         self.parent.remove_widget(the_event_item)
                
        
        
        
        #self.parent.remove_widget(the_event_item)
        if time == "6 AM":
            self.ids.contentEvent.disabled = False
            self.ids.contentEvent.text = ''
        elif time == "7 AM":
            self.ids.sevenAM.disabled = False
            self.ids.sevenAM.text = ''


class EventItemWithCheckbox(OneLineAvatarIconListItem):
    
    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk


    def markEvent(self, check, the_event_item):
        if check.active == True:
            the_event_item.text = '[s]'+the_event_item.text+'[/s]'
        else:
            the_event_item.text = the_event_item.text.split('[s]')[1].split('[/s]')[0]
