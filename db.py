import config
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('plannodb.db')

        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        # Create alarms table
        self.cursor.execute("CREATE TABLE if not exists alarms(alarmID integer PRIMARY KEY AUTOINCREMENT, dateID VARCHAR(255), alarmTime VARCHAR(255), alarmtext VARCHAR(255), userID INTEGER REFERENCES users(userID))")

         # Create users table
        self.cursor.execute("CREATE TABLE if not exists users(userID integer PRIMARY KEY AUTOINCREMENT, email VARCHAR(255), password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255))")
        
        # Create events table
        self.cursor.execute("CREATE TABLE if not exists events(eventID integer PRIMARY KEY AUTOINCREMENT, dateID VARCHAR(255), timestamp VARCHAR(255), time VARCHAR(255), messageBody VARCHAR(255), userID INTEGER REFERENCES users(userID), sticker VARCHAR(255), color VARCHAR(255))")

        # Create todos table
        self.cursor.execute("CREATE TABLE if not exists todos(todoID integer PRIMARY KEY AUTOINCREMENT, dateID VARCHAR(255), timestamp VARCHAR(255), completed int, todoItem VARCHAR(255), userID INTEGER REFERENCES users(userID))")

        # Create colors table
        self.cursor.execute("CREATE TABLE if not exists colors(style VARCHAR(255), userID INTEGER REFERENCES users(userID))")

        # Create theme table
        self.cursor.execute("CREATE TABLE if not exists theme(primary_palette VARCHAR(255), accent_palette VARCHAR(255), theme_style VARCHAR(255))")

        self.cursor.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (?, ?, ?, ?)", ("mai5013@calu.edu", "Bunnies", "Hailey", "Maimone"))

        self.conn.commit()

    def login(self, userText, passText):
        loginCode = -1

        c = self.conn.cursor()
        query = "SELECT * FROM users WHERE email = ?"
        c.execute(query, (userText,))
        records = c.fetchone()
        

        if records:
            if records[1] == userText and records[2] == passText:
                loginCode = 1
                config.store.put('account', userid=records[0], email=userText, password=passText)
            else:
                loginCode = -1
        else:
            loginCode = -1

        self.conn.commit()
        return loginCode

    def register(self, firstName, lastName, enterPass, passReEnter, emailPrompt):
        regCode = -1
        c = self.conn.cursor()

        if firstName == "" or lastName == "":
            regCode = -1
            return regCode
        elif enterPass != passReEnter:
            regCode = -2
            return regCode
        elif enterPass == "" or passReEnter == "":
            regCode = -3
            regLabel = "Password fields required."
            return regCode
        else:
            c.execute("SELECT * FROM users")
            records = c.fetchall()
        if records:
            for record in records:
                if record[1] == emailPrompt:
                    regCode = 0
                else:
                    c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (?, ?, ?, ?)", (emailPrompt, enterPass, firstName, lastName))
                    regCode = 1
                    config.store.put('account', userid=record[0], email=emailPrompt, password=enterPass)
                    break
        else:
            c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (?, ?, ?, ?)", (emailPrompt, enterPass, firstName, lastName))
            regCode = 1
            config.store.put('account', userid=record[0], email=emailPrompt, password=enterPass)
        
        self.conn.commit()
        
        return regCode
    
    def update_sticker(self, text, event_text):
        c = self.conn.cursor()
        query = "UPDATE events SET sticker = ? WHERE messageBody = ?"
        c.execute(query, (text, event_text))
        
        self.conn.commit()

    def save_stickerColor(self, color, event_text):
        c = self.conn.cursor()
        query = "UPDATE events SET color = ? WHERE messageBody = ?"
        c.execute(query, (color, event_text))

        self.conn.commit()

    def close_db(self):
        self.conn.close()
