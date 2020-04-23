class DropMenu():
  def __init__(self, name, tk, choice, options, x, y, w, h):
    self.name = name
    self.tk = tk
    self.choice = choice
    self.options = options
    self.x = x
    self.y = y
    self.w = w
    self.h = h

    def get_name():
      return self.name

    def get_tk():
      return self.tk
    
    def get_choice():
      return self.choice

    def get_options():
      return self.options

    def get_x():
      return self.x

    def get_y():
      return self.y

    def get_w():
      return self.w

    def get_h():
      return self.h

    self.name = self.tk.OptionMenu(self, self.choice, self.options, command= lambda x: changebackground(self.choice.get()))
    self.name.config(bg="white", foreground="black", activeforeground="black", activebackground="white", borderwidth=0, relief="flat", bd=0)        
    self.name['menu'].config(bg="white", fg="black", activebackground="white", activeforeground="black", borderwidth=0, relief="flat", bd=0)
    self.name.place(relx=self.x, rely=self.y, relwidth=self.w, relheight=self.h)

# ttk Nav Button
def button_ttk_nav(self, ttk, ttk_btn_text, controller, showpage, crm_btn_x, crm_btn_y, crm_btn_w, crm_btn_h ):
      ttk_btn_style = ttk.Style()
      ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)
      #ttk_btn_style.configure('Nav.TButton.Label', background='white', foreground='black', relief="flat", padding=0, border=0, anchor="middle", font="helvetica 9", highlightcolor="red" )

      ttk_button = ttk.Button(self, text= ttk_btn_text, style="Nav.TButton", command=lambda: controller.show_frame(showpage))
      ttk_button.place(relx=crm_btn_x, rely=crm_btn_y, relwidth=crm_btn_w, relheight=crm_btn_h)

# ttk Regular Button
def button_ttk_reg(self, ttk, bg, ttk_btn_text, reg_cmd, crm_btn_x, crm_btn_y, crm_btn_w, crm_btn_h ):
      ttk_btn_style = ttk.Style()
      ttk_btn_style.configure('Reg.TButton', background=bg, foreground='black', relief="flat", padding=0, border=0)

      ttk_button = ttk.Button(self, text= ttk_btn_text, style="Reg.TButton", command=reg_cmd)
      ttk_button.place(relx=crm_btn_x, rely=crm_btn_y, relwidth=crm_btn_w, relheight=crm_btn_h)

# ttk Two Command Button
def double_btn(self, ttk, ttk_btn_text, command_1, command_2 ):
      ttk_btn_style = ttk.Style()
      ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)

      ttk_2xbutton = tk.Button(self, text=ttk_btn_text, style="Nav.TButton", command = lambda: [command_1(), command_2()])
      ttk_2xbutton.place(relx=crm_btn_x, rely=crm_btn_y, relwidth=crm_btn_w, relheight=crm_btn_h)

# ttk ?? Button
def crm_btn(self, ttk, crm_btn_text, entry_1, crm_btn_cmd, crm_btn_x, crm_btn_y, crm_btn_w, crm_btn_h):
      crm_btn_name = ttk.Button(self, text= crm_btn_text, command= lambda entry_1=entry_1: crm_btn_cmd)
      crm_btn_name.place(relx=crm_btn_x, rely=crm_btn_y, relwidth=crm_btn_w, relheight=crm_btn_h)

# Pop-up Message Box
def Mbox(ctypes, title, text, style):
      return ctypes.windll.user32.MessageBoxW(0, text, title, style)

# Tkinter Label
def crm_lbl(self, tk, crm_lbl_text, crm_lbl_r, crm_lbl_a, crm_lbl_bg, crm_lbl_fg, crm_lbl_x, crm_lbl_y, crm_lbl_w, crm_lbl_h):
      crm_lbl_name = tk.Label(self, text=crm_lbl_text, relief=crm_lbl_r, anchor=crm_lbl_a, bg = crm_lbl_bg, fg = crm_lbl_fg)
      crm_lbl_name.place(relx=crm_lbl_x, rely=crm_lbl_y, relwidth=crm_lbl_w, relheight=crm_lbl_h)

