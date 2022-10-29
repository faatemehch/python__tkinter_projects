import tkinter.messagebox
from PIL import ImageTk
from tkinter import *
from PIL import Image
import sqlite3

# ================== SETTINGS =====================
root = Tk()
root.geometry( '800x700' )
root.title( 'Contact List' )
root.configure( 'color' )
root.resizable( width=False, height=False )
# ================= FRAMES =========================
# Frame 1
frame_1 = Frame( root, width=700, height=70 )
frame_1.pack( side=TOP )
# Frame 2
frame_2 = Frame( root, width=700, height=70 )
frame_2.pack( side=TOP )
# Frame 3
frame_3 = Frame( root, width=700, height=70 )
frame_3.pack( side=TOP )
# Frame 4
frame_4 = Frame( root, width=700, height=70 )
frame_4.pack( side=TOP )
# ================ Variables ======================
canvas = Canvas( frame_2, height=250 )
canvas.pack()
img = ImageTk.PhotoImage( Image.open( "ContactListTkinter/photo" ).resize( (150, 150), Image.ANTIALIAS ) )
canvas.create_image( 150, 90, anchor=CENTER, image=img )
entry_name = StringVar()
entry_number = StringVar()

# =============== Labels & Listbox =============
# label
lbl_title = Label( frame_1, text='Contact List', font="Courier 40", fg="maroon3", bg='MediumPurple1' )
lbl_title.pack( side=TOP, ipadx=700, ipady=20 )
# list box for search result
results = Listbox( frame_4, bg='ivory2', fg='blue' )
results.pack()


