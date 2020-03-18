# ----- Third Party Imports
# Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

# SQL
import mysql.connector

# Images
import PIL
from PIL import Image, ImageTk
# from resizeimage import resizeimage

# ?
import io
# Imports for PDF writing
# Report Lab
import reportlab
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
import reportlab.rl_config
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
reportlab.rl_config.warnOnMissingFontGlyphs = 0

# PYPDF2
import PyPDF2 as p2
# import glob
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

import csv
from datetime import date
today = date.today()
date1 = today.strftime("%Y-%m-%d")
import ctypes
import os
# Beautiful Soup, web scraping
import bs4
from urllib.request import urlopen as uReq

# ----- Own Imports
from modules import (
Mbox,
crm_lbl,
crm_opt_menu,
crm_btn,
crm_entry,
submit,
button_ttk_nav,
button_ttk_reg,
clear_forms,
draw_pdf, 
openfile,
label_config,
)

####
# --- Create Database
# my_cursor.execute("CREATE DATABASE mcvcontacts")
# # --- Create Table
# my_cursor.execute("CREATE TABLE allcontacts (firstname1 VARCHAR(255) DEFAULT NULL, lastname1 VARCHAR(255) DEFAULT NULL, firstname2 VARCHAR(255) DEFAULT NULL, lastname2 VARCHAR(255) DEFAULT NULL, email1 VARCHAR(255) DEFAULT NULL, phone1 VARCHAR(20) DEFAULT NULL, email2 VARCHAR(255) DEFAULT NULL, phone2 VARCHAR(20) DEFAULT NULL, addressline1 VARCHAR(255) DEFAULT NULL, addressline2 VARCHAR(255) DEFAULT NULL, neighbourhood VARCHAR(255) DEFAULT NULL, city VARCHAR(255) DEFAULT NULL, province VARCHAR(255) DEFAULT NULL, postalcode VARCHAR(10) DEFAULT NULL, company VARCHAR(255) DEFAULT NULL, listprezday DATE DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# # --- Create Table
# my_cursor.execute("CREATE TABLE calanderlist (firstname1 VARCHAR(255) DEFAULT NULL, lastname1 VARCHAR(255) DEFAULT NULL, firstname2 VARCHAR(255) DEFAULT NULL, lastname2 VARCHAR(255) DEFAULT NULL, email1 VARCHAR(255) DEFAULT NULL, phone1 VARCHAR(20) DEFAULT NULL, email2 VARCHAR(255) DEFAULT NULL, phone2 VARCHAR(20) DEFAULT NULL, addressline1 VARCHAR(255) DEFAULT NULL, addressline2 VARCHAR(255) DEFAULT NULL, neighbourhood VARCHAR(255) DEFAULT NULL, city VARCHAR(255) DEFAULT NULL, province VARCHAR(255) DEFAULT NULL, postalcode VARCHAR(10) DEFAULT NULL, company VARCHAR(255) DEFAULT NULL, listprezday DATE DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# # --- Create Table
# my_cursor.execute("CREATE TABLE closings (firstname1 VARCHAR(255) DEFAULT NULL, lastname1 VARCHAR(255) DEFAULT NULL, firstname2 VARCHAR(255) DEFAULT NULL, lastname2 VARCHAR(255) DEFAULT NULL, email1 VARCHAR(255) DEFAULT NULL, phone1 VARCHAR(20) DEFAULT NULL, email2 VARCHAR(255) DEFAULT NULL, phone2 VARCHAR(20) DEFAULT NULL, addressline1 VARCHAR(255) DEFAULT NULL, addressline2 VARCHAR(255) DEFAULT NULL, neighbourhood VARCHAR(255) DEFAULT NULL, city VARCHAR(255) DEFAULT NULL, province VARCHAR(255) DEFAULT NULL, postalcode VARCHAR(10) DEFAULT NULL, company VARCHAR(255) DEFAULT NULL, listprezday DATE DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# #--- Create Table
# my_cursor.execute("CREATE TABLE listingprez (firstname1 VARCHAR(255) DEFAULT NULL, lastname1 VARCHAR(255) DEFAULT NULL, firstname2 VARCHAR(255) DEFAULT NULL, lastname2 VARCHAR(255) DEFAULT NULL, email1 VARCHAR(255) DEFAULT NULL, phone1 VARCHAR(20) DEFAULT NULL, email2 VARCHAR(255) DEFAULT NULL, phone2 VARCHAR(20) DEFAULT NULL, addressline1 VARCHAR(255) DEFAULT NULL, addressline2 VARCHAR(255) DEFAULT NULL, neighbourhood VARCHAR(255) DEFAULT NULL, city VARCHAR(255) DEFAULT NULL, province VARCHAR(255) DEFAULT NULL, postalcode VARCHAR(10) DEFAULT NULL, company VARCHAR(255) DEFAULT NULL, listprezday DATE DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# # --- Create Table
# my_cursor.execute("CREATE TABLE transactions (clientname VARCHAR(255) DEFAULT NULL, address VARCHAR(255) DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# # --- Create Table
# my_cursor.execute("CREATE TABLE agents (name VARCHAR(255), phone VARCHAR(255), email VARCHAR(255), agentcode VARCHAR(255), office VARCHAR(255)")
# Alter Table
# my_cursor.execute("ALTER TABLE closings ADD user_id INTEGER AUTO_INCREMENT PRIMARY Key AFTER listprezday;")
# my_cursor.execute("ALTER TABLE closings ADD pay INTEGER AFTER commission;")

