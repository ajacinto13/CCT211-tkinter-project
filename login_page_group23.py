from _pyrepl.commands import backspace
from random import uniform
from tkinter import *
from tkinter import messagebox


def center_window(win, width, height): # meant for the positioning and size of the window
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    # spawns the window in the center of the screen (dynamically)
    xval = (screen_width //2) - (width//2)
    yval = (screen_height //2) - (height//2)
    win.geometry('%dx%d+%d+%d' % (width, height, xval, yval))
    win.wm_resizable(False, False)

class loginPage(Frame):
    def __init__(self, parent, title, submit_callback):
        super().__init__(parent)
        self.title = title
        self.submit_callback = submit_callback


        form_frame = Frame(self)
        form_frame.pack(pady=10)

        self.name_var = StringVar()
        self.password_var = StringVar()

        Label(form_frame, text=self.title, font=(None, 14)).grid(row=0, column=0, columnspan=2, pady=5)
        Label(form_frame, text="Name").grid(row=1, column=0, sticky=E, padx=5, pady=5)
        Entry(form_frame, textvariable=self.name_var).grid(row=1, column=1, padx=5, pady=5)
        Label(form_frame, text="Password").grid(row=2, column=0, sticky=E, padx=5, pady=5)
        Entry(form_frame, show='*', textvariable=self.password_var).grid(row=2, column=1, padx=5, pady=5)

        Button(self, text='Submit', command=self.on_submit).pack(pady=10)

    def on_submit(self):
        name = self.name_var.get()
        password = self.password_var.get()
        
        # Temporarily disable validation - reopen after home page and database has been added
        #if not name or not password: # validation
         #   messagebox.showerror('Error', 'Please enter your name and password')
          #  return

        self.submit_callback(name, password)

class App(Tk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.size = size  # initializing the argument for future reference
        center_window(self, size[0], size[1])

        self.menubar = loginMenu(self, self.size)
        self.config(menu=self.menubar)

        self.student_login()  # default starting page

        # establishing the program logo
        self.fs_logo = PhotoImage(file='fslogo.png')
        self.iconphoto(True, self.fs_logo)

    def student_login(self):
        self.clear_window()
        form= loginPage(self, "Student Login", self.submit_student)
        form.pack()

    def instructor_login(self):
        self.clear_window()
        form= loginPage(self, "Instructor Login", self.submit_instructor)
        form.pack()

    def submit_student(self, name, password):
        print('Student login:', name, password)
        self.home_pg()

    def submit_instructor(self, name, password):
        print('Instructor login:', name, password)
        self.home_pg()

    def home_pg(self):
        win = Toplevel(self)
        center_window(win, self.size[0], self.size[1])
        win.title("Home")
        Label(win, text='Welcome').pack(pady=20)

    def clear_window(self):
        for widget in self.winfo_children():
            if not isinstance (widget, Menu):
                widget.destroy()




class loginMenu(Menu):
    def __init__(self, parent, size):
        super().__init__(parent)
        self.parent = parent  # referencing main window (App class)
        self.size = size  # keeps a reference

        menu1 = Menu(self, tearoff=0)  # aka "login"
        menu2 = Menu(self, tearoff=0)  # aka "help"

        self.add_cascade(label='Login', menu=menu1)
        self.add_cascade(label='Help', menu=menu2)

        menu1.add_command(label="Authorised User 1", command=self.parent.student_login)
        menu1.add_command(label='Authorized User 2', command=self.parent.instructor_login)



# mainloop for program execution
if __name__ == '__main__':
   app = App('First Start', (420,200))
   app.mainloop()

