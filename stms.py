from tkinter import *
import time

import pandas
import ttkthemes
from tkinter import ttk  #to use themes we have to import ttk
import pymysql
from tkinter import messagebox, filedialog



#Function part

mycursor = None
cnt = None

def clock():
    global date, presenttime
    date = time.strftime('%d/%m/%Y')
    presenttime = time.strftime('%H:%M:%S')
    datetimelabel.config(text = f'   Date:{date}\nTime:{presenttime}', font=('arial'), fg = 'orangered3')
    datetimelabel.after(1000, clock) #1000ms = 1sec

count = 0
text = ''
def slider():
    global text, count
    if count == len(s):
        return
           #count = 0
           #text = ''

    text += s[count]
    sliderlabel.config(text = text)
    count+=1
    sliderlabel.after(130, slider)
def connectdatabase():

    def connect():
        global mycursor, cnt
        try:
            cnt = pymysql.connect(host = hostentry.get(), user = usernameentry.get(),password = passwordentry.get()) # here connect is a inbuilt method
            mycursor = cnt.cursor() # helps in executing commands

        except:
            messagebox.showerror('Error', 'Please enter valid credentials', parent = connectwindow)
            return
        try:
            query = 'create database studentmanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query = ('create table student(id int not null primary key, name varchar(30), mobile varchar(10), email '
                     'varchar(30), address varchar(100), gender varchar(10), dob varchar(20), date varchar(20), '
                     'time varchar(20))')
            mycursor.execute(query)
        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Successfull', ' Connected Successfully', parent=connectwindow)
        # messagebow will appear on the connectwindow since parent is connectwindow
        connectwindow.destroy()
        addstubt.config(state=NORMAL)
        searchstubt.config(state=NORMAL)
        updatestubt.config(state=NORMAL)
        deletestubt.config(state=NORMAL)
        exptdtbut.config(state=NORMAL)
        showstubt.config(state=NORMAL)

    connectwindow = Toplevel()
    connectwindow.grab_set() # so that the window remains there even if we click anywhere
    connectwindow.geometry('470x250+730+230')
    connectwindow.title('Student Database')
    connectwindow.resizable(0,0)

    hostnamelabel = Label(connectwindow, text = 'Host Name', font = ('arial', 15))
    hostnamelabel.grid(row = 0, column = 0, padx = 15)
    hostentry = Entry(connectwindow, font = ('times new roman', 15), bd = 2)
    hostentry.grid(row = 0, column = 1, pady = 15)

    usernamelabel = Label(connectwindow, text = 'Username', font = ('arial', 15))
    usernamelabel.grid(row = 1, column = 0, padx = 15)
    usernameentry = Entry(connectwindow, font = ('times new roman', 15), bd = 2)
    usernameentry.grid(row = 1, column = 1, pady = 15)

    passwordlabel = Label(connectwindow, text = 'Password', font = ('arial', 15))
    passwordlabel.grid(row = 2, column = 0, padx = 15)
    passwordentry = Entry(connectwindow, font = ('times new roman', 15), bd = 2, show='*')
    passwordentry.grid(row = 2, column = 1, pady = 15)



    connectbt = ttk.Button(connectwindow, text = 'Connect', cursor='hand2', command=connect)
    connectbt.grid(row = 3, column = 1)