# SQL connect and close
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
# my_cursor = mydb.cursor() 
# my_cursor.execute("CREATE TABLE calanderlist (firstname1 VARCHAR(255) DEFAULT NULL, lastname1 VARCHAR(255) DEFAULT NULL, firstname2 VARCHAR(255) DEFAULT NULL, lastname2 VARCHAR(255) DEFAULT NULL, email1 VARCHAR(255) DEFAULT NULL, phone1 VARCHAR(20) DEFAULT NULL, email2 VARCHAR(255) DEFAULT NULL, phone2 VARCHAR(20) DEFAULT NULL, addressline1 VARCHAR(255) DEFAULT NULL, addressline2 VARCHAR(255) DEFAULT NULL, neighbourhood VARCHAR(255) DEFAULT NULL, city VARCHAR(255) DEFAULT NULL, province VARCHAR(255) DEFAULT NULL, postalcode VARCHAR(10) DEFAULT NULL, company VARCHAR(255) DEFAULT NULL, listprezday DATE DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# my_cursor.execute("CREATE TABLE transactions (clientname VARCHAR(255) DEFAULT NULL, address VARCHAR(255) DEFAULT NULL, closedate DATE DEFAULT NULL, saleprice INTEGER(10) DEFAULT NULL, commission FLOAT(10) DEFAULT NULL, pay FLOAT(10) DEFAULT NULL, user_id INTEGER AUTO_INCREMENT PRIMARY Key)")
# mydb.commit()
# my_cursor.close()
# mydb.close()  

# Font Options
LARGE_FONT = ("Helvetica", 12)
MED_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)

class crmapp(tk.Tk):
        def __init__(self, *args, **kwargs):
                tk.Tk.__init__(self, *args, **kwargs)

                tk.Tk.iconbitmap(self, default="images/alienicon.ico")
                tk.Tk.wm_title(self, "McV CRM")

                container = tk.Frame(self)
                container.pack(side="top", fill="both", expand=True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)

                self.frames = {}

                for F in (addcontactform, PrezPage, ClosingsPage):

                        frame = F(container, self)

                        self.frames[F] = frame

                        frame.grid(row=0, column=0, sticky="nsew")

                self.show_frame(addcontactform)

        # Change Pages
        def show_frame(self, cont):
                frame = self.frames[cont]
                frame.tkraise()


