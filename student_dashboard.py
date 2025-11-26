from tkinter import *
from tkinter import ttk
from assignment_db import AssignmentManager

class StudentDashboard(Toplevel):
	def __init__(self, master, assignment_manager: AssignmentManager):
		super().__init__(master)
		self.title('Student Dashboard')
		self.geometry('600x400')
		self.assignment_manager = assignment_manager

		Label(self, text='Assignments', font=('Arial', 14)).pack(pady=10)

		# treeview for assignments
		self.tree = ttk.Treeview(self, columns=('ID', 'Title', 'Description', 'Due Date'), show='headings')
		self.tree.heading('Title', text='Title')
		self.tree.heading('Description', text='Description')
		self.tree.heading('Due Date', text='Due Date')
		self.tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

		# populate the treeview
		self.load_assignments()

	def load_assignments(self):
		# clear treeview first
		for row in self.tree.get_children():
			self.tree.delete(row)

		#  fetch all assignments from the database
		assignments = self.assignment_manager.get_all_assignments()
		for assignment in assignments:
			self.tree.insert('', 'end', values=assignment)
