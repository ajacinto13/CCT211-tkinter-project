import sqlite3

class AssignmentManager:
    def __init__(self):
        self.conn = sqlite3.connect("assignment_list.db")
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):

        # table for assignments
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS assignments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def create_assignment(self, title, description, due_date):
        # add a new assignment
        self.cursor.execute(
            "INSERT INTO assignments (title, description, due_date) VALUES (?, ?, ?)",
            (title, description, due_date)
        )
        self.conn.commit()

    def get_all_assignments(self):
        self.cursor.execute("SELECT * FROM assignments")
        return self.cursor.fetchall()

    def delete_assignment(self, assignment_id):
        # delete an assignment by its id
        self.cursor.execute("DELETE FROM assignments WHERE id=?", (assignment_id,))
        self.conn.commit()
