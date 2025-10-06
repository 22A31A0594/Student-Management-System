from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'Fields cannot be empty')
    elif usernameEntry.get() == 'Sri Harsha' and passwordEntry.get() == '1234':
        messagebox.showinfo('', 'login Successfull')
        window.destroy()
        import stms  # here we are calling or opening another window that is student management system window
    else:
        messagebox.showerror('Error', 'Please enter valid credentials')

window = Tk()
window.title('Admin Login Page of Student Management System')

# Set window size
win_width = 1400
win_height = 850

# Get screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Calculate position x and y to center the window
x = (screen_width // 2) - (win_width // 2)
y = (screen_height // 2) - (win_height // 2)

# Set geometry with position
window.geometry(f'{win_width}x{win_height}+{x}+{y}')
window.resizable(False, False)
# Load and resize image
image = Image.open("bg.jpg")
image = image.resize((win_width, win_height), Image.LANCZOS)
bgimage = ImageTk.PhotoImage(image)

# Set background
bglabel = Label(window, image=bgimage)
bglabel.place(x=0, y=0)

'''----------------------login frame-------------------------'''

loginframe = Frame(window)
loginframe.place(x=540, y=200)

'''-------------------logo------------------------'''

logo = PhotoImage(file = 'graduation_logo.png')
logolabel = Label(loginframe, image = logo)
logolabel.grid(row=0, column=0, columnspan=2, pady = 10)

'''---------------------------------Username Entry-------------------------------'''

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginframe, image = usernameImage, text='Username', compound=LEFT,
                      font=('times new roman', 15, "bold")) #compound=left means usernameimage will come on left side
usernameLabel.grid(row=1, column=0, padx = 10, pady = 10)
usernameEntry = Entry(loginframe, font=('times new roman', 13), bd=4)
usernameEntry.grid(row=1, column=1, padx = 10, pady = 10)

'''------------------------Password Entry----------------------------------'''

passwordImage = PhotoImage(file='padlock.png')
passwordLabel = Label(loginframe, image = passwordImage, text='Password', compound=LEFT,
                      font=('times new roman', 15, "bold"))
passwordLabel.grid(row=2, column=0, padx = 10, pady = 10)
passwordEntry = Entry(loginframe, font=('times new roman', 13), bd=4, show = '*')
passwordEntry.grid(row=2, column=1, padx = 10)

'''----------------------------login Button-------------------------------'''

loginbt = Button(loginframe, text='Login', font=('times new roman', 13, 'bold'), bd = 3, width=8, fg = 'white'
                 , bg = 'sienna1', activebackground='sienna1', cursor = 'hand2', command=login)
#fg is used to change the text colour and cursor is used when we put cursor on button it will show hand symbol
loginbt.grid(row=3, column = 0, columnspan = 2, pady = 10)

window.mainloop()
