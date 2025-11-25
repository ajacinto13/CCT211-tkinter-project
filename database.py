import sqlite3

class DatabaseManager:
	def __init__(self):
		self.conn = sqlite3.connect("student_system.db")
		self.cursor = self.conn.cursor()
		self.create_tables()

	def create_tables(self):
	
		# create database tables
		self.cursor.execute("""
        	CREATE TABLE IF NOT EXISTS users (
	            id INTEGER PRIMARY KEY AUTOINCREMENT,
	            username TEXT UNIQUE,
	            password TEXT,
	            role TEXT
        	)
    	""")
		self.conn.commit()

	def create_user(self, username, password, role):
	
		# add a new user
		try:
			self.cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
			self.conn.commit()
		except sqlite3.IntegrityError:
			pass # user already exists

	def verify_user(self, username, password):

		# verify username and password
		self.cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
		result = self.cursor.fetchone()

		# return role if correct, else None
		return result[0] if result else None

	def get_users(self):
	
		# return all user records
		self.cursor.execute("SELECT * FROM users")
		return self.cursor.fetchall()