# ================ Functions ======================
def get_contact(by='name'):
    '''
        find contact with name or number in user table
    '''
    try:
        if by == 'name':
            connection = sqlite3.connect( './contactList.sqlite' )
            cursor = connection.cursor()
            sql = """
                     SELECT * FROM USER WHERE name = ?
                """, (entry_name.get(),)
            cursor.execute( *sql )
            search_result_name = [user for user in cursor]
            connection.commit()
            connection.close()
            return search_result_name
        elif by == 'phoneNumber':
            connection = sqlite3.connect( './contactList.sqlite' )
            cursor = connection.cursor()
            sql = """
                             SELECT * FROM USER WHERE phoneNumber = ?
                        """, (entry_number.get(),)
            cursor.execute( *sql )
            search_result_number = [user for user in cursor]
            connection.commit()
            connection.close()
            return search_result_number
    except:
        # creat user table if does not exist
        connection = sqlite3.connect( './contactList.sqlite' )
        cursor = connection.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS USER(
        name VARCHAR (30),
        phoneNumber varchar (20)
        );

        """
        cursor.execute( sql )
        connection.commit()
        connection.close()
        return []


def add_contact():
    results.delete( 0, END )
    '''
        to add new contact in list of contacts:
        check if there exist that new one show message, 
        else add new one  
    '''
    if entry_name.get() == '' or entry_number.get() == '':
        tkinter.messagebox.showerror( 'Error', 'لطفا نام و شماره مخاطب جدید را وارد کنید' )
    else:
        notExist_name = False
        notExist_number = False
        # check the name is exist or not
        result_name = get_contact( 'name' )
        # check the number is exist or not
        result_number = get_contact( 'phoneNumber' )

        if len( result_name ) == 0 and len( result_number ) == 0:
            notExist_name = True
            notExist_number = True
        elif len( result_name ) > 0 and len( result_number ) > 0:
            tkinter.messagebox.showwarning( 'Error', 'مخاطبی با این نام و شماره وجود دارد' )
        elif len( result_name ) > 0:
            tkinter.messagebox.showwarning( 'Error', 'مخاطبی با این  نام وجود دارد' )
        elif len( result_number ) > 0:
            tkinter.messagebox.showwarning( 'Error', 'مخاطبی با این  شماره وجود دارد' )

        if notExist_name and notExist_number:
            connection = sqlite3.connect( './contactList.sqlite' )
            cursor = connection.cursor()
            sql = """
                      INSERT INTO USER ( name , phoneNumber) VALUES (?, ?) 
                      """, (entry_name.get(), entry_number.get())
            cursor.execute( *sql )
            connection.commit()
            connection.close()
            results.insert( 'end', 'new contact added...' )
            results.insert( 'end', f'{entry_name.get()}: {entry_number.get()}' )
            entry_name.set( '' )
            entry_number.set( '' )
            tkinter.messagebox.showinfo( 'Success', 'مخاطب جدید اضافه شد' )


def search_contact():
    results.delete( 0, END )
    '''
        search single contact in list contact,
    '''
    result = get_contact( by='name' )
    if len( result ) > 0:
        results.delete( 0, END )
        results.insert( 'end', 'List of searched contact...' )
        for i in result:
            results.insert( 'end', f'{i[0]} : {i[1]}' )
    else:
        tkinter.messagebox.showinfo( 'Info', 'مخاطبی با نام مورد نظر یافت نشد.' )
    entry_number.set( '' )
    entry_name.set( '' )


def delete_contact():
    results.delete( 0, END )
    '''
        delete single contact in list of contacts,
        first: check if the entered contact is exist or not,
        second: if exist delete the contact else show message
    '''
    if entry_name.get() == '':
        tkinter.messagebox.showinfo( 'Info', 'لطفا نام مخاطب مورد نظر را جهت حذف وارد نمایید.' )
    else:
        result = get_contact( 'name' )
        if len( result ) > 0:
            connection = sqlite3.connect( './contactList.sqlite' )
            cursor = connection.cursor()
            sql = """
                    DELETE FROM USER WHERE name = ?
                  
                    """, (entry_name.get(),)
            cursor.execute( *sql )
            connection.commit()
            connection.close()
            results.insert( END, 'Contact Deleted From List...' )
            for i in result:
                results.insert( END, f'{i[0]} : {i[1]}' )
        else:
            tkinter.messagebox.showinfo( 'Info', 'مخاطبی با نام مورد نظر یافت نشد.' )
        entry_number.set( '' )
        entry_name.set( '' )


def update_contact():
    results.delete( 0, END )
    '''
        update a contact name and it's phoneNumber
    '''
    if entry_name.get() != '':
        result = get_contact( 'name' )
        if len( result ) > 0:
            if entry_number.get() == '':
                tkinter.messagebox.showwarning( 'Warning', 'لطفا شماره جدید مخاطب را وارد کنید.' )
            else:
                connection = sqlite3.connect( './contactList.sqlite' )
                cursor = connection.cursor()
                sql = """
                                   UPDATE USER SET phoneNumber=? WHERE name = ?
    
                                   """, (entry_number.get(), entry_name.get(),)
                cursor.execute( *sql )
                connection.commit()
                connection.close()
                results.insert( END, 'Contact Updated...' )
                results.insert( END, f'{entry_name.get()} : {entry_number.get()}' )
                entry_name.set( '' )
                entry_number.set( '' )
        else:
            tkinter.messagebox.showerror( 'Error', 'مخاطبی با نام وارد شده وجود ندارد' )
    else:
        tkinter.messagebox.showerror( 'Error', 'لطفا نام مخاطب را جهت تغییر شماره وارد کنید.' )


# ================ buttons ======================
# btn 1 ----> to add new contact
add_btn = Button( frame_3, text='add contact', fg='black', highlightbackground='DeepPink3',
                  command=lambda: add_contact() )
add_btn.pack( side=LEFT, padx=10, pady=15 )
# btn 2 ----> to search a contact by it's name
search_btn = Button( frame_3, text='search contact', fg='black', highlightbackground='DeepPink3',
                     command=lambda: search_contact() )
search_btn.pack( side=LEFT, padx=70, pady=15 )
# btn 3 ---> to delete a contact by it's name
del_btn = Button( frame_3, text='delete contact', fg='black', highlightbackground='DeepPink3',
                  command=lambda: delete_contact() )
del_btn.pack( side=LEFT, padx=50, pady=15 )
# btn 4 ---> to update number of a contact
update_btn = Button( frame_3, text='update contact', fg='black', highlightbackground='DeepPink3',
                     command=lambda: update_contact() )
update_btn.pack( side=LEFT, padx=10, pady=15 )
# ==================== Entry and Label =====================
# contact number
label_get_num = Label( frame_2, text='Contact Name :', fg='maroon1' )
label_get_num.pack( side=LEFT, padx=10, pady=20 )
ent = Entry( frame_2, highlightbackground='tomato', textvariable=entry_name, bg='linen' )
ent.pack( side=LEFT, padx=10, pady=10 )
# contact name
label_get_num = Label( frame_2, text='Contact Number :', fg='maroon1' )
label_get_num.pack( side=LEFT, padx=10, pady=20 )
ent = Entry( frame_2, highlightbackground='tomato', textvariable=entry_number, bg='linen' )
ent.pack( side=RIGHT, padx=10, pady=10 )
# main loop
root.mainloop()
