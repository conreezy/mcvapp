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
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Frame
from reportlab.rl_config import defaultPageSize
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
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
DropMenu,
create_tree,
draw_featuresheet,
openfile1, openfile2, openfile3, openfile4, openfile5, openfile6, openfile7, openfile8, openfile9, openfile10, openfile11
)

SEVENTENELEVEN = (17*inch, 11*inch)
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

 # Get fonts 
pdfmetrics.registerFont(TTFont('Gotham-Bold-Regular', 'Gotham-Bold-Regular.ttf'))
pdfmetrics.registerFont(TTFont('Gotham-Light', 'Gotham-Light.ttf'))
pdfmetrics.registerFont(TTFont('Gotham-Pro-Black', 'Gotham-Pro-Black.ttf'))
pdfmetrics.registerFont(TTFont('Gotham-Narrow-Medium', 'Gotham-Narrow-Medium.ttf'))
pdfmetrics.registerFont(TTFont('Gotham-Narrow-Bold', 'Gotham-Narrow-Bold.ttf'))
pdfmetrics.registerFont(TTFont('Gotham-Narrow-Light', 'Gotham-Narrow-Light.ttf'))
pdfmetrics.registerFont(TTFont('MrsEaves_Roman', 'MrsEaves_Roman.ttf'))

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

        for F in (Contacts, PrezPage, ClosingsPage, PropertyManagement, FeatureSheet):

                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Contacts)

    # Change Pages
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def navbutton(self, controller):
    # Navigation Buttons
    # Contacts
    button_ttk_nav(self, ttk, 'Contacts', controller, Contacts, .02, .01, .1, .04)
    # Closings
    button_ttk_nav(self, ttk, 'Closings', controller, ClosingsPage, .12, .01, .1, .04)
    # Listing Prez
    button_ttk_nav(self, ttk, 'Listing Prez', controller, PrezPage, .22, .01, .1, .04)
    # Feature Sheets
    button_ttk_nav(self, ttk, 'Feature Sheets', controller, FeatureSheet, .32, .01, .1, .04)

def window(self):        
    w_width  = tk.Frame.winfo_screenwidth(self)
    w_height = tk.Frame.winfo_screenheight(self)
    canvas = tk.Canvas(self, height=w_height, width=w_width, background = 'black')
    canvas.pack()

class Contacts(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        window(self)
        #user id tracker for deleting old contact that has been edited
        self.useridedit = 0
        # data base list selection from drop down menu to track which data to re-populate tree with
        editfrmhere = tk.StringVar()

        # Nav Buttons
        navbutton(self, controller)

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
        crm_lbl(self, tk, "  Company:", 'groove', 'w', 'white', 'black', '.02', '.42', '.175', '.03')
        # Company Entry
        companyentry = tk.Entry(self, bg="white")
        companyentry.place(relx=.02, rely=.45, relwidth=.175, relheight=.03)
        # List Prez Day Label
        crm_lbl(self, tk, "  List Prez Day: YYYY-MM-DD", 'groove', 'w', 'white', 'black', '.195', '.42', '.175', '.03')
        # List Prez Day Entry
        listprezdayentry = tk.Entry(self, bg="white")
        listprezdayentry.place(relx=.195, rely=.45, relwidth=.175, relheight=.03)
        # Address line 1 Label
        crm_lbl(self, tk, "  Address Line One:", 'groove', 'w', 'white', 'black', '.02', '.48', '.35', '.03') 
        # Address line 1 Entry
        address1entry = tk.Entry(self, bg="white")
        address1entry.place(relx=.02, rely=.51, relwidth=.35, relheight=.03)
        # Address line 2 Label
        crm_lbl(self, tk, "  Address Line Two:", 'groove', 'w', 'white', 'black', '.02', '.54', '.35', '.03')
        # Address line 2 Entry
        address2entry = tk.Entry(self, bg="white")
        address2entry.place(relx=.02, rely=.57, relwidth=.35, relheight=.03)
        # City Label
        crm_lbl(self, tk, "  City:", 'groove', 'w', 'white', 'black', '.02', '.60', '.175', '.03')
        # City Entry
        cityentry = tk.Entry(self, bg="white")
        cityentry.place(relx=.02, rely=.63, relwidth=.175, relheight=.03)
        # Neighbourhood Label
        crm_lbl(self, tk, "  Neighbourhood:", 'groove', 'w', 'white', 'black', '.195', '.60', '.175', '.03')
        # Neighbourhood Entry
        neighbentry = tk.Entry(self, bg="white")
        neighbentry.place(relx=.195, rely=.63, relwidth=.175, relheight=.03)
        # Province Label
        crm_lbl(self, tk, "  Province:", 'groove', 'w', 'white', 'black', '.02', '.66', '.175', '.03')
        # Province Entry
        proventry = tk.Entry(self, bg="white")
        proventry.place(relx=.02, rely=.69, relwidth=.175, relheight=.03)
        # Postal Code Label
        crm_lbl(self, tk, "  Postal Code:", 'groove', 'w', 'white', 'black', '.195', '.66', '.175', '.03')
        # Postal Code Entry
        postalcodeentry = tk.Entry(self, bg="white",)
        postalcodeentry.place(relx=.195, rely=.69, relwidth=.175, relheight=.03)
        
        # Pop-Up Box
        def Mbox(title, text, style):
                return ctypes.windll.user32.MessageBoxW(0, text, title, style)

        # Clear Form 
        con_forms = (firstname1entry, lastname1entry, firstname2entry, lastname2entry, email1entry, email2entry, phone1entry, phone2entry, companyentry, listprezdayentry, 
                    address1entry, address2entry, cityentry ,neighbentry, proventry, postalcodeentry)

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
            self.useridedit =  (usereditinfo[16]) # Get User_id for use in deleting the chosen contact**
            
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

            # Insert Contact into MySQL
            add2choicedb2 = "INSERT INTO calanderlist (firstname1, lastname1, firstname2, lastname2, email1, phone1, email2, phone2, addressline1, addressline2, neighbourhood, city, province, postalcode, company, listprezday) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            newcontact2 = (fn1get, ln1get, fn2get, ln2get, em1get, p1get, em2get, p2get, a1get, a2get, neighbget, cityget, provget, pcget, comget, pdayget,)
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

        # ---- Buttons ---- #
        # Add Contact Button
        ttk_btn_style = ttk.Style()
        ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)
        ttk_button = ttk.Button(self, text= "Add to Database", style="Nav.TButton", command = lambda:[add_con(), delete_con(), clear_con_form()])
        ttk_button.place(relx=.02, rely=.75, relwidth=.35, relheight=.04)

        # Clear Form Button
        button_ttk_reg(self, ttk, 'white', "Clear Form", clear_con_form, .02, .72, .35, .03)

        # Edit Contact Button
        ttk_btn_style = ttk.Style()
        ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)
        ttk_button = ttk.Button(self, text= "Edit", style="Nav.TButton", command = lambda: [clear_con_form(), edit_con()])
        ttk_button.place(relx=.475, rely=.09, relwidth=.075, relheight=.03)

        # Delete Contact Button
        button_ttk_reg(self, ttk, 'white', "Delete", delete_con, .39, .09, .075, .03)

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
        button_ttk_reg(self, ttk, 'white', "Export CSV", expconcsv, .56, .09, .075, .03)
        
        # # ----------------- Tree View  ------------------ #
        # --- Tree --- #
        tv_columns = ("one","two","three", "four", "five","six","seven", "eight", "nine","ten","eleven", "twelve", "thirteen",
                  "fourteen","fifteen", "sixteen")

        tv_headings = ("First Name 1", "Last Name 1", "First Name 2", "Last Name 2", "Email 1", "Phone 1", "Email 2", "Phone 2", 
                  "Address 1", "Address 2", "Neighbourhood", "City", "Province", "Postal Code", "Company", "Prez Day")

        #----------
        sby_x = .98
        sby_y = .14
        sby_h = .80
        #
        sbx_x = .39
        sbx_y = .94
        sbx_w = .59 
        #
        tree_x = .39 
        tree_y = .14 
        tree_w = .59 
        tree_h = .80

        # Scroll Bar Creation
        scrollbary = tk.Scrollbar(self,)
        scrollbarx = tk.Scrollbar(self, orient='horizontal')
        scrollbary.place(relx=sby_x, rely=sby_y, relheight=sby_h)
        scrollbarx.place(relx=sbx_x, rely=sbx_y, relwidth=sbx_w)

        # Tree Sorting
        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
         
        contact_tree = ttk.Treeview(self, yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, columns = tv_columns, show='headings' )
          
        for col, hed in zip (tv_columns, tv_headings): 
            contact_tree.heading(col, anchor=tk.W, text = hed, command=lambda _col=col: treeview_sort_column(contact_tree, _col, False))
            contact_tree.column(col, width=55, minwidth=50, stretch=tk.YES)

        scrollbary.config(command=contact_tree.yview)
        scrollbarx.config(command=contact_tree.xview)
        contact_tree.place(relx=tree_x, rely=tree_y, relwidth=tree_w, relheight=tree_h)

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
            for i in contact_tree.get_children():
                contact_tree.delete(i)
            for item in addcon_sql.call_list:
                contact_tree.insert("", tk.END, values=item)
        pop_adcon_tree()

        # ----------------- Tree View END  ------------------ #

class PrezPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        window(self)

        # Navigation Buttons
        navbutton(self, controller)
        
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

        button_ttk_reg(self, ttk, 'white', "Delete", delonprez, .635, .09, .075, .03)

        # # ----------------- New pres Tree View  ------------------ #
        # --- Tree --- #
        tv_columns = ("one","two","three", "four", "five","six","seven", "eight", "nine","ten","eleven", "twelve", "thirteen",
                  "fourteen","fifteen", "sixteen")

        tv_headings = ("First Name 1", "Last Name 1", "First Name 2", "Last Name 2", "Email 1", "Phone 1", "Email 2", "Phone 2", 
                  "Address 1", "Address 2", "Neighbourhood", "City", "Province", "Postal Code", "Company", "Prez Day")

        #----------
        sby_x = .98
        sby_y = .14
        sby_h = .80
        #
        sbx_x = .39
        sbx_y = .94
        sbx_w = .59 
        #
        tree_x = .39 
        tree_y = .14 
        tree_w = .59 
        tree_h = .80

        # Scroll Bar Creation
        scrollbary = tk.Scrollbar(self,)
        scrollbarx = tk.Scrollbar(self, orient='horizontal')
        scrollbary.place(relx=sby_x, rely=sby_y, relheight=sby_h)
        scrollbarx.place(relx=sbx_x, rely=sbx_y, relwidth=sbx_w)

        # Tree Sorting
        def treeview_sort_column(tv, col, reverse):
            l = [(tv.set(k, col), k) for k in tv.get_children('')]
            l.sort(reverse=reverse)

            # rearrange items in sorted positions
            for index, (val, k) in enumerate(l):
                    tv.move(k, '', index)

            # reverse sort next time
            tv.heading(col, command=lambda: treeview_sort_column(tv, col, not reverse))
         
        contact_tree = ttk.Treeview(self, yscrollcommand = scrollbary.set, xscrollcommand = scrollbarx.set, columns = tv_columns, show='headings' )
          
        for col, hed in zip (tv_columns, tv_headings): 
            contact_tree.heading(col, anchor=tk.W, text = hed, command=lambda _col=col: treeview_sort_column(contact_tree, _col, False))
            contact_tree.column(col, width=55, minwidth=50, stretch=tk.YES)

        scrollbary.config(command=contact_tree.yview)
        scrollbarx.config(command=contact_tree.xview)
        contact_tree.place(relx=tree_x, rely=tree_y, relwidth=tree_w, relheight=tree_h)

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
            for i in contact_tree.get_children():
                contact_tree.delete(i)
            for item in addcon_sql.call_list:
                contact_tree.insert("", tk.END, values=item)
        pop_adcon_tree()

        # --------------- Tree Buttons --------------# 
        self.prezinfo = tk.StringVar() # declare this variable for use within functions
        # Populate the Tree
        def get_prez_sql(prez_date1, prez_date2):
            mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
            my_cursor = mydb.cursor()

            prez_sql = "SELECT * FROM `calanderlist` WHERE `listprezday` BETWEEN %s and %s"
            my_cursor.execute(prez_sql,(prez_date1, prez_date2))
            self.prez_info = my_cursor.fetchall()
            for i in contact_tree.get_children():
                    contact_tree.delete(i)
            for item in self.prez_info:
                    contact_tree.insert("", tk.END, values=item)

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
        button_ttk_reg(self, ttk, 'white', "Export CSV", prez_csv_exp, .55, .09, .075, .03)
        # ---------- Populate Tree View END -------------#

        # ----------- Create PDF Stuff ----------#
        # --- PDF Labels --- #
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

        # --- PDF Entrys --- #
        # Name 1 Entry
        def check_cl1(cl1_Value):
            if len(cl1_Value.get()) > 22:
                Mbox(ctypes,'Too Long', 'Name Line 1 cannot exceed 22 characters in length.', 0)
                cl1_Value.set(cl1_Value.get()[:22])
            else:
                pass
        cl1_Value=tk.StringVar() 
        cl1_Value.trace('w', lambda *args: check_cl1(cl1_Value))
        clientnameentry1 = tk.Entry(self, bg="white", textvariable =cl1_Value)
        clientnameentry1.place(relx=.02, rely=.20, relwidth=.35, relheight=.03)

        # Name 2 Entry
        def check_cl2(cl2_Value):
            if len(cl2_Value.get()) > 22:
                Mbox(ctypes,'Too Long', 'Name Line 2 cannot exceed 22 characters in length.', 0)
                cl2_Value.set(cl2_Value.get()[:22])
            else:
                pass
        cl2_Value=tk.StringVar()
        cl2_Value.trace('w', lambda *args: check_cl2(cl2_Value))
        clientnameentry2 = tk.Entry(self, bg="white", textvariable = cl2_Value)
        clientnameentry2.place(relx=.02, rely=.26, relwidth=.35, relheight=.03)

        # Prez Address Entry
        def check_addy(addy_Value):
            if len(addy_Value.get()) > 20:
                Mbox(ctypes,'Too Long', 'Address cannot exceed 20 characters in length.', 0)
                addy_Value.set(addy_Value.get()[:20])
            else:
                pass
        addy_Value=tk.StringVar() 
        addy_Value.trace('w', lambda *args: check_addy(addy_Value))
        addressentry = tk.Entry(self, bg="white", textvariable = addy_Value)
        addressentry.place(relx=.02, rely=.32, relwidth=.35, relheight=.03)

        # Prez Neighbourhood Entry
        def check_neighb(neighb_Value):
            if len(neighb_Value.get()) > 40:
                Mbox(ctypes,'Too Long', 'Neighbourhood cannot exceed 40 characters in length.', 0)
                neighb_Value.set(neighb_Value.get()[:40])
            else:
                pass
        neighb_Value=tk.StringVar() 
        neighb_Value.trace('w', lambda *args: check_neighb(neighb_Value))
        neighbentry = tk.Entry(self, bg="white", textvariable =neighb_Value)
        neighbentry.place(relx=.02, rely=.38, relwidth=.35, relheight=.03)     

        # Image              
        # File Name Label
        #crm_lbl(self, tk, "   Select Image:", 'groove', "w", 'white', 'black', '.02', '.41', '.325', '.03')
        imagenamelbl = tk.Label(self, bg="white", text="   Select Image:", anchor="w")
        imagenamelbl.place(relx=.02, rely=.41, relwidth=.325, relheight=.03)

        # Open File Explorer Button
        def open_file():
            openfile(filedialog, imagenamelbl, ImageTk, PIL, Image)

        button_ttk_reg(self, ttk, 'white', "---", open_file, .345, .41, .025, .03 )



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
        button_ttk_reg(self, ttk, 'white', "Create Presentation", make_pdf, .02, .44, .35, .03)                                        
                            
class ClosingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Mysql Connection & Cursor
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="Rocketship99!", db="mcvcontacts")
        my_cursor = mydb.cursor()

        window(self)
    
        # Navigation Buttons
        navbutton(self, controller)
        
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

        button_ttk_reg(self, ttk, 'white', "Delete", delonclose, .635, .09, .075, .03)  

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
        button_ttk_reg(self, ttk, 'white', "Export CSV", close_csv_exp, .55, .09, .075, .03)

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
        button_ttk_reg(self, ttk, 'white', "Add Transaction", add_trans, .195, .26, .175, .03)
        # Clear Form Button
        button_ttk_reg(self, ttk, 'white', "Clear Form", clear_form, .195, .29, .175, .03)

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

class PropertyManagement(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        window(self)

        # Navigation Buttons
        navbutton(self, controller)

class FeatureSheet(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        window(self)

        # Navigation Buttons
        navbutton(self, controller)
        
        # ----------- Create PDF Stuff ----------#
        # Form Labels
        # create listing prez label
        crm_lbl(self, tk, "  Create New Listing Presentation:", 'groove', 'w', 'white', 'black', '.02', '.14', '.36', '.03')
        
        # --- Form Entrys --- #
        # --- Adress Entry --- #
        crm_lbl(self, tk, "  Address:", 'groove', 'w', 'white', 'black', '.02', '.17', '.18', '.03')
        
        def checkAddy(addressValue):
            if len(addressValue.get()) > 30:
                Mbox(ctypes,'Too Long', 'Address cannot exceed 23 character in length.', 0)
                addressValue.set(addressValue.get()[:30])
            else:
                pass
        addressValue=tk.StringVar() 
        addressValue.trace('w', lambda *args: checkAddy(addressValue))
        address_entry = tk.Entry(self, bg="white", textvariable=addressValue)
        address_entry.place(relx=.02, rely=.20, relwidth=.18, relheight=.03)

        # --- Neighbourhood Entry --- #
        crm_lbl(self, tk, "  Neighbourhood:", 'groove', 'w', 'white', 'black', '.20', '.17', '.18', '.03')

        def checkNeighb(neighbValue):
            if len(neighbValue.get()) > 30:
                Mbox(ctypes,'Too Long', 'Neighbourhood cannot exceed 30 character in length.', 0)
                neighbValue.set(neighbValue.get()[:30])
            else:
                pass
        neighbValue=tk.StringVar() 
        neighbValue.trace('w', lambda *args: checkNeighb(neighbValue))
        neighb_entry = tk.Entry(self, bg="white", textvariable=neighbValue)
        neighb_entry.place(relx=.20, rely=.20, relwidth=.18, relheight=.03)

        # --- Price Entry --- #
        crm_lbl(self, tk, "  Price:", 'groove', 'w', 'white', 'black', '.02', '.23', '.09', '.03')

        def checkPrice(priceValue):
            if len(priceValue.get()) > 11:
                Mbox(ctypes,'Too Long', 'Price cannot exceed 11 character in length.', 0)
                priceValue.set(priceValue.get()[:11])
            else:
                pass
        priceValue=tk.StringVar() 
        priceValue.trace('w', lambda *args: checkPrice(priceValue))
        price_entry = tk.Entry(self, bg="white", textvariable=priceValue)
        price_entry.place(relx=.02, rely=.26, relwidth=.09, relheight=.03)
        
        # --- MLS # Entry --- #
        crm_lbl(self, tk, "  MLS#:", 'groove', 'w', 'white', 'black', '.11', '.23', '.09', '.03')

        def checkMls(mlsValue):
            if len(mlsValue.get()) > 7:
                Mbox(ctypes,'Too Long', 'MLS# cannot exceed 7 character in length.', 0)
                mlsValue.set(mlsValue.get()[:7])
            else:
                pass
        mlsValue=tk.StringVar() 
        mlsValue.trace('w', lambda *args: checkMls(mlsValue))
        mls_entry = tk.Entry(self, bg="white", textvariable=mlsValue)
        mls_entry.place(relx=.11, rely=.26, relwidth=.09, relheight=.03)
        
        # --- Bedrooms --- #
        crm_lbl(self, tk, "  Bedrooms:", 'groove', 'w', 'white', 'black', '.20', '.23', '.09', '.03')

        def checkBeds(bedsValue):
            if len(bedsValue.get()) > 2:
                Mbox(ctypes,'Too Long', 'Bedrooms cannot exceed 2 character in length.', 0)
                bedsValue.set(bedsValue.get()[:2])
            else:
                pass
        bedsValue=tk.StringVar() 
        bedsValue.trace('w', lambda *args: checkBeds(bedsValue))
        bedrooms_entry = tk.Entry(self, bg="white", textvariable=bedsValue)
        bedrooms_entry.place(relx=.20, rely=.26, relwidth=.09, relheight=.03) 
        
        # --- Bathrooms --- #
        crm_lbl(self, tk, "  Bathrooms:", 'groove', 'w', 'white', 'black', '.29', '.23', '.09', '.03')

        def checkBaths(bathsValue):
            if len(bathsValue.get()) > 2:
                Mbox(ctypes,'Too Long', 'Bathrooms cannot exceed 2 character in length.', 0)
                bathsValue.set(bathsValue.get()[:2])
            else:
                pass
        bathsValue=tk.StringVar() 
        bathsValue.trace('w', lambda *args: checkBaths(bathsValue))
        bathrooms_entry = tk.Entry(self, bg="white", textvariable=bathsValue)
        bathrooms_entry.place(relx=.29, rely=.26, relwidth=.09, relheight=.03)

        # --- Type Entry --- #
        crm_lbl(self, tk, "  Type:", 'groove', 'w', 'white', 'black', '.02', '.29', '.12', '.03')

        def checkType(typeValue):
            if len(typeValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Type cannot exceed 21 characters in length.', 0)
                typeValue.set(typeValue.get()[:21])
            else:
                pass
        typeValue=tk.StringVar() 
        typeValue.trace('w', lambda *args: checkType(typeValue))
        type_entry = tk.Entry(self, bg="white", textvariable=typeValue)
        type_entry.place(relx=.02, rely=.32, relwidth=.12, relheight=.03)
        
        # --- Style Entry --- #
        crm_lbl(self, tk, "  Style:", 'groove', 'w', 'white', 'black', '.14', '.29', '.12', '.03')

        def checkStyle(styleValue):
            if len(styleValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Style cannot exceed 21 characters in length.', 0)
                styleValue.set(styleValue.get()[:21])
            else:
                pass
        styleValue=tk.StringVar() 
        styleValue.trace('w', lambda *args: checkStyle(styleValue))
        style_entry = tk.Entry(self, bg="white", textvariable=styleValue)
        style_entry.place(relx=.14, rely=.32, relwidth=.12, relheight=.03)

        # ---Taxes Entry --- #
        crm_lbl(self, tk, "  Taxes:", 'groove', 'w', 'white', 'black', '.26', '.29', '.12', '.03')

        def checkTaxes(taxesValue):
            if len(taxesValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Taxes cannot exceed 21 characters in length.', 0)
                taxesValue.set(taxesValue.get()[:21])
            else:
                pass
        taxesValue=tk.StringVar() 
        taxesValue.trace('w', lambda *args: checkTaxes(taxesValue))
        taxes_entry = tk.Entry(self, bg="white", textvariable=taxesValue)
        taxes_entry.place(relx=.26, rely=.32, relwidth=.12, relheight=.03)
        
        # --- Heat / fuel Entry --- #
        crm_lbl(self, tk, "  Heat/Fuel:", 'groove', 'w', 'white', 'black', '.02', '.35', '.09', '.03')

        def checkHeat(heatValue):
            if len(heatValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Heat/Fuel cannot exceed 21 characters in length.', 0)
                heatValue.set(heatValue.get()[:21])
            else:
                pass
        heatValue=tk.StringVar() 
        heatValue.trace('w', lambda *args: checkHeat(heatValue))
        heat_entry = tk.Entry(self, bg="white", textvariable=heatValue)
        heat_entry.place(relx=.02, rely=.38, relwidth=.09, relheight=.03)

        # --- AC Entry --- #
        crm_lbl(self, tk, "  Air Conditioning:", 'groove', 'w', 'white', 'black', '.11', '.35', '.09', '.03')

        def checkAC(ACValue):
            if len(ACValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Air Conditioning cannot exceed 21 characters in length.', 0)
                ACValue.set(ACValue.get()[:21])
            else:
                pass
        ACValue=tk.StringVar() 
        ACValue.trace('w', lambda *args: checkAC(ACValue))
        AC_entry = tk.Entry(self, bg="white", textvariable=ACValue)
        AC_entry.place(relx=.11, rely=.38, relwidth=.09, relheight=.03)
        
        # --- Parking Entry --- #
        crm_lbl(self, tk, "  Parking:", 'groove', 'w', 'white', 'black', '.20', '.35', '.09', '.03')

        def checkPark(parkValue):
            if len(parkValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Parking cannot exceed 21 characters in length.', 0)
                parkValue.set(parkValue.get()[:21])
            else:
                pass
        parkValue=tk.StringVar() 
        parkValue.trace('w', lambda *args: checkPark(parkValue))
        parking_entry = tk.Entry(self, bg="white", textvariable=parkValue)
        parking_entry.place(relx=.20, rely=.38, relwidth=.09, relheight=.03)

        # --- Basement Entry --- #
        crm_lbl(self, tk, "  Basement:", 'groove', 'w', 'white', 'black', '.29', '.35', '.09', '.03')

        def checkBase(baseValue):
            if len(baseValue.get()) > 21:
                Mbox(ctypes,'Too Long', 'Basement cannot exceed 21 characters in length.', 0)
                baseValue.set(baseValue.get()[:21])
            else:
                pass
        baseValue=tk.StringVar() 
        baseValue.trace('w', lambda *args: checkBase(baseValue))
        base_entry = tk.Entry(self, bg="white", textvariable=baseValue)
        base_entry.place(relx=.29, rely=.38, relwidth=.09, relheight=.03)
        
        # --- Check Write Ups --- #
        def check_writeups():
            h_write_v      = writeup_entry.get('1.0', tk.END)
            inc_write_v    = inc_entry.get('1.0', tk.END)
            up_write_v     = updates_entry.get('1.0', tk.END)
            neighb_write_v = neighb_writeup_entry.get('1.0', tk.END)
            if len(h_write_v) > 301:
                Mbox(ctypes,'House Write Up Is Too Long', 'House Write Up cannot exceed 300 characters in length and will be trimmed down automatically', 0)
                writeup_entry.delete('1.0', tk.END)
                writeup_entry.insert('1.0', h_write_v[0:300]) 
            if len(inc_write_v) > 126:
                Mbox(ctypes,'Inclusions Write Up Is Too Long', 'Inclusions Write Up cannot exceed 125 characters in length and will be trimmed down automatically', 0)
                inc_entry.delete('1.0', tk.END)
                inc_entry.insert('1.0', inc_write_v[0:125])
            if len(up_write_v) > 126:
                Mbox(ctypes,'Updates Write Up Is Too Long', 'Updates Write Up cannot exceed 125 characters in length and will be trimmed down automatically', 0)
                updates_entry.delete('1.0', tk.END)
                updates_entry.insert('1.0', up_write_v[0:125])   
            if len(neighb_write_v) > 301:
                Mbox(ctypes,'Neighbourhood Write Up Is Too Long', 'Neighbourhood Write Up cannot exceed 300 characters in length and will be trimmed down automatically', 0)
                neighb_writeup_entry.delete('1.0', tk.END)
                neighb_writeup_entry.insert('1.0', neighb_write_v[0:300])
            else:
                pass

        # --- House Write Up --- #
        crm_lbl(self, tk, "  House Write Up:", 'groove', 'w', 'white', 'black', '.02', '.41', '.36', '.03')
        h_write_v = tk.StringVar()
        writeup_entry = tk.Text(self, bg="white")
        writeup_entry.place(relx=.02, rely=.44, relwidth=.36, relheight=.07)
        
        # Inclusions 
        crm_lbl(self, tk, "  Inclusions:", 'groove', 'w', 'white', 'black', '.02', '.51', '.36', '.03')
        inc_write_v = tk.StringVar()
        inc_entry = tk.Text(self, bg="white")
        inc_entry.place(relx=.02, rely=.54, relwidth=.36, relheight=.04)
        
        # Updates
        crm_lbl(self, tk, "  Updates:", 'groove', 'w', 'white', 'black', '.02', '.58', '.36', '.03')
        up_write_v = tk.StringVar()
        updates_entry = tk.Text(self, bg="white")
        updates_entry.place(relx=.02, rely=.61, relwidth=.36, relheight=.04)                          
        
        # Neighbourhood Write Up
        crm_lbl(self, tk, "  Neighbourhood:", 'groove', 'w', 'white', 'black', '.02', '.65', '.36', '.03')
        neighb_write_v = tk.StringVar()
        neighb_writeup_entry = tk.Text(self, bg="white")
        neighb_writeup_entry.place(relx=.02, rely=.68, relwidth=.36, relheight=.07) 

        # --------- Images ------------------ #
        # Open File Explorer Buttons
        def open_file1():
            openfile1(filedialog, imagenamelbl_1, ImageTk, PIL, Image)

        def open_file2():
            openfile2(filedialog, imagenamelbl_2, ImageTk, PIL, Image)

        def open_file3():
            openfile3(filedialog, imagenamelbl_3, ImageTk, PIL, Image)

        def open_file4():
            openfile4(filedialog, imagenamelbl_4, ImageTk, PIL, Image)

        def open_file5():
            openfile5(filedialog, imagenamelbl_5, ImageTk, PIL, Image)

        def open_file6():
            openfile6(filedialog, imagenamelbl_6, ImageTk, PIL, Image)

        def open_file7():
            openfile7(filedialog, imagenamelbl_7, ImageTk, PIL, Image)

        def open_file8():
            openfile8(filedialog, imagenamelbl_8, ImageTk, PIL, Image)

        def open_file9():
            openfile9(filedialog, imagenamelbl_9, ImageTk, PIL, Image)

        def open_file10():
            openfile10(filedialog, imagenamelbl_10, ImageTk, PIL, Image)

        def open_file11():
            openfile11(filedialog, imagenamelbl_11, ImageTk, PIL, Image)

        imagenamelbl_1 = tk.Label(self, text="   Select Image 1:", bg = 'white', fg = 'black')
        imagenamelbl_1.place(relx=.385, rely=.14, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file1, .485, .14, .025, .03)
        
        imagenamelbl_2 = tk.Label(self, text="   Select Image 2:", bg = 'white', fg = 'black')
        imagenamelbl_2.place(relx=.385, rely=.17, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file2, .485, .17, .025, .03)

        imagenamelbl_3 = tk.Label(self, text="   Select Image 3:", bg = 'white', fg = 'black')
        imagenamelbl_3.place(relx=.385, rely=.20, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file3, .485, .20, .025, .03)
        
        imagenamelbl_4 = tk.Label(self, text="   Select Image 4:", bg = 'white', fg = 'black')
        imagenamelbl_4.place(relx=.385, rely=.23, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file4, .485, .23, .025, .03)
        
        imagenamelbl_5 = tk.Label(self, text="   Select Image 5:", bg = 'white', fg = 'black')
        imagenamelbl_5.place(relx=.385, rely=.26, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file5, .485, .26, .025, .03)
        
        imagenamelbl_6 = tk.Label(self, text="   Select Image 6:", bg = 'white', fg = 'black')
        imagenamelbl_6.place(relx=.385, rely=.29, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file6, .485, .29, .025, .03)
        
        imagenamelbl_7 = tk.Label(self, text="   Select Image 7:", bg = 'white', fg = 'black')
        imagenamelbl_7.place(relx=.385, rely=.32, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file7, .485, .32, .025, .03)
        
        imagenamelbl_8 = tk.Label(self, text="   Select Image 8:", bg = 'white', fg = 'black')
        imagenamelbl_8.place(relx=.385, rely=.35, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file8, .485, .35, .025, .03)
        
        imagenamelbl_9 = tk.Label(self, text="   Select Image 9:", bg = 'white', fg = 'black')
        imagenamelbl_9.place(relx=.385, rely=.38, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file9, .485, .38, .025, .03)
        
        imagenamelbl_10 = tk.Label(self, text="   Select Image 10:", bg = 'white', fg = 'black')
        imagenamelbl_10.place(relx=.385, rely=.41, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file10, .485, .41, .025, .03)

        imagenamelbl_11 = tk.Label(self, text="   Select Image 11:", bg = 'white', fg = 'black')
        imagenamelbl_11.place(relx=.385, rely=.44, relwidth=.10, relheight=.03)
        button_ttk_reg(self, ttk, 'white', "---", open_file11, .485, .44, .025, .03)

        # ----- Preview PDF ----- #
        # Outside PDF
        crm_lbl(self, tk, '', 'groove', 'w', 'white', 'black', '.53', '.17', '.45', '.30')
        # Front
        crm_lbl(self, tk, 'Front', 'flat', 'center', 'black', 'white', '.755', '.14', '.225', '.03')
        # Images
        crm_lbl(self, tk, '1', 'groove', 'center', 'white', 'black', '.760', '.18', '.215', '.1')
        crm_lbl(self, tk, '2', 'groove', 'center', 'white', 'black', '.760', '.28', '.1075', '.1')
        crm_lbl(self, tk, '3', 'groove', 'center', 'white', 'black', '.8675', '.28', '.1075', '.1')
        # Back
        crm_lbl(self, tk, 'Back', 'flat', 'center', 'black', 'white', '.53', '.14', '.225', '.03')
        # Images
        crm_lbl(self, tk, '4', 'groove', 'center', 'white', 'black', '.535', '.18', '.215', '.1')
        crm_lbl(self, tk, '5', 'groove', 'center', 'white', 'black', '.535', '.28', '.1075', '.1')
        crm_lbl(self, tk, '6', 'groove', 'center', 'white', 'black', '.6425', '.28', '.1075', '.1')

        # Inside PDF
        crm_lbl(self, tk, '', 'groove', 'w', 'white', 'black', '.53', '.50', '.45', '.30')
        # Right
        crm_lbl(self, tk, 'Inside Left', 'flat', 'center', 'black', 'white', '.53', '.47', '.225', '.03')
        # Images
        crm_lbl(self, tk, '7', 'groove', 'center', 'white', 'black', '.760', '.51', '.215', '.1')
        crm_lbl(self, tk, '8', 'groove', 'center', 'white', 'black', '.8675', '.61', '.1075', '.1')
        # Left
        crm_lbl(self, tk, 'Inside Right', 'flat', 'center', 'black', 'white', '.755', '.47', '.225', '.03')
        # Images
        crm_lbl(self, tk, '9', 'groove', 'center', 'white', 'black', '.535', '.59', '.1075', '.1')
        crm_lbl(self, tk, '10', 'groove', 'center', 'white', 'black', '.6425', '.59', '.1075', '.1')
        crm_lbl(self, tk, '11', 'groove', 'center', 'white', 'black', '.535', '.69', '.215', '.1')

        # -----  Create PDF - March 2020 ------ #
        featuresheet_pg_1 = "pdfs/featuresheet_pg1.pdf"
        featuresheet_pg_2 = "pdfs/featuresheet_pg2.pdf"
        
        # Royal Lepage Logo
        rlp_logo1  = ""
        rlp_logo2  = ""
        # Left margin on PDF
        pdf_margin = 0

        # Make PDF
        def make_feature_sheet():
            if __name__ == '__main__':
                # Entry Gets 
                address_entry1        = address_entry.get()
                neighb_entry1         = neighb_entry.get()
                price_entry1          = price_entry.get()
                mls_entry1            = mls_entry.get()
                bedrooms_entry1       = bedrooms_entry.get()
                bathrooms_entry1      = bathrooms_entry.get()
                parking_entry1        = parking_entry.get()
                base_entry1           = base_entry.get()
                AC_entry1             = AC_entry.get()
                style_entry1          = style_entry.get()
                taxes_entry1          = taxes_entry.get()
                type_entry1           = type_entry.get()
                heat_entry1           = heat_entry.get()

                # ------- Instantiate Canvas ------- #
                c = canvas.Canvas(featuresheet_pg_1, pagesize=SEVENTENELEVEN)
                # Instantiate getSampleStyleSheet
                style = getSampleStyleSheet()
                # Style
                w_style = ParagraphStyle('house_sty', fontName='MrsEaves_Roman', fontSize=17, leading=21)

                # ------- FRONT & BACK ------ #
                # --- Images --- #
                # Img 1
                pic_1 = openfile1.selected_img
                c.drawImage(pic_1, 8.5*inch, 5.33*inch, width=8.5*inch, height=5.67*inch)
                # Img 2
                pic_2 = openfile2.selected_img
                c.drawImage(pic_2, 8.5*inch, 2.5*inch, width=4.25*inch, height=2.83*inch)
                # Img 3
                pic_3 = openfile3.selected_img
                c.drawImage(pic_3, 12.75*inch, 2.5*inch, width=4.25*inch, height=2.83*inch)
                # Img 4
                pic_4 = openfile4.selected_img
                c.drawImage(pic_4, 0*inch, 5.33*inch, width=8.5*inch, height=5.67*inch)
                # Img 5
                pic_5 = openfile5.selected_img
                c.drawImage(pic_5, 0*inch, 2.5*inch, width=4.25*inch, height=2.83*inch)
                # Img 6
                pic_6 = openfile6.selected_img
                c.drawImage(pic_6, 4.25*inch, 2.5*inch, width=4.25*inch, height=2.83*inch)
                # Front RLP Logo
                rlp_logo_front = "images/rlp_logo.jpg"
                c.drawImage(rlp_logo_front, 15.3747*inch, .2731*inch, width=1.3626*inch, height=0.7585*inch)
                # Back RLP Logo
                rlp_logo_back = "images/rlp_logo.jpg"
                c.drawImage(rlp_logo_back, .275*inch, .2731*inch, width=1.8579*inch, height=1.0253*inch)

                # --- Front --- #
                # Address
                address_1 = c.beginText()
                address_1.setTextOrigin(8.76*inch, 1.7928*inch)
                address_1.setFont("Gotham-Bold-Regular", 34)
                address_1.setFillColor(colors.black)
                address_1.textLine(text=address_entry1)
                c.drawText(address_1)
                # Neighbourhood
                neighb_1 = c.beginText()
                neighb_1.setTextOrigin(8.76*inch, 1.27*inch)
                neighb_1.setFont("Gotham-Light", 26)
                neighb_1.setFillColor(colors.black)
                neighb_1.textLine(text=neighb_entry1)
                c.drawText(neighb_1)
                # # Price 1
                price_1 = c.beginText()
                price_1.setTextOrigin(8.76*inch, .7269*inch)
                price_1.setFont("Gotham-Light", 26)
                price_1.setFillColor(colors.black)
                price_1.textLine(text='$'+price_entry1)
                c.drawText(price_1)
                # # MLS #
                mls_1 = c.beginText()
                mls_1.setTextOrigin(8.76*inch, .2731*inch)
                mls_1.setFont("Gotham-Light", 18)
                mls_1.setFillColor(colors.black)
                mls_1.textLine(text='MLS#'+mls_entry1)
                c.drawText(mls_1)
                # # J&K
                jk_1 = c.beginText()
                jk_1.setTextOrigin(12.5471*inch, .7736*inch)
                jk_1.setFont("Gotham-Bold-Regular", 26)
                jk_1.setFillColor(colors.black)
                jk_1.textLine(text='JEFF & KATHY')
                c.drawText(jk_1)
                # # MCVEIGH
                mcv_1 = c.beginText()
                mcv_1.setTextOrigin(12.5471*inch, .2731*inch)
                mcv_1.setFont("Gotham-Bold-Regular", 40)
                mcv_1.setFillColor(colors.black)
                mcv_1.textLine(text='MCVEIGH')
                c.drawText(mcv_1)

                # # ---- Back ---- #
                # Kathy
                kathymcv_1 = c.beginText()
                kathymcv_1.setTextOrigin(2.458*inch, 1.1146*inch)
                kathymcv_1.setFont('Gotham-Narrow-Medium', 17.43)
                kathymcv_1.setFillColor(colors.black)
                kathymcv_1.textLine(text='Kathy McVeigh')
                c.drawText(kathymcv_1)
                # k-phone
                k_phone = c.beginText()
                k_phone.setTextOrigin(2.458*inch, .849*inch)
                k_phone.setFont('Gotham-Narrow-Medium', 17.43)
                k_phone.setFillColor(colors.black)
                k_phone.textLine(text='613-859-7494')
                c.drawText(k_phone)
                # k-email
                k_email = c.beginText()
                k_email.setTextOrigin(2.458*inch, .563*inch)
                k_email.setFont('Gotham-Narrow-Medium', 17.43)
                k_email.setFillColor(colors.black)
                k_email.textLine(text='kathy@themcveighs.com')
                c.drawText(k_email)
                # k-web
                k_web = c.beginText()
                k_web.setTextOrigin(2.458*inch, .288*inch)
                k_web.setFont('Gotham-Narrow-Medium', 17.43)
                k_web.setFillColor(colors.black)
                k_web.textLine(text='mcveighrealty.com')
                c.drawText(k_web)
                # Jeff
                jeffmcv_1 = c.beginText()
                jeffmcv_1.setTextOrigin(5.398*inch, 1.1146*inch)
                jeffmcv_1.setFont('Gotham-Narrow-Medium', 17.43)
                jeffmcv_1.setFillColor(colors.black)
                jeffmcv_1.textLine(text='Jeff McVeigh')
                c.drawText(jeffmcv_1)
                # j-phone
                j_phone = c.beginText()
                j_phone.setTextOrigin(5.398*inch, .849*inch)
                j_phone.setFont('Gotham-Narrow-Medium', 17.43)
                j_phone.setFillColor(colors.black)
                j_phone.textLine(text='613-720-5150')
                c.drawText(j_phone)
                # j-email
                j_email = c.beginText()
                j_email.setTextOrigin(5.398*inch, .563*inch)
                j_email.setFont('Gotham-Narrow-Medium', 17.43)
                j_email.setFillColor(colors.black)
                j_email.textLine(text='jeff@themcveighs.com')
                c.drawText(j_email)
                # j-web
                j_web = c.beginText()
                j_web.setTextOrigin(5.398*inch, .288*inch)
                j_web.setFont('Gotham-Narrow-Medium', 17.43)
                j_web.setFillColor(colors.black)
                j_web.textLine(text='mcveighrealty.com')
                c.drawText(j_web)
                # # End Canvas
                c.showPage()
                # Create the PDF
                c.save()


                # ------- INSIDE ------ #
                c = canvas.Canvas(featuresheet_pg_2, pagesize=SEVENTENELEVEN)

                #--- Images --- #
                # img 7
                pic_7 = openfile7.selected_img
                c.drawImage(pic_7, 8.5*inch, 7.33*inch, width=8.5*inch, height=3.67*inch)
                # Img 8
                pic_8 = openfile8.selected_img
                c.drawImage(pic_8, 12.75*inch, 4.5*inch, width=4.25*inch, height=2.83*inch)
                # Img 9
                pic_9 = openfile9.selected_img
                c.drawImage(pic_9, 0*inch, 4.45*inch, width=4.25*inch, height=2.83*inch)
                # Img 10
                pic_10 = openfile10.selected_img
                c.drawImage(pic_10, 4.25*inch, 4.45*inch, width=4.25*inch, height=2.83*inch)
                # Img 11
                pic_11 = openfile11.selected_img
                c.drawImage(pic_11, 0*inch, 0*inch, width=8.5*inch, height=4.45*inch)
                
                # --- Inside Left --- #
                # address 2
                address_2 = c.beginText()
                address_2.setTextOrigin(.25*inch, 10.4225*inch)
                address_2.setFont('Gotham-Narrow-Medium', 28)
                address_2.setFillColor(colors.black)
                address_2.textLine(text=address_entry1)
                c.drawText(address_2)
                # Neighbourhood 2
                neighb_2 = c.beginText()
                neighb_2.setTextOrigin(.25*inch, 10.0211*inch)
                neighb_2.setFont('Gotham-Narrow-Medium', 18)
                neighb_2.setFillColor(colors.black)
                neighb_2.textLine(text=neighb_entry1)
                c.drawText(neighb_2)
                # Bed & Bath
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(.25*inch, 9.5838*inch)
                bed_bath.setFont('Gotham-Narrow-Medium', 19)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text= bedrooms_entry1 + ' Bed | '+ bathrooms_entry1 +' Bath')
                c.drawText(bed_bath)
                # Price 2
                price_2 = c.beginText()
                price_2.setTextOrigin(.25*inch, 9.1501*inch)
                price_2.setFont('Gotham-Narrow-Medium', 19)
                price_2.setFillColor(colors.black)
                price_2.textLine(text= '$'+price_entry1)
                c.drawText(price_2)

                # House Write Up
                # Instantiate Text
                h_write_v = writeup_entry.get('1.0', tk.END)
                house_p_1 = Paragraph(h_write_v, style=w_style)
                # Instantiate Flowable List
                house_flow_1=[]
                house_flow_1.append(house_p_1)
                # Instantiate Frame
                house_frame_1 = Frame(.25*inch, 7.5864*inch, 8*inch, 1.4913*inch, leftPadding =0*inch, showBoundary=0)
                # Fill Frame
                house_frame_1.addFromList(house_flow_1, c)

                # --- Inside Right --- #

                # Property Details
                # Property Details Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 6.9511*inch)
                bed_bath.setFont('Gotham-Narrow-Medium', 19)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Property Details')
                c.drawText(bed_bath)

                # Type Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 6.5802*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Type')
                c.drawText(bed_bath)
                # Type Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 6.5802*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text=type_entry1)
                c.drawText(bed_bath)

                # Style Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 6.2791*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Style')
                c.drawText(bed_bath)
                # Style Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 6.2791*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text=style_entry1)
                c.drawText(bed_bath)

                # Taxes Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 5.978*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Taxes')
                c.drawText(bed_bath)
                # Taxes Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 5.978*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='$'+taxes_entry1)
                c.drawText(bed_bath)

                # Heat/Fuel Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 5.6698*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Heat/Fuel')
                c.drawText(bed_bath)
                # Heat/Fuel Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 5.6698*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text=heat_entry1)
                c.drawText(bed_bath)

                # Air Conditioning Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 5.3616*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Air Conditioning')
                c.drawText(bed_bath)
                # Air Conditioning Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 5.3616*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text=AC_entry1)
                c.drawText(bed_bath)

                # Parking Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 5.0605*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Parking')
                c.drawText(bed_bath)
                # Parking Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 5.0605*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text=parking_entry1)
                c.drawText(bed_bath)

                # Basement Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 4.7451*inch)
                bed_bath.setFont('Gotham-Narrow-Bold', 14)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Basement')
                c.drawText(bed_bath)
                # Basement Value
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(10.7648*inch, 4.7451*inch)
                bed_bath.setFont('MrsEaves_Roman', 17)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text=base_entry1)
                c.drawText(bed_bath)

                # Inclusions Write Up
                # Inclusion Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 3.9372*inch)
                bed_bath.setFont('Gotham-Narrow-Medium', 19)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Inclusions')
                c.drawText(bed_bath)
                # Instantiate Write Up Text
                inc_write_v = inc_entry.get('1.0', tk.END)
                inc_p_1 = Paragraph(inc_write_v, style=w_style)
                # Instantiate Flowable List
                inc_flow_1=[]
                inc_flow_1.append(inc_p_1)
                # Instantiate Frame
                inc_frame_1 = Frame(8.75*inch, 2.4918*inch, 3.847*inch, 1.373*inch, leftPadding =0*inch, showBoundary=0)
                # Fill Frame
                inc_frame_1.addFromList(inc_flow_1, c)

                # Updates Write Up
                # Updates Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(8.75*inch, 2.0644*inch)
                bed_bath.setFont('Gotham-Narrow-Medium', 19)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Updates')
                c.drawText(bed_bath)
                # Instantiate Update Text
                up_write_v = updates_entry.get('1.0', tk.END)
                up_p_1 = Paragraph(up_write_v, style=w_style)
                # Instantiate Flowable List
                up_flow_1=[]
                up_flow_1.append(up_p_1)
                # Instantiate Frame
                up_frame_1 = Frame(8.75*inch, .619*inch, 3.847*inch, 1.373*inch, leftPadding=0*inch, showBoundary=0)
                # Fill Frame
                up_frame_1.addFromList(up_flow_1, c)

                # Neighbourhood Write Up 
                # Updates Label
                bed_bath = c.beginText()
                bed_bath.setTextOrigin(12.75*inch, 3.9372*inch)
                bed_bath.setFont('Gotham-Narrow-Medium', 19)
                bed_bath.setFillColor(colors.black)
                bed_bath.textLine(text='Neighbourhood')
                c.drawText(bed_bath)
                # Instantiate Text
                neighb_write_v = neighb_writeup_entry.get('1.0', tk.END)
                neighb_p_1 = Paragraph(neighb_write_v, style=w_style)
                # Instantiate Flowable List
                neighb_flow_1=[]
                neighb_flow_1.append(neighb_p_1)
                # Instantiate Frame
                neighb_frame_1 = Frame(12.75*inch, .619*inch, 3.451*inch, 3.2458*inch, leftPadding =0*inch, showBoundary=0)
                # Fill Frame
                neighb_frame_1.addFromList(neighb_flow_1, c)

                # End This Canvas
                c.showPage()
                # Create the PDF
                c.save()

                pdf_merger = PdfFileMerger()
                pdf_merger.merge(position = 0, fileobj = featuresheet_pg_1, pages = (0,1)) 
                pdf_merger.merge(position = 1, fileobj = featuresheet_pg_2, pages = (0,1))

                save_pdf_as = filedialog.asksaveasfilename(title = "Save Listing Presentation", initialdir = "d:", defaultextension = ".pdf")

                pdf_merger.write(fileobj = save_pdf_as)

                # make_feature_sheet()

                # Draw PDF
                # draw_featuresheet(featuresheet_pg_1, featuresheet_pg_2,

                #         address_entry1, neighb_entry1, price_entry1, mls_entry1, bedrooms_entry1, bathrooms_entry1, 
                #         writeup_entry, inc_entry, updates_entry, neighb_writeup_entry,

                #         getSampleStyleSheet, ParagraphStyle, Paragraph, pdf_margin, canvas, SEVENTENELEVEN, inch, PdfFileMerger, filedialog)

                # Clear Forms - ***** FIX THIS
                # prez_forms = (clientnameentry1, clientnameentry2, addressentry, neighbentry)
                # clear_forms(self, prez_forms)
                
                # Change Back image Label to blank - ***** FIX THIS
                # label_config(imagenamelbl, "   Select Image:")

                # Success message
                Mbox(ctypes,'Success', 'The New Feature Sheet Has Been Created', 0)   

        # Create Feature Sheet Button
        sheet_button_style = ttk.Style()
        sheet_button_style.configure('Sheet.TButton', background='yellow', foreground='black', relief="flat", padding=0, border=0)
        sheet_button = ttk.Button(self, text="Create Feature Sheet", style="Sheet.TButton", command = lambda: [check_writeups(), make_feature_sheet()])
        sheet_button.place(relx=.385, rely=.68, relwidth=.125, relheight=.07)

app = crmapp()
app.mainloop()