def field_data(title, button_text, command):

    global identry, nameentry, mobileentry, emailentry, addressentry, genderentry, dobentry, screen

    screen = Toplevel()
    screen.geometry('470x500+530+230')
    screen.resizable(False, False)
    screen.grab_set()
    screen.title(title)

    idlabel = Label(screen, text='Id', font=('times new roman', 17, 'bold'))
    idlabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)  # stick to west
    identry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    identry.grid(row=0, column=1, pady=15, padx=10)

    namelabel = Label(screen, text='Name', font=('times new roman', 17, 'bold'))
    namelabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameentry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    nameentry.grid(row=1, column=1, pady=15, padx=10)

    mobilelabel = Label(screen, text='Mobile', font=('times new roman', 17, 'bold'))
    mobilelabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    mobileentry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    mobileentry.grid(row=2, column=1, pady=15, padx=10)

    emaillabel = Label(screen, text='Email', font=('times new roman', 17, 'bold'))
    emaillabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    emailentry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    emailentry.grid(row=3, column=1, pady=15, padx=10)

    addresslabel = Label(screen, text='Address', font=('times new roman', 17, 'bold'))
    addresslabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    addressentry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    addressentry.grid(row=4, column=1, pady=15, padx=10)

    genderlabel = Label(screen, text='Gender', font=('times new roman', 17, 'bold'))
    genderlabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    genderentry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    genderentry.grid(row=5, column=1, pady=15, padx=10)

    doblabel = Label(screen, text='D.O.B', font=('times new roman', 17, 'bold'))
    doblabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    dobentry = ttk.Entry(screen, font=('times new roman', 15), width=24)
    dobentry.grid(row=6, column=1, pady=15, padx=10)

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()  # moves focus to next widget
        return "break"  # prevent default behavior

    identry.bind("<Return>", focus_next_widget)
    identry.bind("<Down>", focus_next_widget)

    nameentry.bind("<Return>", focus_next_widget)
    nameentry.bind("<Down>", focus_next_widget)

    mobileentry.bind("<Return>", focus_next_widget)
    mobileentry.bind("<Down>", focus_next_widget)

    emailentry.bind("<Return>", focus_next_widget)
    emailentry.bind("<Down>", focus_next_widget)

    addressentry.bind("<Return>", focus_next_widget)
    addressentry.bind("<Down>", focus_next_widget)

    genderentry.bind("<Return>", focus_next_widget)
    genderentry.bind("<Down>", focus_next_widget)

    dobentry.bind("<Return>", focus_next_widget)
    dobentry.bind("<Down>", focus_next_widget)

    bt = ttk.Button(screen, text=button_text, command=command)
    bt.grid(row=7, column=1)

    if title == 'Update Student':

        indexing = stutable.focus()
        content = stutable.item(indexing)
        listdata = content['values']

        identry.insert(0, listdata[0])
        nameentry.insert(0, listdata[1])
        mobileentry.insert(0, listdata[2])
        emailentry.insert(0, listdata[3])
        addressentry.insert(0, listdata[4])
        genderentry.insert(0, listdata[5])
        dobentry.insert(0, listdata[6])


def add_data():
    global mycursor, cnt
    if (identry.get() == '' or nameentry.get() == '' or mobileentry.get() == '' or
            emailentry.get() == '' or addressentry.get() == '' or genderentry.get() == '' or
            dobentry.get() == ''):
        messagebox.showerror('Error', 'All fields are required')
        return
    else:
        try:

            query = ('INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)')
            mycursor.execute(query, (
                identry.get(),
                nameentry.get(),
                mobileentry.get(),
                emailentry.get(),
                addressentry.get(),
                genderentry.get(),
                dobentry.get(),
                date,
                presenttime
            ))
            cnt.commit()

            result = messagebox.askyesno('Data added successfully', 'Do you want to add another Student?', parent = screen)
            if result:
                identry.delete(0, END)
                nameentry.delete(0, END)
                mobileentry.delete(0, END)
                emailentry.delete(0, END)
                addressentry.delete(0, END)
                genderentry.delete(0, END)
                dobentry.delete(0, END)
            else:
                screen.destroy()
            query = 'select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            stutable.delete(*stutable.get_children())
            for data in fetched_data:
                stutable.insert('', END, values = data)
        except:
            messagebox.showerror('Error', 'Id should not be repeated', parent = screen)
            return