# Tkinter Label With Image BG
def crm_lbl_img(self, tk, crm_lbl_text, crm_lbl_r, crm_lbl_a, lbl_img, crm_lbl_bg, crm_lbl_fg, crm_lbl_x, crm_lbl_y, crm_lbl_w, crm_lbl_h):
      crm_lbl_name = tk.Label(self, text=crm_lbl_text, relief=crm_lbl_r, anchor=crm_lbl_a, image=lbl_img, bg = crm_lbl_bg, fg = crm_lbl_fg)
      crm_lbl_name.place(relx=crm_lbl_x, rely=crm_lbl_y, relwidth=crm_lbl_w, relheight=crm_lbl_h)

# Creat a tk.Entry
def crm_entry(self, tk, entry_get, crm_entry_x, crm_entry_y, crm_entry_w, crm_entry_h):
      crm_entry_name = tk.Entry(self, textvariable= entry_get, bg="white")
      crm_entry_name.place(relx=crm_entry_x, rely=crm_entry_y, relwidth=crm_entry_w, relheight=crm_entry_h)

# Clear a list of tk.Entrys
def clear_forms(self, forms):
      for i in forms:
            i.delete(0, 'end')

# Print contents of a tk.Entry
def submit(crmentry):
      print(crmentry.get())

# Tkinter Option Menu
def crm_opt_menu(self, crmoptmenu, tk, choice, menu_opts, men_relx, men_rely, men_w, men_h):
      # choice = tk.StringVar()
      crmoptmenu = tk.OptionMenu(self, choice, *menu_opts, command= lambda x: lbmenubg(clicked1.get()))
      crmoptmenu.config(bg="white", foreground="black", activeforeground="black", activebackground="white", borderwidth=0, relief="flat", bd=0)        
      crmoptmenu['menu'].config(bg="white", fg="black", activebackground="white", activeforeground="black", borderwidth=0, relief="flat", bd=0)
      crmoptmenu.place(relx=men_relx, rely=men_rely, relwidth=men_w, relheight=men_h)

# Open file eplorer for file opening                
def openfile(filedialog, imagenamelbl, ImageTk, PIL, Image):
      openfile.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select and Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
      imagenamelbl.config(text = "    Image:  " + openfile.selected_img )
      openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile.selected_img))

# Configure Labels
def label_config(label_name, config_text):
      label_name.configure(text=config_text)

