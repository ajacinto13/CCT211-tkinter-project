from tkinter import *
from tkinter import ttk, messagebox
from assignment_db import AssignmentManager

class InstructorDashboard(Toplevel):
    def __init__(self, master, assignment_manager: AssignmentManager):
        super().__init__(master)
        self.title("Instructor Dashboard")
        self.geometry("600x400")
        self.assignment_manager = assignment_manager

        # add assignment frame        
        frame = Frame(self)
        frame.pack(pady=10)

        Label(frame, text="Title").grid(row=0, column=0, padx=5, pady=5)
        self.title_var = StringVar()
        Entry(frame, textvariable=self.title_var).grid(row=0, column=1, padx=5, pady=5)

        Label(frame, text="Description").grid(row=1, column=0, padx=5, pady=5)
        self.desc_var = StringVar()
        Entry(frame, textvariable=self.desc_var).grid(row=1, column=1, padx=5, pady=5)

        Label(frame, text="Due Date (YYYY-MM-DD)").grid(row=2, column=0, padx=5, pady=5)
        self.due_var = StringVar()
        Entry(frame, textvariable=self.due_var).grid(row=2, column=1, padx=5, pady=5)

        Button(frame, text="Add Assignment", command=self.add_assignment).grid(row=3, column=0, columnspan=2, pady=10)

        # --- assignment list treeview ---
        self.tree = ttk.Treeview(self, columns=("ID", "Title", "Description", "Due Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.pack(fill=BOTH, expand=True, pady=10)

        # delete button
        Button(self, text="Delete Selected", command=self.delete_assignment).pack(pady=5)

        # populate initial data
        self.load_assignments()

    def load_assignments(self):
        # clear treeview
        for row in self.tree.get_children():
            self.tree.delete(row)

        # load all assignments
        for assignment in self.assignment_manager.get_all_assignments():
            self.tree.insert("", "end", values=assignment)

    def add_assignment(self):
        title = self.title_var.get()
        desc = self.desc_var.get()
        due = self.due_var.get()

        if not title or not due:
            messagebox.showerror("Error", "Title and Due Date are required")
            return

        self.assignment_manager.create_assignment(title, desc, due)
        self.title_var.set("")
        self.desc_var.set("")
        self.due_var.set("")
        self.load_assignments()

    def delete_assignment(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select an assignment to delete")
            return
        assignment_id = self.tree.item(selected[0])["values"][0]
        self.assignment_manager.delete_assignment(assignment_id)
        self.load_assignments()