def search_data():
    query = 'select * from student where id = %s or name = %s or email = %s or mobile = %s or address = %s or gender = %s or dob = %s'
    mycursor.execute(query, (identry.get(), nameentry.get(), emailentry.get(), mobileentry.get(), addressentry.get(), genderentry.get(), dobentry.get()))
    stutable.delete(*stutable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        stutable.insert('', END, values=data)
    screen.destroy()


def delete_student():
    indexing = stutable.focus() # this will get the selected row index
    content = stutable.item(indexing)
    content_id = content['values'][0]

    res = messagebox.askyesno('Confirmation', f'Do you want to delete id:{content_id}?')
    if res:
        query = 'delete from student where id = %s'
        mycursor.execute(query, content_id)


    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    stutable.delete(*stutable.get_children())
    for data in fetched_data:
        stutable.insert('', END, values = data)
    messagebox.showinfo('Success', f'student having id:{content_id} has successfully deleted.')
    cnt.commit()

def show_students():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    stutable.delete(*stutable.get_children())
    for data in fetched_data:
        stutable.insert('', END, values=data)


def update_data():
    query = '''UPDATE student 
               SET name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s 
               WHERE id=%s'''
    mycursor.execute(query, (
        nameentry.get(),
        mobileentry.get(),
        emailentry.get(),
        addressentry.get(),
        genderentry.get(),
        dobentry.get(),
        date,
        presenttime,
        identry.get()
    ))

    cnt.commit()
    messagebox.showinfo('Success', f'Successfully updated student having id:{identry.get()}', parent = screen)
    screen.destroy()
    show_students()

def export_data():
    path = filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = stutable.get_children()
    newlist = []
    for index in indexing:
        content = stutable.item(index)
        datalist = content['values']
        newlist.append(datalist)

    table = pandas.DataFrame(newlist, columns = ['Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B', 'Added Date', 'Added Time'])
    table.to_csv(path, index = False)
    messagebox.showinfo('Success', 'Data is imported successfully!')


def isexit():
    res = messagebox.askyesno('Confirmation', 'Do you want to exit?')
    if res: window.destroy()

#-----------------------Main Window--------------------------------------------
window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('radiance')
window.title('Student Management System')
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

datetimelabel = Label(window, text = 'hello', font = ('times new roman',15,'bold'))
datetimelabel.place(x = 5, y = 20)
clock()

s = 'Student Management System'
sliderlabel = Label(window, font = ('arial',35,'bold'), fg = 'midnight blue', width = 30)
sliderlabel.place(x = 270, y = 10 )
slider()

#-------------------------Connect database button---------------------------------
cntdb = ttk.Button(window, text = 'Connect Database', cursor='hand2', command=connectdatabase)
cntdb.place(x = 1200, y = 25)

#----------------------left frame-----------------------------
leftframe = Frame(window)
leftframe.place(x = 55, y = 150, width = 300, height = 700)

#-------------image logo
imagelogo = PhotoImage(file='student1.png')
logolabel = Label(leftframe, image = imagelogo)
logolabel.grid(row = 0, column = 0, pady = 25)

#------------student buttons
addstubt = ttk.Button(leftframe, text = 'Add Student', width = 15, state=DISABLED, command=lambda: field_data('Add Student', 'Add', add_data)) # lambda is used because whenever we click on add then only the fuction is executed
addstubt.grid(row = 1, column = 0, pady = 5)

searchstubt = ttk.Button(leftframe, text = 'Search Student', width = 15, state=DISABLED, command=lambda: field_data('Search Student', 'Search', search_data))
searchstubt.grid(row = 2, column = 0, pady = 10)

deletestubt = ttk.Button(leftframe, text = 'Delete Student', width = 15, state=DISABLED, command=delete_student)
deletestubt.grid(row = 3, column = 0, pady = 10)

updatestubt = ttk.Button(leftframe, text = 'Update Student', width=15, state=DISABLED, command = lambda: field_data('Update Student', 'Update', update_data))
updatestubt.grid(row = 4, column = 0, pady = 10)

showstubt = ttk.Button(leftframe, text = 'Show Data', width=15, state=DISABLED, command = show_students)
showstubt.grid(row = 5, column = 0, pady = 10)

exptdtbut = ttk.Button(leftframe, text = 'Export Data', width=15, state=DISABLED, command = export_data)
exptdtbut.grid(row = 6, column = 0, pady = 10)

exitbt = ttk.Button(leftframe, text = 'Exit', width=15, command = isexit)
exitbt.grid(row = 7, column = 0, pady = 10)

#-----------------------right frame---------------------------

rightframe = Frame(window)
rightframe.place(x = 500, y = 150, width = 800, height = 500)

#--------------------scrollbars

scrollbarx = Scrollbar(rightframe, orient=HORIZONTAL)
scrollbary = Scrollbar(rightframe, orient=VERTICAL)
scrollbarx.pack(side = BOTTOM, fill = X)
scrollbary.pack(side = RIGHT, fill = Y)

#-----------------------student table

stutable = ttk.Treeview(rightframe, columns=('Id', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'D.O.B',
                                             'Added Date', 'Added Time'), xscrollcommand=scrollbarx.set,
                        yscrollcommand=scrollbary.set) # treeview is used to display the data or table
scrollbarx.config(command=stutable.xview)
scrollbary.config(command=stutable.yview)

stutable.heading('Id', text = 'Id')
stutable.heading('Name', text = 'Name')
stutable.heading('Mobile No', text = 'Mobile')
stutable.heading('Email', text = 'Email')
stutable.heading('Address', text = 'Address')
stutable.heading('Gender', text = 'Gender')
stutable.heading('D.O.B', text = 'D.O.B')
stutable.heading('Added Date', text = 'Added Date')
stutable.heading('Added Time', text = 'Added Time')
stutable.config(show='headings') # to avoid unnecessary columns

stutable.pack(fill = BOTH, expand = 1)

stutable.column('Id', width = 50, anchor=CENTER)
stutable.column('Name', width = 250, anchor=CENTER)
stutable.column('Email', width = 300, anchor=CENTER)
stutable.column('Mobile No', width = 180, anchor=CENTER)
stutable.column('Address', width = 400, anchor=CENTER)
stutable.column('Gender', width = 80, anchor=CENTER)
stutable.column('D.O.B', width = 100, anchor=CENTER)
stutable.column('Added Date', width = 150, anchor=CENTER)
stutable.column('Added Time', width = 150, anchor=CENTER)

style = ttk.Style()
style.configure('Treeview',rowheight = 30, font = ('arial', 11))
style.configure('Treeview.Heading', font = ('arial', 13))


window.mainloop()