# -----  Create PDF - Non Flowable - March 2020 ------ #   
def draw_pdf(prez_page_1, merge_prez_1of2, prez_page_14, merge_prez_2of2, offer_example, listing_agreement, sched_a, wwr, sellers_direction, prez_notes, cliname1, 
                cliname2, prezaddy, prezneighb, rlp_logo, pdf_margin, canvas, letter, inch, PdfFileMerger, filedialog):
        # Front Page
        # Create Canvas
        c = canvas.Canvas(prez_page_1, pagesize=letter)
        # Draw black rectangle
        c.setFillColorRGB(0,0,0)
        c.rect(0.75*inch, 10.5*inch, 7*inch, 0.5*inch, fill=1)
        # Adress
        c.setFont("Gotham-Bold-Regular", 37)
        c.drawCentredString(4.25*inch, 9.583*inch, prezaddy)
        # Nieghbourhood
        c.setFont("Gotham-Light", 18)
        c.drawCentredString(4.25*inch, 8.944*inch, prezneighb)
        # House Image
        house_pic = openfile.selected_img
        c.drawImage(house_pic, 0.736*inch, 3.806*inch, width=7.014*inch, height=4.66*inch)
        # Prepared for
        c.setFont("Gotham-Bold-Regular", 40)
        c.drawCentredString(4.25*inch, 3.014*inch, "Prepared for:")
        # Name line 1
        c.setFont("Gotham-Light", 43)
        c.drawCentredString(4.25*inch, 2.181*inch, cliname1)
        # Name line 2
        c.setFont("Gotham-Light", 43)
        c.drawCentredString(4.25*inch, 1.458*inch, cliname2)
        # Draw RLP Logo
        c.drawImage(rlp_logo, 3.653*inch, 0.311*inch, width=1.195*inch, height=0.668*inch)
        # Draw Lines
        c.setLineWidth(2)
        c.setStrokeColorRGB(0,0,0)
        c.line(0.75*inch, 0.677*inch, 3.45*inch, 0.677*inch )  # left line
        c.line(5.036*inch, 0.677*inch, 7.75*inch, 0.677*inch ) # right line   
        # Finish drawing on this page
        c.showPage()
        # Create the PDF
        c.save()

        # -- Page 14 -- #
        # Create the PDF
        c = canvas.Canvas(prez_page_14, pagesize=letter)
        # --- Header --- #
        # McV Difference
        c.setFont("Gotham-Pro-Black", 27)
        c.drawString(pdf_margin*inch, 10.2222*inch, "The McVeigh Difference")
        # House Image
        tiny_houses = "images/tinyhouses.png"
        c.drawImage(tiny_houses, 6.1552*inch, 10.2222*inch, width=1.841*inch, height=.4583*inch)
        # Black Line
        c.setLineWidth(2)
        c.setStrokeColorRGB(0,0,0)
        c.line(0*inch, 10.0139*inch, 8.5*inch, 10.0139*inch )
        # --- Page Content --- #
        # Marketing Strategy
        c.setFont("Gotham-Bold-Regular", 17)
        c.drawString(pdf_margin*inch, 9.0278*inch, "Marketing Strategy")
        # Address
        c.setFont("Gotham-Bold-Regular", 17)
        c.drawString(pdf_margin*inch, 8.458*inch, prezaddy)
        # Line 1
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 7.8472*inch, "Meeting / discussions regarding special features of home and neighbourhood.")
        # Line 2
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 7.2639*inch, "Establish plan for showings and discuss family special needs regarding scheduling i.e. pets,")
        c.drawString(pdf_margin*inch, 7.0556*inch, "children and work schedules.")
        # Line 3
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 6.4583*inch, "Peer to peer marketing and marketing to our database.")
        # Line 4
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 5.875*inch, "Staging suggestions provided for your home.")
        # Line 5
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 5.2639*inch, "Arrange for professional photographer to photograph interior and exterior of property.")
        # Line 6
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 4.6667*inch, "Prepare presentation brochures.")
        # Line 7
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 4.0556*inch, "Install sign - same day as home is put on the MLS system and or install “Coming Soon")
        c.drawString(pdf_margin*inch, 3.8611*inch, "sign.")
        # Line 8
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 3.2778*inch, "Organize and implement web and print media.")
        # Line 9
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 2.6806*inch, "Schedule open house for public and neighbours.")
        # Line 10
        c.setFont("Gotham-Light", 12)
        c.drawString(pdf_margin*inch, 2.0556*inch, "Present offers to sellers as soon as discussed considering market conditions.")
        # Save
        c.showPage()
        c.save()

        pdf_merger = PdfFileMerger()
        pdf_merger.merge(position = 0, fileobj = prez_page_1, pages = (0,1)) 
        pdf_merger.merge(position = 1, fileobj = merge_prez_1of2, pages = (0,12))
        pdf_merger.merge(position = 14, fileobj = prez_page_14, pages = (0,1))
        pdf_merger.merge(position = 15, fileobj = merge_prez_2of2, pages = (0,5))
        pdf_merger.append(fileobj = offer_example, pages = (0,7))
        pdf_merger.append(fileobj = listing_agreement, pages = (0,3))
        pdf_merger.append(fileobj = sched_a, pages = (0,1))
        pdf_merger.append(fileobj = wwr, pages = (0,1))
        pdf_merger.append(fileobj = sellers_direction, pages = (0,1))
        pdf_merger.append(fileobj = prez_notes, pages = (0,2))

        save_pdf_as = filedialog.asksaveasfilename(title = "Save Listing Presentation", initialdir = "G:", defaultextension = ".pdf")

        pdf_merger.write(fileobj = save_pdf_as)