class addcontactform(tk.Frame):
        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                canvas = tk.Canvas(self, height=976, width=1600, background = 'black')
                canvas.pack()
                
                #user id tracker for deleting old contact that has been edited
                self.useridedit = 0
                # data base list selection from drop down menu to track which data to re-populate tree with
                editfrmhere = tk.StringVar()
            
                # Navigation Buttons
                # Contacts
                button_ttk_nav(self, ttk, 'Contacts', controller, addcontactform, .02, .03, .1, .04)
                # Listing Prez
                button_ttk_nav(self, ttk, 'Listing Prez', controller, PrezPage, .12, .03, .1, .04)
                 # Closings
                button_ttk_nav(self, ttk, 'Closings', controller, ClosingsPage, .22, .03, .1, .04)

                # --- Add & Remove Buttons
                # Add new contact label
                crm_lbl(self, tk, "  Add New Contact", "groove", "w", "white", 'black','.02', '.14', '.35', '.04')
                # First Name 1 Label
                crm_lbl(self, tk, "  First Name 1:", "groove", 'w', 'white', 'black', '.02', '.18', '.175', '.03' )
                # First Name 1 Entry
                firstname1entry = tk.Entry(self, bg="white")
                firstname1entry.place(relx=.02, rely=.21, relwidth=.175, relheight=.03)
                # Last Name 1 Label
                crm_lbl(self, tk, "  Last Name 1:", 'groove', 'w', 'white', 'black', '.195', '.18', '.175', '.03')
                # Last Name 1 Entry
                lastname1entry = tk.Entry(self, bg="white")
                lastname1entry.place(relx=.195, rely=.21, relwidth=.175, relheight=.03)
                # First Name 2 Label
                crm_lbl(self, tk, "  First Name 2:", 'groove', 'w', 'white', 'black', '.02', '.24', '.175', '.03')
                # First Name 2 Entry
                firstname2entry = tk.Entry(self, bg="white")
                firstname2entry.place(relx=.02, rely=.27, relwidth=.175, relheight=.03)
                # Last Name 2 Label
                crm_lbl(self, tk, "  Last Name 2:", 'groove', 'w', 'white', 'black', '.195', '.24', '.175', '.03')
                # Last Name 2 Entry
                lastname2entry = tk.Entry(self, bg="white")
                lastname2entry.place(relx=.195, rely=.27, relwidth=.175, relheight=.03)
                # Email 1 Label
                crm_lbl(self, tk, "  Email One:", 'groove', 'w', 'white', 'black', '.02', '.30', '.25', '.03')
                # Email 1 Entry
                email1entry = tk.Entry(self, bg="white")
                email1entry.place(relx=.02, rely=.33, relwidth=.25, relheight=.03)
                # Phone 1 Label
                crm_lbl(self, tk, "  Phone One:", 'groove', 'w', 'white', 'black', '.27', '.30', '.10', '.03')
                # Phone 1 Entry
                phone1entry = tk.Entry(self, bg="white")
                phone1entry.place(relx=.27, rely=.33, relwidth=.10, relheight=.03) 
                # Email 2 Label
                crm_lbl(self, tk, "  Email Two:", 'groove', 'w', 'white', 'black', '.02', '.36', '.25', '.03')
                # Email 2 Entry
                email2entry = tk.Entry(self, bg="white")
                email2entry.place(relx=.02, rely=.39, relwidth=.25, relheight=.03)
                # Phone 2 Label
                crm_lbl(self, tk, "  Phone Two:", 'groove', 'w', 'white', 'black', '.27', '.36', '.10', '.03')
                # Phone 2 Entry
                phone2entry = tk.Entry(self, bg="white")
                phone2entry.place(relx=.27, rely=.39, relwidth=.10, relheight=.03)
                # Company Label
                crm_lbl(self, tk, "  Company:", 'groove', 'w', 'white', 'black', '.02', '.42', '.35', '.03')
                # Company Entry
                companyentry = tk.Entry(self, bg="white")
                companyentry.place(relx=.02, rely=.45, relwidth=.35, relheight=.03)
                # List Prez Day Label
                crm_lbl(self, tk, "  List Prez Day: YYYY-MM-DD", 'groove', 'w', 'white', 'black', '.02', '.48', '.175', '.03')
                # List Prez Day Entry
                listprezdayentry = tk.Entry(self, bg="white")
                listprezdayentry.place(relx=.02, rely=.51, relwidth=.175, relheight=.03)
                # Closing Date Label
                crm_lbl(self, tk, "  Closing Date: YYYY-MM-DD", 'groove', 'w', 'white', 'black', '.195', '.48', '.175', '.03')
                # Closing Date Entry
                closedayentry = tk.Entry(self, bg="white")
                closedayentry.place(relx=.195, rely=.51, relwidth=.175, relheight=.03)
                # Sale Price Label
                crm_lbl(self, tk, "  Sale Price:", 'groove', 'w', 'white', 'black', '.02', '.54', '.175', '.03')
                # Sale Price Entry
                salepriceentry = tk.Entry(self, bg="white")
                salepriceentry.insert(0, 0)
                salepriceentry.place(relx=.02, rely=.57, relwidth=.175, relheight=.03)

                # Commission Label
                crm_lbl(self, tk, "  Commission Amount:", 'groove', 'w', 'white', 'black', '.195', '.54', '.125', '.03')
                # Commission Entry
                commissionentry = tk.Entry(self, bg="white")
                commissionentry.insert(0, 0)
                commissionentry.place(relx=.195, rely=.57, relwidth=.125, relheight=.03)
                # Commission % or $ Label
                crm_lbl(self, tk, "   $ or %", 'groove', 'w', 'white', 'black', '.32', '.54', '.05', '.03')
                # Commission type dropdown menu
                comm_types = ["%", "$"]
                comm_type = tk.StringVar()
                crm_opt_menu(self, 'comm_type_menu', tk, comm_type, comm_types, '.32', '.57', '.05', '.03')
                # Address line 1 Label
                crm_lbl(self, tk, "  Address Line One:", 'groove', 'w', 'white', 'black', '.02', '.60', '.35', '.03') 
                # Address line 1 Entry
                address1entry = tk.Entry(self, bg="white")
                address1entry.place(relx=.02, rely=.63, relwidth=.35, relheight=.03)
                # Address line 2 Label
                crm_lbl(self, tk, "  Address Line Two:", 'groove', 'w', 'white', 'black', '.02', '.66', '.35', '.03')
                # Address line 2 Entry
                address2entry = tk.Entry(self, bg="white")
                address2entry.place(relx=.02, rely=.69, relwidth=.35, relheight=.03)
                # City Label
                crm_lbl(self, tk, "  City:", 'groove', 'w', 'white', 'black', '.02', '.72', '.175', '.03')
                # City Entry
                cityentry = tk.Entry(self, bg="white")
                cityentry.place(relx=.02, rely=.75, relwidth=.175, relheight=.03)
                # Neighbourhood Label
                crm_lbl(self, tk, "  Neighbourhood:", 'groove', 'w', 'white', 'black', '.195', '.72', '.175', '.03')
                # Neighbourhood Entry
                neighbentry = tk.Entry(self, bg="white")
                neighbentry.place(relx=.195, rely=.75, relwidth=.175, relheight=.03)
                # Province Label
                crm_lbl(self, tk, "  Province:", 'groove', 'w', 'white', 'black', '.02', '.78', '.175', '.03')
                # Province Entry
                proventry = tk.Entry(self, bg="white")
                proventry.place(relx=.02, rely=.81, relwidth=.175, relheight=.03)
                # Postal Code Label
                crm_lbl(self, tk, "  Postal Code:", 'groove', 'w', 'white', 'black', '.195', '.78', '.175', '.03')
                # Postal Code Entry
                postalcodeentry = tk.Entry(self, bg="white",)
                postalcodeentry.place(relx=.195, rely=.81, relwidth=.175, relheight=.03)
                
                # Pop-Up Box
                def Mbox(title, text, style):
                        return ctypes.windll.user32.MessageBoxW(0, text, title, style)

                # Clear Form 
                con_forms = (firstname1entry, lastname1entry, firstname2entry, lastname2entry, email1entry, email2entry, phone1entry, phone2entry, companyentry, listprezdayentry, 
                            address1entry, address2entry, cityentry ,neighbentry, proventry, postalcodeentry, closedayentry, salepriceentry, commissionentry)

                def clear_con_form():
                        clear_forms(self, con_forms)
                        self.useridedit = 0

                # Edit Contact
                def edit_con():
                        # Find New Values
                        edititem = edittree.selection() # Get Tree selection
                        dictedit = (edittree.item(edititem)) # Get all info from selected row
                        usereditinfo = (dictedit["values"]) # get column values
                        
                        # Declare New Values
                        firstname1edit = (usereditinfo[0])
                        lastname1edit = (usereditinfo[1])
                        firstname2edit = (usereditinfo[2])
                        lastname2edit = (usereditinfo[3])
                        email1edit = (usereditinfo[4])
                        phone1edit = (usereditinfo[5])
                        email2edit = (usereditinfo[6])
                        phone2edit = (usereditinfo[7])
                        address1edit = (usereditinfo[8])
                        address2edit = (usereditinfo[9])
                        neighbedit = (usereditinfo[10])
                        cityedit = (usereditinfo[11])
                        provedit = (usereditinfo[12])
                        postalcodeedit = (usereditinfo[13])
                        companyedit = (usereditinfo[14])
                        listprezdayedit = (usereditinfo[15])
                        closedayedit = (usereditinfo[16])
                        salepriceedit = (usereditinfo[17])
                        commissionedit = (usereditinfo[18])
                        self.useridedit =  (usereditinfo[20]) # Get User_id for use in deleting the chosen contact**
                        
                        # Insert New Values
                        firstname1entry.insert(0, firstname1edit)
                        lastname1entry.insert(0, lastname1edit)
                        firstname2entry.insert(0, firstname2edit)
                        lastname2entry.insert(0, lastname2edit)
                        email1entry.insert(0, email1edit)
                        email2entry.insert(0, email2edit)
                        phone1entry.insert(0, phone1edit)
                        phone2entry.insert(0, phone2edit)
                        companyentry.insert(0, companyedit)
                        listprezdayentry.insert(0, listprezdayedit)
                        address1entry.insert(0, address1edit)
                        address2entry.insert(0, address2edit)
                        neighbentry.insert(0, neighbedit)
                        cityentry.insert(0, cityedit)
                        proventry.insert(0, provedit)
                        postalcodeentry.insert(0, postalcodeedit)
                        closedayentry.insert(0, closedayedit)
                        salepriceentry.insert(0, salepriceedit)
                        commissionentry.insert(0, commissionedit)

                # Add Contact Button
                def add_con():
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()
                        # Gets
                        fn1get = firstname1entry.get()
                        ln1get = lastname1entry.get()
                        fn2get = firstname2entry.get()
                        ln2get = lastname2entry.get()
                        em1get = email1entry.get()
                        em2get = email2entry.get()
                        p1get = phone1entry.get()
                        p2get = phone2entry.get()
                        comget = companyentry.get()
                        pdayget = listprezdayentry.get()
                        if len(listprezdayentry.get()) == 0:
                            pdayget = "0000-00-00"
                        cdayentryget = closedayentry.get()
                        if len(closedayentry.get()) == 0:
                            cdayentryget = "0000-00-00"
                        a1get = address1entry.get()
                        a2get = address2entry.get()
                        cityget = cityentry.get()
                        neighbget = neighbentry.get()
                        provget = proventry.get()
                        pcget = postalcodeentry.get()
                        salepriceget = int(salepriceentry.get())
                        if salepriceget == '':
                            salepriceget = int(0)
                        commget = float(commissionentry.get())
                        if commget == '':
                            commget = float(0)
                        addcpay = float()
                        comchoice = comm_type.get()
                        if comchoice == "$":
                            addcpay = commget
                        else:
                            addcpay = (salepriceget * (commget / 100))

                        # Insert Contact into MySQL
                        add2choicedb2 = "INSERT INTO calanderlist (firstname1, lastname1, firstname2, lastname2, email1, phone1, email2, phone2, addressline1, addressline2, neighbourhood, city, province, postalcode, company, listprezday, closedate, saleprice, commission, pay) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                        newcontact2 = (fn1get, ln1get, fn2get, ln2get, em1get, p1get, em2get, p2get, a1get, a2get, neighbget, cityget, provget, pcget, comget, 
                                        pdayget, cdayentryget, salepriceget, commget, addcpay)
                        my_cursor.execute(add2choicedb2, newcontact2)

                        mydb.commit()
                        my_cursor.close()
                        mydb.close()
                        
                # Delete Selcted Contact from MySQL
                def delete_con():
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()
                        delfrmthis2 = "DELETE FROM calanderlist WHERE user_id = %s"
                        my_cursor.execute(delfrmthis2,(self.useridedit,))

                        mydb.commit()
                        my_cursor.close()
                        mydb.close()

                        # set, user id to be deleted, back to zero                       
                        self.useridedit = 0

                # ---- Buttons ----- #
                # Add Contact Button
                ttk_btn_style = ttk.Style()
                ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)
                ttk_button = ttk.Button(self, text= "Add to Database", style="Nav.TButton", command = lambda:[add_con(), delete_con(), clear_con_form()])
                ttk_button.place(relx=.02, rely=.87, relwidth=.35, relheight=.04)

                # Clear Form Button
                button_ttk_reg(self, ttk, "Clear Form", clear_con_form, .02, .84, .35, .03)

                # Edit Contact Button
                ttk_btn_style = ttk.Style()
                ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)
                ttk_button = ttk.Button(self, text= "Edit", style="Nav.TButton", command = lambda: [clear_con_form(), edit_con()])
                ttk_button.place(relx=.475, rely=.09, relwidth=.075, relheight=.03)

                # Delete Contact Button
                button_ttk_reg(self, ttk, "Delete", delete_con, .39, .09, .075, .03)

                # Export CSV Button
                def expconcsv():
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor() 
                        # Get Data from MySQL
                        my_cursor.execute("SELECT * FROM calanderlist")
                        allcons = my_cursor.fetchall()
                        # Open CSV and create it
                        newcsv = open('csvs/calanderlist.csv', 'w', newline='')
                        allconfile = csv.writer(newcsv)
                        allconfile.writerows(allcons)
                        newcsv.close()
                        my_cursor.close()
                        mydb.close()     
                # Button
                button_ttk_reg(self, ttk, "Export CSV", expconcsv, .56, .09, .075, .03)


                # ------------------------- Edit Contact Section --------------------------#

                # ----------------- Tree View  ------------------ #
                # Scroll Bar Creation
                scrollbary = tk.Scrollbar(self,)
                scrollbarx = tk.Scrollbar(self, orient='horizontal')
                scrollbary.place(relx=.98, rely=.14, relheight=.76)
                scrollbarx.place(relx=.39, rely=.91, relwidth=.59)

                # Tree Sorting
                def treeview_sort_column(tv, col, reverse):
                        l = [(tv.set(k, col), k) for k in tv.get_children('')]
                        l.sort(reverse=reverse)

                        # rearrange items in sorted positions
                        for index, (val, k) in enumerate(l):
                                tv.move(k, '', index)

                        # reverse sort next time
                        tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
                
                # Tree View Creation
                tv_columns = ("one","two","three", "four", "five","six","seven", "eight", "nine","ten","eleven", "twelve", "thirteen",
                                "fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen", "twenty")
                edtv_headings = ("First Name 1", "Last Name 1", "First Name 2", "Last Name 2", "Email 1", "Phone 1", "Email 2", "Phone 2", 
                                "Address 1", "Address 2", "Neighbourhood", "City", "Province", "Postal Code", "Company", "Prez Day", "Close Date", "Sale Price", "Commission", "Pay")
               
                edittree = ttk.Treeview(self, yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, columns = tv_columns, show='headings' )
                
                for col, hed in zip (tv_columns, edtv_headings): 
                        edittree.heading(col, anchor=tk.W, text = hed, command=lambda _col=col: treeview_sort_column(edittree, _col, False))
                        edittree.column(col, width=50, minwidth=50, stretch=tk.YES)

                scrollbary.config(command=edittree.yview)
                scrollbarx.config(command=edittree.xview)
                edittree.place(relx=.39, rely=.14, relwidth=.59, relheight=.77)

                # Get Cal list from SQL
                def addcon_sql():
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()
                        my_cursor.execute("SELECT * FROM calanderlist")
                        addcon_sql.call_list = my_cursor.fetchall()
                        my_cursor.close()
                        mydb.close()
                addcon_sql()

                # Populate Tree
                def pop_adcon_tree():
                        for i in edittree.get_children():
                            edittree.delete(i)
                        for item in addcon_sql.call_list:
                            edittree.insert("", tk.END, values=item)
                pop_adcon_tree()

                # ----------------- Tree View END  ------------------ #

