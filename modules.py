
# ttk Nav Button
def button_ttk_nav(self, ttk, ttk_btn_text, controller, showpage, crm_btn_x, crm_btn_y, crm_btn_w, crm_btn_h ):
      ttk_btn_style = ttk.Style()
      ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)
      #ttk_btn_style.configure('Nav.TButton.Label', background='white', foreground='black', relief="flat", padding=0, border=0, anchor="middle", font="helvetica 9", highlightcolor="red" )

      ttk_button = ttk.Button(self, text= ttk_btn_text, style="Nav.TButton", command=lambda: controller.show_frame(showpage))
      ttk_button.place(relx=crm_btn_x, rely=crm_btn_y, relwidth=crm_btn_w, relheight=crm_btn_h)

# ttk Regular Button
def button_ttk_reg(self, ttk, ttk_btn_text, reg_cmd, crm_btn_x, crm_btn_y, crm_btn_w, crm_btn_h ):
      ttk_btn_style = ttk.Style()
      ttk_btn_style.configure('Nav.TButton', background='white', foreground='black', relief="flat", padding=0, border=0)

      ttk_button = ttk.Button(self, text= ttk_btn_text, style="Nav.TButton", command=reg_cmd)
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
      crmoptmenu = tk.OptionMenu(self, choice, *menu_opts)
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
      lbl_config.configure(text=config_text)

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

          # -----  Create PDF - Flowable - March 2020 ------ #
          # Create Document Template
          # doc_1 = BaseDocTemplate(self, filename,
          #                         pagesize=defaultPageSize,
          #                         pageTemplates=[],
          #                         showBoundary=0,
          #                         leftMargin=inch,
          #                         rightMargin=inch,
          #                         topMargin=inch,
          #                         bottomMargin=inch,
          #                         allowSplitting=1,
          #                         title=None,
          #                         author=None,
          #                         _pageBreakQuick=1,
          #                         encrypt=None)
          # doc_1.afterInit(self)

          # # Page Templates
          # prez_flowables = ()

          # # Use this after the
          # BaseDocTemplate.afterPage(self)

          # # Add page templates to document
          # doc_1.addPageTemplates(self,pageTemplate1, pageTemplate2, etc)    

          # # Place flowables throughout document
          # doc_1.build(self, prez_flowables, filename=None, canvasmaker = can.Canvas)

          # styles = getSampleStyleSheet()

          # def all_pdf():
          #         prez_page_1  = "prez_page_1.pdf"
          #         prez_page_17 = "prez_page_17.pdf"
          #         # Entry Gets   
          #         cliname1   = clientnameentry1.get()
          #         cliname2   = clientnameentry2.get()
          #         prezaddy   = addressentry.get()
          #         prezneighb = neighbentry.get()
          #         flows_1    =  ()

                  # Prez Page 1 Template (draw the constant elements here)
                  # canv = canvas.Canvas("test_pdf.pdf")
                  # def prez_pg_1(can, doc):
                  #     # Start the thing
                  #     can.saveState()
                  #     # Draw black rectangle
                  #     can.setFillColorRGB(0,0,0)
                  #     can.rect(0.75*inch, 11.5*inch, 7*inch, 0.5*inch, fill=1)
                  #     # Draw RLP Logo
                  #     rlp_logo = "images/rlp_logo.png"
                  #     can.drawImage(rlp_logo, 3.653*inch, 1*inch)
                  #     # Draw Lines
                  #     can.setStrokeColorRGB(0,0,0)
                  #     can.line(0.75*inch, 0.677*inch, 3.45*inch, 0.677*inch ) # left line
                  #     can.line(5.036*inch, 0.677*inch, 10.25*inch, 0.677*inch ) # right line
                  #     # End the thing
                  #     can.restoreState()

          #         # # Prez Regular Page Template (draw the constant elements here)
          #         # def prez_pg_reg(canvas, doc):
          #         #     # start the thing
          #         #     can.saveState()
          #         #     # Draw mcveigh difference

          #         #     # Draw little houses

          #         #     # Draw black line

          #         #     # End the thing
          #         #     can.restoreState()

          #         def go():
          #             doc   = SimpleDocTemplate(prez_page_1)
          #             story = []
          #             style = styles["Normal"]
          #             bogus_text = "This is a test string"
          #             p=Paragraph(bogus_text, style)
          #             doc.build(flows_1, onFirstPage=prez_pg_1)
          #         go()
          # all_pdf()


          # PAGE_HEIGHT=defaultPageSize[1]; PAGE_WIDTH=defaultPageSize[0]
          # styles = getSampleStyleSheet()

          # # platypusfirstpage =
          # Title = "Hello world"
          # pageinfo = "platypus example"
          # def myFirstPage(canvas, doc):
          #     canvas.saveState()
          #     canvas.setFont('Times-Bold',16)
          #     canvas.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-108, Title)
          #     canvas.setFont('Times-Roman',9)
          #     canvas.drawString(inch, 0.75 * inch, "First Page / %s" % pageinfo)
          #     canvas.restoreState()

          # # platypusnextpage =
          # def myLaterPages(canvas, doc):
          #     canvas.saveState()
          #     canvas.setFont('Times-Roman',9)
          #     canvas.drawString(inch, 0.75 * inch, "Page %d %s" % (doc.page, pageinfo))
          #     canvas.restoreState()

          # # platypusgo = 
          # def go():
          #     doc = SimpleDocTemplate("phello.pdf")
          #     Story = [Spacer(1,2*inch)]
          #     style = styles["Normal"]
          #     for i in range(100):
          #         bogustext = ("This is Paragraph number %s.  " % i) *20
          #         p = Paragraph(bogustext, style)
          #         Story.append(p)
          #         Story.append(Spacer(1,0.2*inch))
          #     doc.build(Story, onFirstPage=myFirstPage, onLaterPages=myLaterPages)


          # if __name__=="__main__":
          #     # then do the platypus hello world
          #     for b in platypussetup, platypusfirstpage, platypusnextpage, platypusgo:
          #         b = b.strip()
          #         exec(b+'\n')
          #     go()


