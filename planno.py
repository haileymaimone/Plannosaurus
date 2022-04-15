from kivy.lang import Builder
from kivymd.app import MDApp
from sdates import StartingDates
from wmanager import WindowManager
from db import Database
import config
import psycopg2
import psycopg2.extras
import datetime
from datetime import *
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.picker import MDDatePicker, MDThemePicker
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineListItem
from kivymd.uix.textfield import MDTextFieldRound, MDTextField, MDTextFieldRect
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.list import TwoLineAvatarIconListItem, OneLineAvatarIconListItem, ILeftBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.dialog import MDDialog
from kivy.utils import get_color_from_hex
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDRoundFlatButton


db = Database()
icon_text = ""
event_icon = ""
content_Event = ""
eleven_AM = ""
config.userid = -1
config.dateID = datetime.today().strftime("%m%d%Y")
config.store = JsonStore('account.json')
listindex = 0
theColor = ""
trigger = ""


class MainApp(MDApp):
    task_list_dialog = None
    customize_dialog = None
    addStickerDialog = None
    global listindex

    def build(self):
        Builder.load_file("app.kv")
        self.gen_cal(date.today())

        return WindowManager()

    def on_start(self):
        #Clock.schedule_once(self.set_screen, 5)
        self.set_screen(0)

    def set_screen(self, dt):

        if config.store.exists('account'):
            self.root.init_load(self.root)
            self.postTodo()
            self.root.postEvents(self.root)
            self.root.current = "main_sc"
        else:
            self.root.current = "login_sc"

    def logout(self):
        config.store.delete('account')
        self.root.current = "login_sc"

    def gen_cal(self, date):
        curr_day = date

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

        self.theDays = StartingDates(first_day, second_day, third_day, fourth_day, fifth_day, sixth_day, seventh_day)

    def pick_date(self):
        init_date = datetime.strptime(config.dateID, "%m%d%Y")
        init_day = init_date.strftime("%#d")
        init_month = init_date.strftime("%#m")
        init_year = init_date.strftime("%Y")
        date_dialog = MDDatePicker(year=int(init_year), month=int(init_month), day=int(init_day))
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()
        

    def on_save(self, instance, value, date_range):
        config.dateID = value.strftime("%m%d%Y")
        self.gen_cal(value)
        self.postTodo()
        self.root.postEvents(self.root)

        
        if self.theDays.day1 == value:
            self.root.ids.day1.text = "[color=#42f58d]"+ self.theDays.day1.strftime("%d") +"[/color]"
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day2 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = "[color=#42f58d]"+ self.theDays.day2.strftime("%d") +"[/color]"
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day3 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = "[color=#42f58d]"+ self.theDays.day3.strftime("%d") +"[/color]"
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day4 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = "[color=#42f58d]"+ self.theDays.day4.strftime("%d") +"[/color]"
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day5 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = "[color=#42f58d]"+ self.theDays.day5.strftime("%d") +"[/color]"
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        elif self.theDays.day6 == value:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = "[color=#42f58d]"+ self.theDays.day6.strftime("%d") +"[/color]"
            self.root.ids.day7.text = self.theDays.day7.strftime("%d")

        else:
            self.root.ids.day1.text = self.theDays.day1.strftime("%d")
            self.root.ids.day2.text = self.theDays.day2.strftime("%d")
            self.root.ids.day3.text = self.theDays.day3.strftime("%d")
            self.root.ids.day4.text = self.theDays.day4.strftime("%d")
            self.root.ids.day5.text = self.theDays.day5.strftime("%d")
            self.root.ids.day6.text = self.theDays.day6.strftime("%d")
            self.root.ids.day7.text = "[color=#42f58d]"+ self.theDays.day7.strftime("%d") +"[/color]"
        

        
    def login(self):
        loginCode = db.login(self.root.ids.user.text, self.root.ids.password.text)
        if loginCode == 1:
            self.root.ids.welcome_label.text = "Logged in successfully"
        else:
            self.root.ids.welcome_label.text = "User doesn't exist or incorrect password entered"
        return loginCode
        
    def newlist (self, listname):
        list = TabbedPanelItem(text = listname)
        mdtextfield = MDTextField(
            hint_text = "Add item to list",
            pos_hint = {'center_x': .5, 'center_y': .95},
            size_hint_x = None,
            width = 250)

        self.root.ids['listkv'].add_widget(list)
        fl = FloatLayout()
        list.add_widget(fl)
        fl.add_widget(mdtextfield)
        mdbutton = MDRoundFlatButton(
            text = "+",
            pos_hint = {'center_x': .79, 'center_y': .95},
            on_release = lambda widget:self.addlistitem(mdtextfield.text, fl)
        )
        fl.add_widget(mdbutton)

    def addlistitem(self, text, fl):
        listitem = OneLineListItem(text = text, pos_hint = {'center_x': .5, 'center_y': .5})
        fl.add_widget(listitem)
        

               
        
      	
        
    def clear(self):
        self.root.ids.welcome_label.text = "Please Login or Register"
        self.root.ids.user.text = ""
        self.root.ids.password.text = ""

    def register(self):
        firstName = self.root.ids.firstName.text
        lastName = self.root.ids.lastName.text
        enterPass = self.root.ids.enterPass.text
        passReEnter = self.root.ids.passReEnter.text
        emailPrompt = self.root.ids.emailPrompt.text
        regCode = db.register(firstName, lastName, enterPass, passReEnter, emailPrompt)

        if regCode == 0:
            self.root.ids.regLabel.text = "An account with these credentials already exists"
        elif regCode == 1:
            # redirect to login upon successful account creation
            self.root.current = "login_sc"
            self.root.ids.welcome_label.text = "Account created successfully"
        elif regCode == -1:
            self.root.ids.regLabel.text = "Fields cannot be empty."
        elif regCode == -2:
            self.root.ids.enterPass.text = ''
            self.root.ids.passReEnter.text = ''
            self.root.ids.regLabel.text = "Passwords must match."
        elif regCode == -3:
            self.root.ids.regLabel.text = "Password fields required."
   

    def left_cal(self):
        newDate = ""
        self.theDays.day1 = (self.theDays.day1 - timedelta(days = 7))
        self.theDays.day2 = (self.theDays.day2 - timedelta(days = 7))
        self.theDays.day3 = (self.theDays.day3 - timedelta(days = 7))
        self.theDays.day4 = (self.theDays.day4 - timedelta(days = 7))
        self.theDays.day5 = (self.theDays.day5 - timedelta(days = 7))
        self.theDays.day6 = (self.theDays.day6 - timedelta(days = 7))
        self.theDays.day7 = (self.theDays.day7 - timedelta(days = 7))

        day1 = self.theDays.day1
        day2 = self.theDays.day2
        day3 = self.theDays.day3
        day4 = self.theDays.day4
        day5 = self.theDays.day5
        day6 = self.theDays.day6
        day7 = self.theDays.day7
        
        dayHold = ""
        currMonth = ""
        currYear = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id
        
        if dayHold.text == self.root.ids.day1.text:
            currMonth = day1.strftime("%#m")
            currYear = day1.strftime("%Y")
            currDay = day1.strftime("%#d")
        elif dayHold.text == self.root.ids.day2.text:
            currMonth = day2.strftime("%#m")
            currYear = day2.strftime("%Y")
            currDay = day2.strftime("%#d")
        elif dayHold.text == self.root.ids.day3.text:
            currMonth = day3.strftime("%#m")
            currYear = day3.strftime("%Y")
            currDay = day3.strftime("%#d")
        elif dayHold.text == self.root.ids.day4.text:
            currMonth = day4.strftime("%#m")
            currYear = day4.strftime("%Y")
            currDay = day4.strftime("%#d")
        elif dayHold.text == self.root.ids.day5.text:
            currMonth = day5.strftime("%#m")
            currYear = day5.strftime("%Y")
            currDay = day5.strftime("%#d")
        elif dayHold.text == self.root.ids.day6.text:
            currMonth = day6.strftime("%#m")
            currYear = day6.strftime("%Y")
            currDay = day6.strftime("%#d")
        else:
            currMonth = day7.strftime("%#m")
            currYear = day7.strftime("%Y")
            currDay = day7.strftime("%#d")

        
        self.root.ids.day1.text = day1.strftime("%d")
        self.root.ids.day2.text = day2.strftime("%d")
        self.root.ids.day3.text = day3.strftime("%d")
        self.root.ids.day4.text = day4.strftime("%d")
        self.root.ids.day5.text = day5.strftime("%d")
        self.root.ids.day6.text = day6.strftime("%d")
        self.root.ids.day7.text = day7.strftime("%d")

        newDate = currMonth + currDay + currYear
        
        config.dateID = datetime.strptime(newDate, '%m%d%Y').strftime("%m%d%Y")

        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted
        self.postTodo()
        self.root.postEvents(self.root)

    def right_cal(self):
        self.theDays.day1 = (self.theDays.day1 + timedelta(days = 7))
        self.theDays.day2 = (self.theDays.day2 + timedelta(days = 7))
        self.theDays.day3 = (self.theDays.day3 + timedelta(days = 7))
        self.theDays.day4 = (self.theDays.day4 + timedelta(days = 7))
        self.theDays.day5 = (self.theDays.day5 + timedelta(days = 7))
        self.theDays.day6 = (self.theDays.day6 + timedelta(days = 7))
        self.theDays.day7 = (self.theDays.day7 + timedelta(days = 7))

        day1 = self.theDays.day1
        day2 = self.theDays.day2
        day3 = self.theDays.day3
        day4 = self.theDays.day4
        day5 = self.theDays.day5
        day6 = self.theDays.day6
        day7 = self.theDays.day7

        dayHold = ""
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    dayHold = self.root.ids[key] # save reference to current day id

        if dayHold.text == self.root.ids.day1.text:
            currMonth = day1.strftime("%#m")
            currYear = day1.strftime("%Y")
            currDay = day1.strftime("%#d")
        elif dayHold.text == self.root.ids.day2.text:
            currMonth = day2.strftime("%#m")
            currYear = day2.strftime("%Y")
            currDay = day2.strftime("%#d")
        elif dayHold.text == self.root.ids.day3.text:
            currMonth = day3.strftime("%#m")
            currYear = day3.strftime("%Y")
            currDay = day3.strftime("%#d")
        elif dayHold.text == self.root.ids.day4.text:
            currMonth = day4.strftime("%#m")
            currYear = day4.strftime("%Y")
            currDay = day4.strftime("%#d")
        elif dayHold.text == self.root.ids.day5.text:
            currMonth = day5.strftime("%#m")
            currYear = day5.strftime("%Y")
            currDay = day5.strftime("%#d")
        elif dayHold.text == self.root.ids.day6.text:
            currMonth = day6.strftime("%#m")
            currYear = day6.strftime("%Y")
            currDay = day6.strftime("%#d")
        else:
            currMonth = day7.strftime("%#m")
            currYear = day7.strftime("%Y")
            currDay = day7.strftime("%#d")
        
        self.root.ids.day1.text = day1.strftime("%d")
        self.root.ids.day2.text = day2.strftime("%d")
        self.root.ids.day3.text = day3.strftime("%d")
        self.root.ids.day4.text = day4.strftime("%d")
        self.root.ids.day5.text = day5.strftime("%d")
        self.root.ids.day6.text = day6.strftime("%d")
        self.root.ids.day7.text = day7.strftime("%d")

        newDate = currMonth + currDay + currYear
        config.dateID = datetime.strptime(newDate, '%m%d%Y').strftime("%m%d%Y")

        dayHold.text = "[color=#42f58d]" + dayHold.text + "[/color]" # change text color of same day of the week when shifted
        self.postTodo()
        self.root.postEvents(self.root)
                
    def current_day(self, instance):
        newDate = ''
        prevDay = ''
        currDay = ''
        currKey = ''
        prevKey = ''
        temp = ''
        tempMonth = ''
        for key, val in self.root.ids.items():
            if "day" in key:
                if "[" in self.root.ids[key].text:
                    self.root.ids[key].text = self.root.ids[key].text.split(']')[1].split('[')[0]
                    prevDay = self.root.ids[key].text
                    prevKey = key
                if instance.text[0:2] == self.root.ids[key].text:
                    currDay = self.root.ids[key].text
                    currKey = key

        newDate = list(config.dateID)
        newDate[2] = instance.text[0]
        newDate[3] = instance.text[1]
        newDate = ''.join(newDate)
        
        if prevDay == "01" and currDay > prevDay and currKey < prevKey:
            temp = datetime.strptime(config.dateID, "%m%d%Y")
            tempMonth = str(temp.month - 1)
            temp = tempMonth + newDate[2:4] + newDate[4:]
            config.dateID = datetime.strptime(temp, '%m%d%Y').strftime("%m%d%Y")
        elif prevDay == "28" or prevDay == "30" or prevDay == "31" and currDay < prevDay and currKey > prevKey:
            temp = datetime.strptime(config.dateID, "%m%d%Y")
            tempMonth = str(temp.month + 1)
            temp = tempMonth + newDate[2:4] + newDate[4:]
            config.dateID = datetime.strptime(temp, '%m%d%Y').strftime("%m%d%Y")
        else:
            config.dateID = datetime.strptime(newDate, '%m%d%Y').strftime("%m%d%Y")
        
        instance.text = "[color=#42f58d]" + instance.text + "[/color]"
        self.postTodo()
        self.root.postEvents(self.root)

    def delete_event(self, root, the_event_item):
        global content_Event
        global eleven_AM
        deleteItem = ''
        
        if the_event_item.text[0:3] == '[b]':
            deleteItem = the_event_item.text.split('[b]')[1].split('[/b]')[0]
        else:
            deleteItem = the_event_item.text.split('[s][b]')[1].split('[/b][/s]')[0]
        

        conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "SELECT time FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (config.userid, deleteItem,))
        timeofEvent = c.fetchall()

        
        query = "DELETE FROM events WHERE userid = %s AND messageBody = %s"
        c.execute(query, (config.userid, deleteItem,))
        
        conn.commit()
        conn.close()
        
        if str(timeofEvent) == "[('6 AM',)]":
            self.root.ids.contentEvent.disabled=False
            self.root.ids.contentEvent.text = ''
            self.root.ids.add6AM.disabled=False
        elif str(timeofEvent) == "[('7 AM',)]":
            self.root.ids.sevenAM.disabled=False
            self.root.ids.sevenAM.text = ''
            self.root.ids.add7AM.disabled=False
        elif str(timeofEvent) == "[('8 AM',)]":
            self.root.ids.eightAM.disabled=False
            self.root.ids.eightAM.text = ''
            self.root.ids.add8AM.disabled=False
        elif str(timeofEvent) == "[('9 AM',)]":
            self.root.ids.nineAM.disabled=False
            self.root.ids.nineAM.text = ''
            self.root.ids.add9AM.disabled=False
        elif str(timeofEvent) == "[('10 AM',)]":
            self.root.ids.tenAM.disabled=False
            self.root.ids.tenAM.text = ''
            self.root.ids.add10AM.disabled=False
        elif str(timeofEvent) == "[('11 AM',)]":
            self.root.ids.elevenAM.disabled=False
            self.root.ids.elevenAM.text = ''
            self.root.ids.add11AM.disabled=False
        elif str(timeofEvent) == "[('12 PM',)]":
            self.root.ids.noon.disabled=False
            self.root.ids.noon.text = ''
            self.root.ids.add12PM.disabled=False
        elif str(timeofEvent) == "[('1 PM',)]":
            self.root.ids.onePM.disabled=False
            self.root.ids.onePM.text = ''
            self.root.ids.add1PM.disabled=False
        elif str(timeofEvent) == "[('2 PM',)]":
            self.root.ids.twoPM.disabled=False
            self.root.ids.twoPM.text = ''
            self.root.ids.add2PM.disabled=False
        elif str(timeofEvent) == "[('3 PM',)]":
            self.root.ids.threePM.disabled=False
            self.root.ids.threePM.text = ''
            self.root.ids.add3PM.disabled=False
        elif str(timeofEvent) == "[('4 PM',)]":
            self.root.ids.fourPM.disabled=False
            self.root.ids.fourPM.text = ''
            self.root.ids.add4PM.disabled=False
        elif str(timeofEvent) == "[('5 PM',)]":
            self.root.ids.fivePM.disabled=False
            self.root.ids.fivePM.text = ''
            self.root.ids.add5PM.disabled=False
        elif str(timeofEvent) == "[('6 PM',)]":
            self.root.ids.sixPM.disabled=False
            self.root.ids.sixPM.text = ''
            self.root.ids.add6PM.disabled=False
        elif str(timeofEvent) == "[('7 PM',)]":
            self.root.ids.sevenPM.disabled=False
            self.root.ids.sevenPM.text = ''
            self.root.ids.add7PM.disabled=False
        elif str(timeofEvent) == "[('8 PM',)]":
            self.root.ids.eightPM.disabled=False
            self.root.ids.eightPM.text = ''
            self.root.ids.add8PM.disabled=False
        elif str(timeofEvent) == "[('9 PM',)]":
            self.root.ids.ninePM.disabled=False
            self.root.ids.ninePM.text = ''
            self.root.ids.add9PM.disabled=False
        
        self.root.ids.eventContainer.remove_widget(the_event_item)
        
        
    def changeIt(self, rect_color):
        self.rect_color=1,0,0,1
        return

        
    def show_customize_dialog(self):
        if not self.customize_dialog:
            self.customize_dialog=MDDialog(
                title="Customize",
                type="custom",
                content_cls=CustomizeDialog(),
            )
        self.customize_dialog.open()
    
    
    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def update_theme(self):
        # todo: modify it to save a theme for each user
        conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()

        c.execute("SELECT * FROM theme")
        curr_theme = c.fetchall()

        if len(curr_theme) == 0:
            c.execute("INSERT INTO theme (primary_palette, accent_palette, theme_style) VALUES (%s, %s, %s)",
            (self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style))
        else:
            c.execute("UPDATE theme SET primary_palette = %s, accent_palette = %s, theme_style = %s", 
            (self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style))

        conn.commit()
        conn.close()
        
    
    def customizeColor(self, root):
        
        self.root.ids.contentEventMain.fill_color = .5, 0, 0, .5
    
    def close_customize_dialog(self):
        self.customize_dialog.dismiss()
    
    def showAddSticker_dialog(self, eventItem):
        global event_icon
        if not self.addStickerDialog:
            self.addStickerDialog=MDDialog(
                title="Add Sticker",
                type="custom",
                content_cls=AddStickerDialog(),
            )
        event_icon = eventItem
        self.addStickerDialog.open()

    def update_sticker(self, text):
        global event_icon
        event_icon.ids.eventIcon.icon = text
        conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "UPDATE events SET sticker = %s"
        c.execute(query, (text,))
        conn.commit()
        conn.close()

    
    def update_stickerColor(self, color):
        global event_icon
        theColor = ""

        if color == "RED":
            event_icon.ids.eventIcon.text_color = 1, 0, 0, 1
            theColor = "RED"
        elif color == "GREEN":
            event_icon.ids.eventIcon.text_color = 0, 1, 0, 1
            theColor = "GREEN"
        elif color == "YELLOW":
            event_icon.ids.eventIcon.text_color = 1, 1, 0, 1
            theColor = "YELLOW"
        elif color == "BLUE":
            event_icon.ids.eventIcon.text_color = 0, 0, 1, 1
            theColor = "BLUE"
        elif color == "PURPLE":
            event_icon.ids.eventIcon.text_color = 1, 0, 1, 1
            theColor = "PURPLE"
        self.save_stickerColor(theColor)

    def save_stickerColor(self, color):
         # 0, 0, 0, 1 is default
        conn = psycopg2.connect(
            host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            database = "d19re7njihace8",
            user = "lveasasuicarlg",
            password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "UPDATE events SET color = %s"
        c.execute(query, (color,))
        conn.commit()
        conn.close()
    
    def show_todolist_dialog(self):
        if not self.task_list_dialog:
            self.task_list_dialog=MDDialog(
                title="Create To-Do",
                type="custom",
                content_cls=DialogContent(),
            )
        self.task_list_dialog.content_cls.update_date()
        self.task_list_dialog.open()
    
    def close_todolist_dialog(self):
        self.task_list_dialog.dismiss()

    def save_addSticker(self):
        global icon_text
        global event_icon
        self.addStickerDialog.content_cls.get_sticker()
        self.update_sticker(icon_text)
    
    def close_addSticker_dialog(self):
        self.addStickerDialog.dismiss()
    
    def add_todo(self, task, task_date):

        conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        
        if config.store.exists('account'):
            config.userid = config.store.get('account')['userid']
            
        todoMessage = task.text
        
        c.execute("INSERT INTO todos(dateID, timestamp, completed, todoItem, userID) VALUES (%s, %s, %s, %s, %s)", (config.dateID, task_date, 0, todoMessage, config.userid))
        self.root.ids['container'].add_widget(ListItemWithCheckbox(text='[b]'+task.text+'[/b]', secondary_text='[size=12]'+'have done by: '+ task_date+'[/size]'))
        task.text=''
        
       
        conn.commit()
        conn.close()


    def postTodo(self):

        if config.store.exists('account'):
            config.userid = config.store.get('account')['userid']

        #self.root.ids.contentTODOMain.text = '' # reset textfield to be blank

        conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        c = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM todos WHERE userID = %s AND dateID = %s"
        c.execute(query, (config.userid, config.dateID,))
        records = c.fetchall()
        


        self.root.ids['container'].clear_widgets()
        if records:
            for items in records:
                if items[3] == 1:
                    self.root.ids['container'].add_widget(ListItemWithCheckbox(text= '[s][b]' + items[4] + '[/b][/s]'))
                    self.root.ids['container'].children[0].ids['check'].active = True
                elif items[3] == 0:
                    self.root.ids['container'].add_widget(ListItemWithCheckbox(text= '[b]' + items[4] + '[/b]'))
        
         # load theme data
        c.execute("SELECT * FROM theme")
        curr_theme = c.fetchall()
        
        if len(curr_theme) == 0:
            # default theme  
            self.theme_cls.primary_palette = "Green" 
            self.theme_cls.accent_palette = "Amber"
            self.theme_cls.theme_style = "Light"
            self.theme_cls.primary_hue = "500"
        else:
            # theme saved in database
            self.theme_cls.primary_palette = curr_theme[0][0]
            self.theme_cls.accent_palette = curr_theme[0][1]
            self.theme_cls.theme_style = curr_theme[0][2]
            self.theme_cls.primary_hue = "500"

        
        conn.commit()
        conn.close()
        #task.text = ''


class CustomizeDialog(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
       # self.ids.date_text.text = str(datetime.now().strftime('%A %d %B %Y'))

class AddStickerDialog(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        md_stickers = ["cat",
        "christianity",
        "coffee",
        "coffin",
        "crown",
        "dance-pole",
        "diamond-stone",
        "dumbbell",
        "dog",
        "doctor",
        "email-outline",
        "emoticon-poop",
        "flower",
        "food",
        "foot-print",
        "ghost-outline",
        "glass-cocktail",
        "google-downasaur",
        "airplane",
        "baby-carriage",
        "bat",
        "beach",
        "beer-outline",
        "book-open-variant",
        "cake-variant",
        "cannabis",
        "car",
        "cards-heart",
        "alarm",
        "halloween",
        "deathly-hallows",
        "lightning-bolt",
        "yoga",
        "whatsapp",
        "web",
        "ultra-high-definition",
        "twitter",
        "turkey",
        "triforce",
        "zodiac-aquarius",
        "zodiac-aries",
        "zodiac-cancer",
        "zodiac-capricorn",
        "zodiac-gemini",
        "zodiac-leo",
        "zodiac-libra",
        "zodiac-pisces",
        "zodiac-sagittarius",
        "zodiac-scorpio",
        "zodiac-taurus",
        "zodiac-virgo"]
        sticker_list = [
            {
                "viewclass": "StickerItem",
                "icon": f"{i}",
                "text": f"{i}",
                "on_release": lambda x = f"{i}": self.set_sticker(x),
            } for i in md_stickers
        ]
        self.menu = MDDropdownMenu(
            caller = self.ids.stickers_list,
            items = sticker_list,
            position = "center",
            width_mult = 4,
        )
        self.menu.bind()

    def set_sticker(self, item):
        global icon_text
        self.ids.stickers_list.set_item(item)
        icon_text = item
        self.menu.dismiss()
    
    def get_sticker(self):
        global icon_text
        return icon_text
        

class DialogContent(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        formatedDate = datetime.strptime(config.dateID, "%m%d%Y")
        self.ids.date_text.text = str(formatedDate.strftime("%A %d %B %Y"))
        

    def update_date(self):
        formatedDate = datetime.strptime(config.dateID, "%m%d%Y")
        self.ids.date_text.text = str(formatedDate.strftime("%A %d %B %Y"))


    def show_date_picker(self):
        init_date = datetime.strptime(config.dateID, "%m%d%Y")
        init_day = init_date.strftime("%#d")
        init_month = init_date.strftime("%#m")
        init_year = init_date.strftime("%Y")
        date_dialog = MDDatePicker(year=int(init_year), month=int(init_month), day=int(init_day))
        date_dialog.bind(on_save = self.on_save)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%A %d %B %Y')
        self.ids.date_text.text = str(date)

class EventItemWithCheckbox(OneLineAvatarIconListItem):
    
    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk


    def markEvent(self, check, the_event_item):
        if check.active == True:
            the_event_item.text = '[s]'+the_event_item.text+'[/s]'
        else:
            the_event_item.text = the_event_item.text.split('[s]')[1].split('[/s]')[0]


        
        
    
    
        
# below class for Todos
class ListItemWithCheckbox(OneLineAvatarIconListItem):


    def __init__(self, pk=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk


    def mark(self, check, the_list_item):
        
        if check.active == True:
            conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
            )
            markedItem = the_list_item.text.split('[b]')[1].split('[/b]')[0]
            
            # Create a cursor
            c = conn.cursor()
            query = "UPDATE todos SET completed = 1 WHERE userid = %s AND todoItem = %s"
            c.execute(query, (config.userid, markedItem,))

            conn.commit()
            conn.close()
            the_list_item.text = '[s][b]'+the_list_item.text+'[/b][/s]'
        else:
            the_list_item.text = the_list_item.text.split('[s]')[1].split('[/s]')[0]
            conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
            )
            markedItem = the_list_item.text.split('[b]')[1].split('[/b]')[0]
            
            # Create a cursor
            c = conn.cursor()
            query = "UPDATE todos SET completed = 0 WHERE userid = %s AND todoItem = %s"
            c.execute(query, (config.userid, markedItem,))
        
            conn.commit()
            conn.close()

    def delete_item(self, the_list_item):
        deleteItem = ''

        if the_list_item.text[0:3] == '[b]':
            deleteItem = the_list_item.text.split('[b]')[1].split('[/b]')[0]
        else:
            deleteItem = the_list_item.text.split('[s][b]')[1].split('[/b][/s]')[0]
        

        conn = psycopg2.connect(
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
        )

        # Create a cursor
        c = conn.cursor()
        query = "DELETE FROM todos WHERE userid = %s AND todoItem = %s"
        c.execute(query, (config.userid, deleteItem,))
        
        conn.commit()
        conn.close()
        self.parent.remove_widget(the_list_item)

class LeftCheckbox(ILeftBodyTouch, MDCheckbox):
    """creates checkbox for task"""

class StickerItem(OneLineAvatarIconListItem):
    icon = StringProperty()

MainApp().run()