# Feature Sheet Images
def openfile1(filedialog, imagenamelbl_1, ImageTk, PIL, Image):
    openfile1.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_1.config(text = "    Image:  " + openfile1.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile1.selected_img))

def openfile2(filedialog, imagenamelbl_2, ImageTk, PIL, Image):
    openfile2.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_2.config(text = "    Image:  " + openfile2.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile2.selected_img))

def openfile3(filedialog, imagenamelbl_3, ImageTk, PIL, Image):
    openfile3.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_3.config(text = "    Image:  " + openfile3.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile3.selected_img))

def openfile4(filedialog, imagenamelbl_4, ImageTk, PIL, Image):
    openfile4.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_4.config(text = "    Image:  " + openfile4.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile4.selected_img))

def openfile5(filedialog, imagenamelbl_5, ImageTk, PIL, Image):
    openfile5.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_5.config(text = "    Image:  " + openfile5.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile5.selected_img))

def openfile6(filedialog, imagenamelbl_6, ImageTk, PIL, Image):
    openfile6.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_6.config(text = "    Image:  " + openfile6.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile6.selected_img))

def openfile7(filedialog, imagenamelbl_7, ImageTk, PIL, Image):
    openfile7.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_7.config(text = "    Image:  " + openfile7.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile7.selected_img))

def openfile8(filedialog, imagenamelbl_8, ImageTk, PIL, Image):
    openfile8.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_8.config(text = "    Image:  " + openfile8.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile8.selected_img))

def openfile9(filedialog, imagenamelbl_9, ImageTk, PIL, Image):
    openfile9.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_9.config(text = "    Image:  " + openfile9.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile9.selected_img))

def openfile10(filedialog, imagenamelbl_10, ImageTk, PIL, Image):
    openfile10.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_10.config(text = "    Image:  " + openfile10.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile10.selected_img))

def openfile11(filedialog, imagenamelbl_11, ImageTk, PIL, Image):
    openfile11.selected_img = filedialog.askopenfilename(initialdir="G:", title="Select Image", filetypes=(("JPG files", "*.*"),("All files", "*.*")))
    imagenamelbl_11.config(text = "    Image:  " + openfile11.selected_img)
    openedimage = ImageTk.PhotoImage(PIL.Image.open(openfile11.selected_img))

