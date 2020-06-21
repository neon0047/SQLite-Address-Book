from tkinter import *
from PIL import ImageTk,Image
import sqlite3

root = Tk(className = 'Address Book')
root.iconbitmap('image/icon.ico')

#Create a database or connecte to existing one
conn = sqlite3.connect('address_book.db')


#create cursor
c = conn.cursor()

#creat table
''''
c.execute(
    """CREATE TABLE people(
    First_name text,
    Last_name, text,
    address text,
    city text, 
    zipcode integer
       )""")
'''

#create submit function
def submit():

    #connect to database
    conn = sqlite3.connect('address_book.db')
    #create cursor
    c = conn.cursor()
    c.execute("INSERT INTO people VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
        {
            'f_name' : f_name.get(),
            'l_name' : l_name.get(),
            'address': address.get(),
            'city'   : city.get(),
            'state'  : state.get(),
            'zipcode': zipcode.get()})

    #Commit changes
    conn.commit()

    #close connection
    conn.close()



    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state .delete(0, END)
    zipcode.delete(0, END)

def query():
    #create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    #Create cursor
    c = conn.cursor()
    #query the database
    print_records = ''
    c.execute("SELECT *, oid FROM people")
    records = c.fetchall()

    for record in records:
        print_records += str(record) + "\n"

    query_label = Label(root, text = print_records )
    query_label.grid(row= 8, column = 0, columnspan = 2)    

    #commit changes
    conn.commit()

    #close connection
    conn.close()
    


f_name = Entry(root,width = 30)
f_name.grid(row=0 , column=1, padx = 20 )

l_name = Entry(root,width = 30)
l_name.grid(row=1 , column=1, padx = 20 )

address = Entry(root,width = 30)
address.grid(row=2 , column=1, padx = 20 )

city = Entry(root,width = 30)
city.grid(row=3 , column=1, padx = 20 )

state = Entry(root,width = 30)
state.grid(row=4 , column=1, padx = 20 )

zipcode = Entry(root,width = 30)
zipcode.grid(row=5 , column=1, padx = 20 )


#create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row = 0 , column = 0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row = 1 , column = 0)

address_label = Label(root, text="Address")
address_label.grid(row = 2 , column = 0)

city_label = Label(root, text="City")
city_label.grid(row = 3 , column = 0)

state_label = Label(root, text="State")
state_label.grid(row = 4 , column = 0)

zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row = 5 , column = 0)

#create submut button
submit_btn = Button(root, text = 'Add Record to Database', command = submit)
submit_btn.grid(row= 6, column= 0, columnspan= 2, padx = 10 , pady = 10, ipadx = 100)

query_btn = Button(root, text = 'Show Records', command = query)
query_btn.grid(row= 7, column= 0, columnspan= 2, padx = 10 , pady = 10, ipadx = 128)

#Commit changes
conn.commit()


#commit changes
conn.close()

root.mainloop()