class PrezPage(tk.Frame):

        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)
                
                # Canvas
                tk_canvas = tk.Canvas(self, height=976, width=1600, background = 'black')
                tk_canvas.pack()

                # Navigation Buttons
                # Contacts
                button_ttk_nav(self, ttk, 'Contacts', controller, addcontactform, .02, .03, .1, .04)
                # Listing Prez
                button_ttk_nav(self, ttk, 'Listing Prez', controller, PrezPage, .12, .03, .1, .04)
                 # Closings
                button_ttk_nav(self, ttk, 'Closings', controller, ClosingsPage, .22, .03, .1, .04)
                
                # Delete Contact Button
                def delonprez():
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()
                        delitem1 = prezlistbox.selection() # Get Tree selection
                        dictdel1 = (prezlistbox.item(delitem1)) # Get all info from selected row
                        prezinfo = (dictdel1["values"]) # get column values
                        prezuserid = (prezinfo[20]) # get user_id
                        delprezsql = "DELETE FROM calanderlist WHERE user_id = %s"
                        my_cursor.execute(delprezsql, (prezuserid,))
                        prezlistbox.delete(delitem1)
                        mydb.commit()
                        my_cursor.close()
                        mydb.close()

                button_ttk_reg(self, ttk, "Delete", delonprez, .635, .09, .075, .03)

                # ------------- Tree View -------------#
                prezscrollbary = tk.Scrollbar(self,)
                prezscrollbary.place(relx=.97, rely=.14, relheight=.80)
                prezscrollbarx = tk.Scrollbar(self, orient='horizontal')
                prezscrollbarx.place(relx=.39, rely=.94, relwidth=.58)  

                tv_columns = ("one","two","three", "four", "five","six","seven", "eight", "nine","ten","eleven", "twelve", 
                                "thirteen","fourteen","fifteen", "sixteen", "seventeen","eighteen","nineteen", "twenty")
                
                tv_headings = ("First Name 1", "Last Name 1", "First Name 2", "Last Name 2", "Email 1", "Phone 1", "Email 2", 
                                "Phone 2", "Address 1", "Address 2", "Neighbourhood", "City", "Province", "Postal Code", 
                                "Company", "Prez Day", "Close Date", "Sale Price", "Commission", "Pay")
               
                prezlistbox = ttk.Treeview(self, yscrollcommand = prezscrollbary.set, xscrollcommand = prezscrollbarx.set, columns = tv_columns, show='headings' )
                
                for col, hed in zip (tv_columns, tv_headings): 
                        prezlistbox.heading(col, anchor=tk.W, text = hed, command=lambda _col=col: treeview_sort_column(prezlistbox, _col, False))
                        prezlistbox.column(col, width=50, minwidth=50, stretch=tk.YES)

                prezscrollbary.config(command=prezlistbox.yview)
                prezscrollbarx.config(command=prezlistbox.xview)
                prezlistbox.place(relx=.39, rely=.14, relwidth=.58, relheight=.80)
                # ------------ Tree View END ------------#

                # --------------- Tree Buttons --------------# 
                self.prezinfo = tk.StringVar() # declare this variable for use within functions
                # Populate the Tree
                def get_prez_sql(prez_date1, prez_date2):
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()

                        prez_sql = "SELECT * FROM `calanderlist` WHERE `listprezday` BETWEEN %s and %s"
                        my_cursor.execute(prez_sql,(prez_date1, prez_date2))
                        self.prez_info = my_cursor.fetchall()
                        for i in prezlistbox.get_children():
                                prezlistbox.delete(i)
                        for item in self.prez_info:
                                prezlistbox.insert("", tk.END, values=item)

                        my_cursor.close()
                        mydb.close()
                get_prez_sql('2020-01-00', '2020-12-31')

                # Export CSV
                def prez_csv_exp():
                        if prez_4_year.get() == '':
                                Mbox(ctypes,'No Year Selected', 'Please select a year for csv export.', 0)
                        if prez_4_year.get() == '2019':
                                newcsv1 = open('csvs/2019prez.csv', 'w', newline='')    
                                allprezfile = csv.writer(newcsv1)
                                allprezfile.writerows(self.prez_info)
                                newcsv1.close()
                        if prez_4_year.get() == '2020':
                                newcsv2 = open('csvs/2020prez.csv', 'w', newline='')
                                allprezfile2 = csv.writer(newcsv2)
                                allprezfile2.writerows(self.prez_info)
                                newcsv2.close()
                        if prez_4_year.get() == '2021':
                                newcsv3 = open('csvs/2021prez.csv', 'w', newline='')
                                allprezfile2 = csv.writer(newcsv3)
                                allprezfile2.writerows(self.prez_info)
                                newcsv3.close()

                # Get the between values based on year selected then 
                prez_4_year = tk.StringVar()
                def get_prez_betweens(prez_4_year):
                        if prez_4_year == '2019':
                            get_prez_sql('2019-01-00', '2019-12-31')
                        if prez_4_year == '2020':
                            get_prez_sql('2020-01-00', '2020-12-31')
                        if prez_4_year == '2021':
                            get_prez_sql('2021-01-00', '2021-12-31')


                prezyear_lbl = tk.Label(self, text="Select Year:", bg="white")                                                   
                prezyear_lbl.place(relx=.39, rely=.09, relwidth=.075, relheight=.03)

                prezyear_opt = ['2019', '2020', '2021'] 
                prezyear_menu = tk.OptionMenu(self, prez_4_year, *prezyear_opt, command= lambda x: get_prez_betweens(prez_4_year.get()))
                prezyear_menu.config(bg="white", foreground="black", activeforeground="black", activebackground="white", borderwidth=0, relief="flat")        
                prezyear_menu['menu'].config(bg="white", fg="black", activebackground="white", activeforeground="black", borderwidth=0, relief="flat")                           
                prezyear_menu.place(relx=.465, rely=.09, relwidth=.075, relheight=.03)

                # Export CSV Button
                button_ttk_reg(self, ttk, "Export CSV", prez_csv_exp, .55, .09, .075, .03)
                # ---------- Populate Tree View END -------------#

                # ----------- Create PDF Stuff ----------#
                # Form Labels
                # create listing prez label
                newlistprezlbl = tk.Label(self, text="  Create New Listing Presentation:", bg="white", relief="groove", anchor="w")
                newlistprezlbl.place(relx=.02, rely=.14, relwidth=.35, relheight=.03)
                # Client Name Line 1
                # Label
                clientname1 = tk.Label(self, text="  Client Name Line One:", bg="white", anchor="w")
                clientname1.place(relx=.02, rely=.17, relwidth=.35, relheight=.03)
                # Client Name Line 2
                # Label
                clientname2 = tk.Label(self, text="  Client Name Line Two:", bg="white", anchor="w")
                clientname2.place(relx=.02, rely=.23, relwidth=.35, relheight=.03)
                # Address
                # Label
                addresslbl = tk.Label(self, text="  Address:", bg="white", anchor="w")
                addresslbl.place(relx=.02, rely=.29, relwidth=.35, relheight=.03)
                # Neighbourhood
                # Label
                neighblbl = tk.Label(self, text="  Neighbourhood:", bg="white", anchor="w")
                neighblbl.place(relx=.02, rely=.35, relwidth=.35, relheight=.03)
                
                # Form Entrys
                # Name 1 Entry
                clientnameentry1 = tk.Entry(self, bg="white")
                clientnameentry1.place(relx=.02, rely=.20, relwidth=.35, relheight=.03)
                # Name 2 Entry
                clientnameentry2 = tk.Entry(self, bg="white")
                clientnameentry2.place(relx=.02, rely=.26, relwidth=.35, relheight=.03)
                # Prez Address Entry
                addressentry = tk.Entry(self, bg="white")
                addressentry.place(relx=.02, rely=.32, relwidth=.35, relheight=.03)
                # Prez Neighbourhood Entry
                neighbentry = tk.Entry(self, bg="white")
                neighbentry.place(relx=.02, rely=.38, relwidth=.35, relheight=.03)                   
                # Image              
                # File Name Label
                #crm_lbl(self, tk, "   Select Image:", 'groove', "w", 'white', 'black', '.02', '.41', '.325', '.03')
                imagenamelbl = tk.Label(self, bg="white", text="   Select Image:", anchor="w")
                imagenamelbl.place(relx=.02, rely=.41, relwidth=.325, relheight=.03)

                # Open File Explorer Button
                def open_file():
                    openfile(filedialog, imagenamelbl, ImageTk, PIL, Image)

                button_ttk_reg(self, ttk, "---", open_file, .345, .41, .025, .03 )

                # Get fonts 
                pdfmetrics.registerFont(TTFont('Gotham-Bold-Regular', 'Gotham-Bold-Regular.ttf'))
                pdfmetrics.registerFont(TTFont('Gotham-Light', 'Gotham-Light.ttf'))
                pdfmetrics.registerFont(TTFont('Gotham-Pro-Black', 'Gotham-Pro-Black.ttf'))

                # -----  Create PDF - Non Flowable - March 2020 ------ #
                prez_page_1  = "pdfs/prez_page_1.pdf"
                merge_prez_1of2 = "pdfs/merge_prez_1of2.pdf"
                prez_page_14 = "pdfs/prez_page_14.pdf"
                merge_prez_2of2 = "pdfs/merge_prez_2of2.pdf"
                offer_example = "pdfs/offer_example.pdf"
                listing_agreement = "pdfs/listing_agreement.pdf"
                sched_a = "pdfs/sched_a.pdf"
                wwr = "pdfs/wwr.pdf"
                sellers_direction = "pdfs/sellers_direction.pdf"
                prez_notes = "pdfs/prez_notes.pdf"
                
                # Royal Lepage Logo
                rlp_logo = "images/rlp_logo.jpg"
                # Left margin on PDF
                pdf_margin = 0.5

                # Make PDF
                def make_pdf():
                        # Entry Gets   
                        cliname1 = clientnameentry1.get()
                        cliname2 = clientnameentry2.get()
                        prezaddy = addressentry.get()
                        prezneighb = neighbentry.get()
                        
                        # Draw PDF
                        draw_pdf(prez_page_1, merge_prez_1of2, prez_page_14, merge_prez_2of2, offer_example, listing_agreement, 
                                sched_a, wwr, sellers_direction, prez_notes, cliname1, cliname2, prezaddy, prezneighb, rlp_logo, 
                                pdf_margin, canvas, letter, inch, PdfFileMerger, filedialog)

                        # Clear Forms
                        prez_forms = (clientnameentry1, clientnameentry2, addressentry, neighbentry)
                        clear_forms(self, prez_forms)
                        
                        # Change Back image Label to blank
                        label_config(imagenamelbl, "   Select Image:")

                        # Success message
                        Mbox(ctypes,'Success', 'The New Listing Presentation Has Been Created', 0)
       
                # Create PDF Button
                button_ttk_reg(self, ttk, "Create Presentation", make_pdf, .02, .44, .35, .03)                                        
                            
