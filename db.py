import config
import psycopg2
import psycopg2.extras

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            host = "localhost",
            database = "plannodb",
            user = "postgres",
            password = "postgres",
            port = "5432",
            # host = "ec2-34-205-209-14.compute-1.amazonaws.com",
            # database = "d19re7njihace8",
            # user = "lveasasuicarlg",
            # password = "c372ee6ba2bc15c476bf85a8258fa444d2a51f4323b6903a1963c0c5fb118a08",
            # port = "5432",
        )

        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
         # Create users table
        self.cursor.execute("CREATE TABLE if not exists users(userID SERIAL PRIMARY KEY, email VARCHAR(255), password VARCHAR(255), firstName VARCHAR(255), lastName VARCHAR(255))")
        
        # Create events table
        self.cursor.execute("CREATE TABLE if not exists events(eventID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), time VARCHAR(255), messageBody VARCHAR(255), userID int REFERENCES users, sticker VARCHAR(255), color VARCHAR(255))")

        # Create todos table
        self.cursor.execute("CREATE TABLE if not exists todos(todoID SERIAL PRIMARY KEY, dateID VARCHAR(255), timestamp VARCHAR(255), completed int, todoItem VARCHAR(255), userID int REFERENCES users)")

        # Create colors table
        self.cursor.execute("CREATE TABLE if not exists colors(style VARCHAR(255), userID int REFERENCES users)")

        # Create theme table
        self.cursor.execute("CREATE TABLE if not exists theme(primary_palette VARCHAR(255), accent_palette VARCHAR(255), theme_style VARCHAR(255))")

        self.cursor.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", ("mai5013@calu.edu", "Bunnies", "Hailey", "Maimone"))

        self.conn.commit()

    def login(self, userText, passText):
        loginCode = -1

        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query = "SELECT * FROM users WHERE email = %s"
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
        c = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

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
                    c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (emailPrompt, enterPass, firstName, lastName))
                    regCode = 1
                    config.store.put('account', userid=record[0], email=emailPrompt, password=enterPass)
                    break
        else:
            c.execute("INSERT INTO users (email, password, firstName, lastName) VALUES (%s, %s, %s, %s)", (emailPrompt, enterPass, firstName, lastName))
            regCode = 1
            config.store.put('account', userid=record[0], email=emailPrompt, password=enterPass)
        
        self.conn.commit()
        
        return regCode

    def close_db(self):
        self.conn.close()