# ------  Create Feature Sheet ------ #   
def draw_featuresheet(featuresheet_pg_1, featuresheet_pg_2,
                    address_entry1, neighb_entry1, price_entry1, mls_entry1, bedrooms_entry1, bathrooms_entry1, 
                    writeup_entry1, inc_entry1, updates_entry1, neighb_writeup_entry1,
 
                    getSampleStyleSheet, ParagraphStyle, Paragraph, pdf_margin, canvas, SEVENTENELEVEN, inch, PdfFileMerger, filedialog):

        # Front & Back
        c = canvas.Canvas(featuresheet_pg_1, pagesize=SEVENTENELEVEN)
        #Img 1
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
        
        style = getSampleStyleSheet()
        address_style = ParagraphStyle('Address',
                                        fontName= "Gotham-Bold-Regular",
                                        fontsize=34,
                                        alignment=0,
                                        beginText=(8.76*inch, 1.7928*inch)
                                        )
        c.Paragraph(address_1, address_style)

        # Adress
        c.setFont("Gotham-Bold-Regular", 34)
        c.drawCenterString(8.76*inch, 1.7928*inch, address_entry1)
        # # Nieghbourhood
        c.setFont("Gotham-Light", 26)
        c.drawCenterSring(8.76*inch, 1.27*inch, neighb_entry1)
        # Price
        c.setFont("Gotham-Light", 26)
        c.drawCenterString(8.76*inch, .7269*inch, price_entry1)
        # MLS #
        c.setFont("Gotham-Light", 18)
        c.drawCenterString(8.76*inch, .2731*inch, 'MLS#'+mls_entry1)
        # JK McVeigh
        c.setFont("Gotham-Light", 25)
        c.drawCenterString(12.5471*inch, .2731*inch, 'JEFF & KATHY')
        # MCVEIGH
        c.setFont("Gotham-Light", 40)
        c.drawCenterString(12.5471*inch, .7736*inch, 'MCVEIGH')
        # # Draw RLP Logo
        c.drawImage(rlp_logo, 15.374*inch, 0.2731*inch, width=1.3681*inch, height=0.7641*inch)
        c.showPage()
        # Create the PDF
        c.save()

        # Inside #
        # Create the PDF
        c = canvas.Canvas(featuresheet_pg_2, pagesize=SEVENTENELEVEN)
        # Draw black rectangle
        # c.setFillColorRGB(0,0,0)
        # c.rect(0.75*inch, 10.5*inch, 7*inch, 0.5*inch, fill=1)
        # Adress
        # c.setFont("Gotham-Bold-Regular", 37)
        # c.drawCentredString(4.25*inch, 9.583*inch, prezaddy)
        # # Nieghbourhood
        # c.setFont("Gotham-Light", 18)
        # c.drawCentredString(4.25*inch, 8.944*inch, prezneighb)
        # Img 1
        pic_7 = openfile7.selected_img
        c.drawImage(pic_7, 8.5*inch, 7.33*inch, width=8.5*inch, height=3.67*inch)
        # Img 2
        pic_8 = openfile8.selected_img
        c.drawImage(pic_8, 12.75*inch, 4.5*inch, width=4.25*inch, height=2.83*inch)
        # # Img 3
        pic_9 = openfile9.selected_img
        c.drawImage(pic_9, 0*inch, 4.45*inch, width=4.25*inch, height=2.83*inch)
        # # Img 4
        pic_10 = openfile10.selected_img
        c.drawImage(pic_10, 4.25*inch, 4.45*inch, width=4.25*inch, height=2.83*inch)
        # # Img 5
        pic_11 = openfile11.selected_img
        c.drawImage(pic_11, 0*inch, 0*inch, width=8.5*inch, height=4.45*inch)
        # # Img 6
        # pic_6 = openfile6.selected_img
        # c.drawImage(pic_6, 4.25*inch, 3.67*inch, width=4.25*inch, height=3.67*inch)
        # # # Draw RLP Logo
        # c.drawImage(rlp_logo, 3.653*inch, 0.311*inch, width=1.195*inch, height=0.668*inch)
        # Draw Lines
        # c.setLineWidth(2)
        # c.setStrokeColorRGB(0,0,0)
        # c.line(0.75*inch, 0.677*inch, 3.45*inch, 0.677*inch )  # left line
        # c.line(5.036*inch, 0.677*inch, 7.75*inch, 0.677*inch ) # right line   
        # Finish drawing on this page
        c.showPage()
        # Create the PDF
        c.save()

        pdf_merger = PdfFileMerger()
        pdf_merger.merge(position = 0, fileobj = featuresheet_pg_1, pages = (0,1)) 
        pdf_merger.merge(position = 1, fileobj = featuresheet_pg_2, pages = (0,1))


        save_pdf_as = filedialog.asksaveasfilename(title = "Save Listing Presentation", initialdir = "d:", defaultextension = ".pdf")

        pdf_merger.write(fileobj = save_pdf_as)


# ----------------- Tree View  ------------------ #
def create_tree(self, contact_tree, tv_columns, tv_headings, tk, ttk, sby_x, sby_y, sby_h, sbx_x, sbx_y, sbx_w, tree_x, tree_y, tree_w, tree_h):

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