class ClosingsPage(tk.Frame):

        def __init__(self, parent, controller):
                tk.Frame.__init__(self, parent)

                # Mysql Connection & Cursor
                mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                my_cursor = mydb.cursor()
                # Canvas
                canvas = tk.Canvas(self, height=976, width=1600, background = 'black')
                canvas.pack()
            
                # Navigation Buttons
                # Contacts
                button_ttk_nav(self, ttk, 'Contacts', controller, addcontactform, .02, .03, .1, .04)
                # Listing Prez
                button_ttk_nav(self, ttk, 'Listing Prez', controller, PrezPage, .12, .03, .1, .04)
                 # Closings
                button_ttk_nav(self, ttk, 'Closings', controller, ClosingsPage, .22, .03, .1, .04)
                
                # Delete Contact Button
                def delonclose():
                        my_cursor = mydb.cursor()
                        delitem2 = closelistbox.selection() # Get Tree selection
                        dictdel2 = (closelistbox.item(delitem2)) # Get all info from selected row
                        closeinfo = (dictdel2["values"]) # get column values
                        closeuserid = (closeinfo[6]) # get user_id
                        delclosesql = "DELETE FROM transactions WHERE user_id = %s"
                        my_cursor.execute(delclosesql, (closeuserid,))
                        mydb.commit()
                        closelistbox.delete(delitem2)

                button_ttk_reg(self, ttk, "Delete", delonclose, .635, .09, .075, .03)  

                # ------------- Tree View -------------#
                clscrollbary = tk.Scrollbar(self,)
                clscrollbary.place(relx=.98, rely=.14, relheight=.60)
                clscrollbarx = tk.Scrollbar(self, orient='horizontal')
                clscrollbarx.place(relx=.39, rely=.74, relwidth=.59)

                # Tree View Table Creation
                tv_columns = ("one","two","three", "four", "five","six",)
                tv_headings = ("Client Name", "Address", "Close Date", "Sale Price", "Commission", "Pay")
               
                closelistbox = ttk.Treeview(self, yscrollcommand = clscrollbary.set, xscrollcommand = clscrollbarx.set, columns = tv_columns, show='headings' )
                
                for col, hed in zip (tv_columns, tv_headings): 
                        closelistbox.heading(col, anchor=tk.W, text = hed, command=lambda _col=col: treeview_sort_column(closelistbox, _col, False))
                        closelistbox.column(col, width=50, minwidth=50, stretch=tk.YES)

                clscrollbary.config(command=closelistbox.yview)
                clscrollbarx.config(command=closelistbox.xview)
                closelistbox.place(relx=.39, rely=.14, relwidth=.59, relheight=.60)
                # ------------ Tree View END -------------#

                # Get Info from Sql
                def get_close_sql(close_date1, close_date2):
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()

                        close_sql = "SELECT * FROM `transactions` WHERE `closedate` BETWEEN %s and %s"
                        my_cursor.execute(close_sql,(close_date1, close_date2))
                        get_close_sql.close_info = my_cursor.fetchall()

                        my_cursor.close()
                        mydb.close()
                get_close_sql('2019-11-15', '2020-11-15')

                # Clear the Tree
                def clear_close_tree():
                        for i in closelistbox.get_children():
                                closelistbox.delete(i)
                clear_close_tree()

                # Populate the Tree
                def pop_close_tree():
                        for item in get_close_sql.close_info:
                                closelistbox.insert("", tk.END, values=item)
                pop_close_tree()

                # Export CSV
                def close_csv_exp():
                        if close_4_year.get() == '':
                                Mbox(ctypes,'No Year Selected', 'Please select a year for csv export.', 0)
                        if close_4_year.get() == '2019':
                                newcsv1 = open('csvs/2019close.csv', 'w', newline='')    
                                allprezfile = csv.writer(newcsv1)
                                allprezfile.writerows(get_close_sql.close_info)
                                newcsv1.close()
                        if close_4_year.get() == '2020':
                                newcsv2 = open('csvs/2020close.csv', 'w', newline='')
                                allprezfile2 = csv.writer(newcsv2)
                                allprezfile2.writerows(get_close_sql.close_info)
                                newcsv2.close()
                        if close_4_year.get() == '2021':
                                newcsv3 = open('csvs/2021close.csv', 'w', newline='')
                                allprezfile2 = csv.writer(newcsv3)
                                allprezfile2.writerows(get_close_sql.close_info)
                                newcsv3.close()

                # Get the between values based on year selected then 
                close_4_year = tk.StringVar()
                def get_close_betweens(close_4_year):
                        if close_4_year == '2019':
                            get_close_sql('2018-11-16', '2019-11-15')
                        if close_4_year == '2020':
                            get_close_sql('2019-11-16', '2020-11-15')
                        if close_4_year == '2021':
                            get_close_sql('2020-11-16', '2021-11-15')
                        clear_close_tree()
                        pop_close_tree()
                # Select Year Label
                closeyear_lbl = tk.Label(self, text="Select Year:", bg="white")                                                   
                closeyear_lbl.place(relx=.39, rely=.09, relwidth=.075, relheight=.03)
                # Year Menu
                closeyear_opt = ['2019', '2020', '2021'] 
                closeyear_menu = tk.OptionMenu(self, close_4_year, *closeyear_opt, command= lambda x: get_close_betweens(close_4_year.get()))
                closeyear_menu.config(bg="white", foreground="black", activeforeground="black", activebackground="white", borderwidth=0, relief="flat")        
                closeyear_menu['menu'].config(bg="white", fg="black", activebackground="white", activeforeground="black", borderwidth=0, relief="flat")                           
                closeyear_menu.place(relx=.465, rely=.09, relwidth=.075, relheight=.03)
                # Export Button
                button_ttk_reg(self, ttk, "Export CSV", close_csv_exp, .55, .09, .075, .03)

                # Transaction Entrys
                # Name
                crm_lbl(self, tk, "  Client Name:", 'groove', 'w', 'white', 'black', .02, .14, .175, .03)
                trans_name_entry = tk.Entry(self, bg="white")
                trans_name_entry.place(relx=.02, rely=.17, relwidth=.175, relheight=.03)
                # Address
                crm_lbl(self, tk, "  Address:", 'groove', 'w', 'white', 'black', .02, .20, .175, .03)
                trans_addy_entry = tk.Entry(self, bg="white")
                trans_addy_entry.place(relx=.02, rely=.23, relwidth=.175, relheight=.03)
                # Close Date
                crm_lbl(self, tk, "  Close Date: YYYY-MM-DD", 'groove', 'w', 'white', 'black', .02, .26, .175, .03)
                trans_close_entry = tk.Entry(self, bg="white")
                trans_close_entry.place(relx=.02, rely=.29, relwidth=.175, relheight=.03)
                # Sale Price
                crm_lbl(self, tk, "  Sale Price:", 'groove', 'w', 'white', 'black', .195, .14, .175, .03)
                trans_price_entry = tk.Entry(self, bg="white")
                trans_price_entry.place(relx=.195, rely=.17, relwidth=.175, relheight=.03)
                trans_price_entry.insert(0, 0)
                # Commission
                crm_lbl(self, tk, "  Commission:", 'groove', 'w', 'white', 'black', .195, .20, .175, .03)
                trans_comm_entry = tk.Entry(self, bg="white")
                trans_comm_entry.place(relx=.195, rely=.23, relwidth=.175, relheight=.03)
                trans_comm_entry.insert(0, 0)
                # Commission % or $ Option Menu
                comm_type = tk.StringVar()
                crm_lbl(self, tk, "$ or %", 'groove', 'w', 'white', 'black', .335, .20, .035, .03)
                comish_opt = ['$', '%'] 
                comish_menu = tk.OptionMenu(self, comm_type, *comish_opt, command= lambda x: get_close_betweens(comm_type.get()))
                comish_menu.config(bg="white", foreground="black", activeforeground="black", activebackground="white", borderwidth=0, relief="flat")        
                comish_menu['menu'].config(bg="white", fg="black", activebackground="white", activeforeground="black", borderwidth=0, relief="flat")                           
                comish_menu.place(relx=.335, rely=.23, relwidth=.035, relheight=.03)

                # clear transaction form
                trans_forms = (trans_name_entry, trans_addy_entry, trans_close_entry, trans_price_entry, trans_comm_entry)
                def clear_form():
                        clear_forms(self, trans_forms)

                # Add Transaction
                def add_trans():
                        # Gets
                        t_name = trans_name_entry.get()
                        t_addy = trans_addy_entry.get()
                        t_close = trans_close_entry.get()
                        if len(trans_close_entry.get()) == 0:
                            t_close = "0000-00-00"
                        t_price = int(trans_price_entry.get())
                        t_comm = float(trans_comm_entry.get())
                        t_comtyp = comm_type.get()
                        t_pay = float()
                        if t_comtyp == "$":
                            t_pay = t_comm
                        else:
                            t_pay = (t_price * (t_comm / 100))

                        # Connect to Sql
                        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
                        my_cursor = mydb.cursor()
                        # Insert Transaction into Sql
                        add_2_trans = "INSERT INTO transactions (clientname, address, closedate, saleprice, commission, pay) VALUES (%s, %s, %s, %s, %s, %s)"
                        t_new = (t_name, t_addy, t_close, t_price, t_comm, t_pay)
                        my_cursor.execute(add_2_trans, t_new)
                        # Close Sql
                        mydb.commit()
                        my_cursor.close()
                        mydb.close()
                        clear_forms(self, trans_forms)

                # Add Transaction Button
                button_ttk_reg(self, ttk, "Add Transaction", add_trans, .195, .26, .175, .03)
                # Clear Form Button
                button_ttk_reg(self, ttk, "Clear Form", clear_form, .195, .29, .175, .03)

                # --------- Award Tracking --------- #
                # get_close_sql.close_info

                # get commision amounts from sql
                def get_comm_amt():
                        get_comm_amt.total_commish = 0
                        for item in get_close_sql.close_info:
                                get_comm_amt.total_commish += float(item[5])
                get_close_sql('2019-11-16', '2020-11-15')
                get_comm_amt()

                # divide commision amt by 650 to figure out width of label
                def goal_percent(com_sofar):
                        goal_percent.amt = (com_sofar / 650000)*.96
                goal_percent(get_comm_amt.total_commish)

                # figure out rel_x
                def goal_relx(g_dollar):
                        goal_relx.g_relx = (((g_dollar / 650000)*.96)- .02)

                # make the commision amount label
                def make_comm_lbl(comm_lbl_txt, comm_lbl_bg, comm_lbl_fg, comm_lbl_x, comm_lbl_y, comm_lbl_w, comm_lbl_h):
                        com_label = tk.Label(self, text=comm_lbl_txt, bg = comm_lbl_bg, fg = comm_lbl_fg)
                        com_label.place(relx=comm_lbl_x, rely=comm_lbl_y, relwidth=comm_lbl_w, relheight=comm_lbl_h)
                

                make_comm_lbl(get_comm_amt.total_commish, 'green', 'white', '.02', '.88', goal_percent.amt, '.04')
                # Presidents Gold
                goal_relx(125000)
                make_comm_lbl('Presidents Gold\n$125,000\n|', 'black', 'white', goal_relx.g_relx, '.82', '.08', '.06')
                # Platinum
                goal_relx(230000)
                make_comm_lbl('Platinum\n$230,000\n|', 'black', 'white', goal_relx.g_relx, '.82', '.08', '.06')
                # Diamond
                goal_relx(340000)
                make_comm_lbl('Diamond\n$340,000\n|', 'black', 'white', goal_relx.g_relx, '.82', '.08', '.06')
                # Red Diamond
                goal_relx(500000)
                make_comm_lbl('Red Diamond\n$500,000\n|', 'black', 'white', goal_relx.g_relx,'.82', '.08', '.06')  
                # --------- Award Tracking END --------- #



app = crmapp()
app.mainloop()