#SubGUI
#FIX DELETE

from settings import MainConfig as c
from MainFiles.Sale_Class import Sale
from tkinter import *
from datetime import datetime as dt
from MainFiles.Daily_Class import DailySales
from NewSale.objects_file_ops import *
class CurrentSales:
    def __init__(self, master):
        pass

class NewSale:
    def __init__(self, dailysale):
        pass
        if len(dailysale.sale_num_dict) != 0:
            self.sale_num = max(dailysale.sale_num_dict)+1
        else:
            self.sale_num = 1
        self.payment_type = '' #cash/credit
        self.dailysale = dailysale
        self.name = ''
        self.phone = ''
        self.address = ''
        self.description = ''
        self.quantity = 0
        self.price = 0
        self.change = 0
        self.total_sale = self.quantity*self.price
        self.t = dt.today()
        self.date_string = '{0}/{1}/{2}'.format(self.t.day,\
                                                            self.t.month,\
                                                            self.t.year)       
        self.subtotal = 0
        self.saleobj = []
    def getsaleobj(self):
        pass


class OptionalInfoGUI:
    def __init__(self, master, newsale):
        Frame(master)
        master.minsize(width = 600, height =600)
        color = '#e0ccff'
        self.newsale = newsale
        master.config(bg=color)
        Label(master, text="Client Information:", font= ("Century Gothic",40, 'bold'), bg=color,fg='black').grid(row=1, column=2, columnspan=3)
        self.name = Label(master, text = 'Name:', font=("Century Gothic",25,'bold'), bg=color, pady=25)
        self.name.grid(row=3,column=0)
        self.e = Text(master, width = 25, height = 1, font=("Century Gothic",25), border=3, highlightbackground=color)
        self.e.focus_set() #Sets focus on the input text area
        self.e.grid(row=3,column=1, sticky=W, columnspan=4)
        self.phone = Label(master, text = 'Phone:', font=("Century Gothic",25,'bold'), bg=color, pady=25)
        self.phone.grid(row=4,column=0)
        self.ph = Text(master, width = 25, height = 1, font=("Century Gothic",25), border=3, highlightbackground=color)
        self.ph.focus_set() #Sets focus on the input text area
        self.ph.grid(row=4,column=1, sticky=W, columnspan=4)
        self.address = Label(master, text = 'Address:', font=("Century Gothic",25,'bold'), bg=color, pady=25)
        self.address.grid(row=5,column=0)
        self.ad = Text(master, width = 25, height = 1, font=("Century Gothic",25), border=3, highlightbackground=color)
        self.ad.focus_set() #Sets focus on the input text area
        self.ad.grid(row=5,column=1, sticky=W, columnspan=4)
        self.des = Label(master, text = 'Remarks:', font=("Century Gothic",25,'bold'), bg=color, pady=25)
        self.des.grid(row=6,column=0)
        self.des = Text(master, width = 25, height = 1, font=("Century Gothic",25), border=3, highlightbackground=color)
        self.des.focus_set() #Sets focus on the input text area
        self.des.grid(row=6,column=1, sticky=W, columnspan=4)
        self.photo1=PhotoImage(file='Images/grey.gif')
        h = 50
        w = 120
        px = 0
        py = 0
        self.bfont = ("Century Gothic",20)
##        self.lace = Button(master,text="\nLace",compound=BOTTOM, command=lambda: self.setdes('lace'))
##        self.lace.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
##        self.lace.grid(row=7, column=1)
##        self.cot = Button(master,text="\nCotton",command=lambda: self.setdes('cotton'), compound=BOTTOM)
##        self.cot.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
##        self.cot.grid(row=7, column=2)
##        self.sat = Button(master,text="\n\nSatin\nChiffon",command=lambda: self.setdes('satin/chiffon'),compound=BOTTOM)
##        self.sat.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
##        self.sat.grid(row=7, column=3)
        h = 50
        w = 400
        self.bfont = ("Century Gothic",35, 'bold')
        self.restart = Button(master,text="\nRestart",command=self.restart_func,compound=BOTTOM)
        self.restart.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        self.restart.grid(row=8, column=1, columnspan=4)
        self.cont = Button(master,text="\nContinue",command = self.cont_func, compound=BOTTOM)
        self.cont.config(image=self.photo1,font=self.bfont,fg='red',height=h, width = w,padx = px, pady=py, highlightbackground=color)
        self.cont.grid(row=9, column=1, columnspan=4)
        self.e.bind("<Tab>", self.focus_next_window)
        self.e.bind("<Shift_L>", self.cont_func)
        self.ph.bind("<Tab>", self.focus_next_window)
        self.ad.bind("<Tab>", self.focus_next_window)
        self.des.bind("<Tab>", self.focus_next_window)
        self.e.bind("<Down>", self.focus_next_window)
        self.ph.bind("<Down>", self.focus_next_window)
        self.ad.bind("<Down>", self.focus_next_window)
        self.des.bind("<Down>", self.focus_next_window)
        self.e.bind("<Return>", self.focus_next_window)
        self.ph.bind("<Return>", self.focus_next_window)
        self.ad.bind("<Return>", self.focus_next_window)
        self.des.bind("<Return>", self.focus_next_window)
        master.focus_set()
##        master.bind("<Control-c>", self.cottonbind)
##        master.bind("<Control-l>", self.lacebind)
##        master.bind("<Control-s>", self.satinbind)
        master.bind("<Triple-Return>",self.enter_key)
        master.bind("<Escape>",self.close_window)
        self.master = master
        self.master.focus_set()

        

    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    def enter_key(self, event):
        self.cont_func()

    def cont_func(self):
        self.newsale.name = self.e.get(1.0,END)
        self.newsale.phone = self.ph.get(1.0,END)
        self.newsale.address = self.ad.get(1.0, END)
        self.newsale.description = self.des.get(1.0, END).split()
        self.master.destroy()
        new = Toplevel()
        #step2
        start = GoodsType(new, self.newsale, 'first')
        
    def restart_func(self):
        self.master.destroy()
        new = Toplevel()
        start_sale(self.newsale, new)

    def restart_key(self, event):
        self.restart_func()
        
    def clear(self, event):
        self.des.delete(1.0, END)

    def close_window(self, event):
        self.master.destroy()


class NumPad:
    def __init__(self, master, NewSale, title):
        #color = c().color
        color = 'light green'
        self.color = color
        self.maintitle = title
        self.newsale = NewSale
        master.config(bg=color)
        self.title = Label(master, text = title, font=("Century Gothic",40,'bold','underline'), bg=color)
        self.title.grid(row=0, columnspan =3)
        self.e = Text(master, width = 11, height = 1, font=("Century Gothic",60,'bold'), border=3,bg=color, highlightbackground=color)
        self.e.focus_set() #Sets focus on the input text area
        self.e.grid(row=1, columnspan = 3)
        #master.attributes("-fullscreen", True)
        self.photo1=PhotoImage(file='Images/grey.gif')
        h = 100
        w = 120
        px = 0
        py = 0
        self.bfont = ("Century Gothic",35,'bold')

        seven = Button(master,text="\n\n7",command=lambda:self.action(7),compound=BOTTOM)
        seven.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        seven.grid(row=2, column=0)
        
        eight = Button(master,text="\n\n8",width=w,command=lambda:self.action(8),compound=BOTTOM)
        eight.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        eight.grid(row=2, column=1)

        nine = Button(master,text="\n\n9",command=lambda:self.action(9),compound=BOTTOM)
        nine.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        nine.grid(row=2, column=2)
        
        four = Button(master,text="\n\n4",command=lambda:self.action(4),compound=BOTTOM)
        four.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        four.grid(row=3, column=0)
        
        five = Button(master,text="\n\n5",command=lambda:self.action(5),compound=BOTTOM)
        five.grid(row=3, column=1)
        five.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)

        six = Button(master,text="\n\n6",command=lambda:self.action(6),compound=BOTTOM)
        six.grid(row=3, column=2)
        six.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)

        
        one = Button(master,text="\n\n1",command=lambda:self.action(1),compound=BOTTOM)
        one.grid(row=4, column=0)
        one.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)

        
        two = Button(master,text="\n\n2",command=lambda:self.action(2),compound=BOTTOM)
        two.grid(row=4, column=1)
        two.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        
        three = Button(master,text="\n\n3",command=lambda:self.action(3),compound=BOTTOM)
        three.grid(row=4, column=2)
        three.config(image=self.photo1,font=self.bfont,height=h, width=w,padx = px, pady=py, highlightbackground=color)
        
        zero = Button(master,text="\n\n0",command=lambda:self.action(0),compound=BOTTOM)
        zero.grid(row=5, column=0)
        zero.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)

        dot = Button(master,text="\n\n.",command=lambda:self.action('.'),compound=BOTTOM)
        dot.grid(row=5, column=1)
        dot.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)


        
        backspace = Button(master, text='\n\nErase', compound=BOTTOM, command=self.erase)
        backspace.grid(row=5, column=2)
        backspace.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)


        submit = Button(master, text='\n\nENTER', compound=BOTTOM, command=self.enter)
        submit.grid(row=6, column=0, columnspan=3)
        submit.config(image=self.photo1,font=self.bfont,height=h, width = 380,padx = px, pady=py, highlightbackground=color)

        master.bind('<Return>', self.enter_event)
        self.master= master
    def action(self,argi): 
      """pressed button's value is inserted into the end of the text area"""
      #self.e.delete(1.0,END)
      self.e.insert(END,argi)

    def erase(self):
        new = self.e.get(1.0,END)
        self.e.delete(1.0,END)
        self.e.insert(1.0, new[:-2])

    def enter(self):
        new = self.e.get(1.0, END)
        newsaleobj = self.newsale
        #step3
        if 'quantity' in self.maintitle.lower():
            try:
                self.newsale.quantity = float(new)
                self.master.destroy()
                new = Toplevel()
                gui = NumPad(new, newsaleobj, 'Enter Price:')
            except ValueError:
                messagebox.showerror('Invalid Input', "Please enter a valid number")
        if 'price' in self.maintitle.lower():
            try:
                self.newsale.price = float(new)
                self.newsale.total_sale = self.newsale.quantity*self.newsale.price
                self.newsale.subtotal += self.newsale.total_sale
                x = Sale(num=self.newsale.sale_num,name=self.newsale.name.strip(), \
                         address=self.newsale.address.strip(), \
                         description=self.newsale.description.strip(),
                         quantity=self.newsale.quantity,\
                        price=self.newsale.price)
                self.newsale.saleobj.append(x)
                self.master.destroy()
                new = Toplevel()
                #step4
                checkout = CheckOut(new, self.newsale)
    ##            gui =NumPad(new, newsaleobj, 'Enter Given:')
            except ValueError:
                messagebox.showerror('Invalid Input', "Please enter a valid number")


    def enter_event(self, event):
        self.enter()
##
class SecondNumPad(NumPad):
    def __init__(self, master, newsale, title, checkout):
        NumPad.__init__(self, master, newsale, title)
        x = Frame(master)
        x.grid(sticky=E)
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        x = int((master.winfo_screenwidth() // 2) * 1.2 )
        y = (master.winfo_screenheight() // 2) - (height // 2)
        master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        master.focus_set()
        #center(master)
        self.checkout = checkout
    def enter(self):
        new = self.e.get(1.0, END)
        newsaleobj = self.newsale
        if 'quantity' in self.maintitle.lower():
            try:
                self.newsale.quantity = float(new)
                self.master.destroy()
                new = Toplevel()
                gui = SecondNumPad(new, newsaleobj, 'Enter Price:', self.checkout)
            except ValueError:
                messagebox.showerror('Invalid Input', "Please enter a valid number")

                
        if 'price' in self.maintitle.lower():
            try:
                
                self.newsale.price = float(new)
                self.newsale.total_sale = self.newsale.quantity*self.newsale.price
                self.newsale.subtotal += self.newsale.total_sale
                self.checkout.add_item('first')
                x = Sale(num=self.newsale.sale_num,name=self.newsale.name.strip(), \
                         address=self.newsale.address.strip(), \
                         description=self.newsale.description.strip(),
                         quantity=self.newsale.quantity,\
                        price=self.newsale.price)
                self.newsale.saleobj.append(x)
                self.master.destroy()
            except ValueError:
                messagebox.showerror('Invalid Input', "Please enter a valid number")

        if 'given' in self.maintitle.lower():
            if new.strip().isnumeric():
                self.newsale.change = float(new) - self.newsale.subtotal
            else:
                self.newsale.change = '-'
            self.master.destroy()
            self.checkout.set_change()

    def enter_event(self, event):
        self.enter()
        

class GoodsType(NumPad):
    def __init__(self, master, NewSale, order, checkout = None):
        color = 'light green'
        self.checkout = checkout
        self.order = order
        self.newsale = NewSale
        master.config(bg=color)
        self.title = Label(master, text = "Goods Type:", font=("Century Gothic",40,'bold','underline'), bg=color)
        self.title.grid(row=0, columnspan =3)
        self.e = Text(master, width = 11, height = 1, font=("Century Gothic",60,'bold'), border=3,bg=color, highlightbackground=color)
        self.e.focus_set() #Sets focus on the input text area
        self.e.grid(row=1, columnspan = 3)
        #master.attributes("-fullscreen", True)
        self.photo1=PhotoImage(file='Images/grey.gif')
        h = 120
        w = 120
        px = 0
        py = 0
        self.bfont = ("Century Gothic",25,'bold')

        seven = Button(master,text="\n\nLace",command=lambda:self.action('Lace'),compound=BOTTOM)
        seven.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        seven.grid(row=2, column=0)
        eight = Button(master,text="\n\nCotton",width=w,command=lambda:self.action('Cotton'),compound=BOTTOM)
        eight.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        eight.grid(row=2, column=1)
        nine = Button(master,text="\nSatin\nChiffon",command=lambda:self.action('Satin/Chiffon'),compound=BOTTOM)
        nine.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        nine.grid(row=2, column=2)
        other = Button(master,text="\n\nOthers",command=lambda:self.action('Other'),compound=BOTTOM)
        other.config(image=self.photo1,font=self.bfont,height=h, width = w,padx = px, pady=py, highlightbackground=color)
        other.grid(row=3, column=0)
        enter = Button(master,text="\n\nContinue",command=self.enter,compound=BOTTOM)
        enter.config(image=self.photo1,font=self.bfont,height=h, width = 240,padx = px, pady=py, highlightbackground=color)
        enter.grid(row=3, column=1, columnspan =2)
        master.bind("<Triple-Return>", self.enter_event)
        master.bind("<Return>", self.enter_event)
        master.bind("<Control-c>", self.cottonbind)
        master.bind("<Control-l>", self.lacebind)
        master.bind("<Control-s>", self.satinbind)
        master.bind("<Control-o>", self.otherbind)
        self.master = master
        master.update_idletasks()
        x = 140
        y = 112
        width = master.winfo_width()
        height = master.winfo_height()
        master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        
    def enter(self):
        new = self.e.get(1.0, END)
        newsaleobj = self.newsale
        self.newsale.description = self.e.get(1.0, END)
        self.master.destroy()
        top = Toplevel()
        if self.order == 'first':
            start = NumPad(top, self.newsale, 'Enter Quantity:')
        if self.order == 'second':
            start = SecondNumPad(top, self.newsale, 'Enter Quantity:', self.checkout)


    def setdes(self,text):
        self.e.delete(0.0, END)
        if text.lower() == 'lace':
            self.e.insert(END, 'Lace')
        if text.lower() == 'cotton':
            self.e.insert(END, 'Cotton')
        if text.lower() == 'satin/chiffon':
            self.e.insert(END, "Satin/Chiffon")
        if text.lower() == 'other':
            self.e.insert(END, "Others")


            
    def enter_event(self, event):
        self.enter()

    def lacebind(self, event):
        self.e.delete(0.0, END)
        self.setdes('lace')
        self.enter()
    def cottonbind(self, event):
        self.e.delete(0.0, END)
        self.setdes('cotton')
        self.enter()
    def satinbind(self, event):
        self.e.delete(0.0, END)
        self.setdes('satin/chiffon')
        self.enter()
    def otherbind(self, event):
        self.e.delete(0.0, END)
        self.setdes('other')
        self.enter()

class CheckOut:
    def __init__(self, master, newsale):
        Frame(master)
        #master.minsize(width = 600, height=600)
        self.command = {}
        self.checkout = self
        color = '#ffe6b3'
        self.newsale = newsale
        master.config(bg=color)
         #master.eval('tk::PlaceWindow {0} center'.format(master.winfo_pathname(master.winfo_id())))
        master.focus_set()
        Label(master, text="Check Out", font= ("Century Gothic",40, 'bold'), bg=color,fg='black').grid(row=1,sticky=W+E, column=0, columnspan=5)
        Label(master, text = 'Sale #: {0}'.format(self.newsale.sale_num), font= ("Century Gothic",15, 'bold'), bg=color,fg='black').grid(row=1,sticky=W+E, column=4, columnspan=5)
        self.name = Label(master, text = 'Goods Type:', font=("Century Gothic",25,'bold'),fg='maroon',  bg=color, pady=10 , padx=20)
        self.name.grid(row=3,column=0, rowspan=1)
        self.phone = Label(master, text = 'Quantity:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.phone.grid(row=3, column=1, rowspan=1)
        self.address = Label(master, text = 'Price:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.address.grid(row=3,column=2, rowspan=1)
        self.des = Label(master, text = 'Total:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.des.grid(row=3,column=3, rowspan=1)
        self.des = Label(master, text = 'Delete', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.des.grid(row=3,column=4, rowspan=1)
        self.photo1=PhotoImage(file='Images/grey.gif')
        self.bfont = ("Century Gothic",35, 'bold')
        h = 50
        w = 300
        self.last_row = 3
        self.add = Button(master,text="\nAdd Item",command=lambda: self.add_item('second'),compound=BOTTOM)
        self.add.config(image=self.photo1,font=self.bfont,height=h, width = w, highlightbackground=color)
        self.add.grid(row=20, column=0, columnspan=2)
        self.cont = Button(master,text="\nContinue",command = self.cont_func, compound=BOTTOM)
        self.cont.config(image=self.photo1,font=self.bfont,fg='red',height=h, width = w, highlightbackground=color)
        self.cont.grid(row=20, column=2, columnspan=3)
        self.color = color
        self.master = master
        self.item_dict = {}

        master.bind("a", self.add_item_bind)
        master.bind("<Triple-Return>", self.cont_bind, '+')
        master.bind("<Shift-Return>", self.exitbind)
        master.update_idletasks()
        self.width = master.winfo_width()
        self.height = master.winfo_height()
        self.x = int((master.winfo_screenwidth() // 2)) - 500
        self.y = (master.winfo_screenheight() // 2) - (self.height // 2)-200

        master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        self.add_item('first')
        
    def add_item(self, order):
        self.master = self.master
        if order == 'first':
            self.item_dict[self.last_row+1]=[[],0,0, '']
            if self.newsale.description.strip() == '':
                self.newsale.description = '-'
##            self.var = StringVar()
##            self.var.set("\nDelete {0}".format(str(self.last_row-2)))
            self.type = Label(self.master, text = '{0}'.format(self.newsale.description), font=("Century Gothic",15), bg=self.color,pady=0 , padx=1)
            self.type.grid(row=self.last_row+1,column=0, sticky=N)
            #APPEND
            self.item_dict[self.last_row+1][0].append(self.type)


            self.quan = Label(self.master, text = '{0}'.format(self.newsale.quantity), font=("Century Gothic",15,'bold'), bg=self.color,pady=0, padx=1)
            self.quan.grid(row=self.last_row+1, column=1, sticky=N)
            #APPEND
            self.item_dict[self.last_row+1][0].append(self.quan)
            self.item_dict[self.last_row+1][1] += self.newsale.quantity
            
              
            self.price = Label(self.master, text = '{0}'.format(self.newsale.price), font=("Century Gothic",15,'bold'), bg=self.color,pady=0, padx=1)
            self.price.grid(row=self.last_row+1,column=2, sticky=N)
            #APPEND
            self.item_dict[self.last_row+1][0].append(self.price)
            
            self.total = Label(self.master, text = '{0}'.format(self.newsale.total_sale), font=("Century Gothic",15,'bold'), bg=self.color,pady=0, padx=1)
            self.total.grid(row=self.last_row+1,column=3, sticky=N)
            #APPEND
            self.item_dict[self.last_row+1][0].append(self.total)
            self.item_dict[self.last_row+1][2] += self.newsale.total_sale
            color = self.color
            button_text = "\nDelete: {0}".format(self.last_row+1)
            self.but = Button(self.master,text=button_text,compound=BOTTOM)
            self.but.config(image=self.photo1,font=("Century Gothic",15),height=18, width = 50, highlightbackground=color)
            self.but.grid(row=self.last_row+1, column=4, columnspan=2, sticky=N)
            self.item_dict[self.last_row+1][3] = self.last_row+1
            self.item_dict[self.last_row+1][0].append(self.but)

            self.last_row+=1
            self.height += 45
            self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        if order == 'second':
            new = Toplevel()
            start = GoodsType(new, self.newsale, 'second', self.checkout)
            #start = SecondNumPad(new, self.newsale, 'Enter Quantity:', self.checkout)

    def delete_entry(self, num):
        num = num - 1
        lst = self.item_dict[num]
        for item in lst[0]:
            item.destroy()

        self.newsale.subtotal -= lst[2]
        self.item_dict.pop(num)

    def click(self):
        x = self.but['text']
        #self.delete_entry(int(x[-1]))
        print(x)

    def add_item_bind(self, event):
        self.add_item('second')
    def cont_bind(self, event):
        self.cont_func()
    
            
    def cont_func(self):
        color = self.color
        x = messagebox.askyesno('Conclude?', "Are you sure you want to check out?")
        if bool(x) == True:
            row = self.last_row + 1
            Label(self.master, text="Subtotal: ", font= ("Century Gothic",20), bg=color,fg='black').grid(row=row, column=0, sticky=E)
            Label(self.master, text = "฿ {0}".format(float(self.newsale.subtotal)), font=("Century Gothic",50,'bold','italic'), bg=color,fg='dark blue').\
                               grid(row=row, column=1, columnspan=2, sticky=E+W)
            new = Toplevel()
            gui = Payment(new, self.newsale, checkout = self)
            Label(self.master, text="Change: ", font= ("Century Gothic",20), bg=color,fg='black').grid(row=row+1, column=0,sticky=E)
            self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height+25, self.x, self.y))
            self.cont.destroy()
            self.add.destroy()
            for val in list(self.item_dict.values()):
                val[0][-1].destroy()
    def set_change(self):
        color = self.color
        row = self.last_row+1
        Label(self.master, text="Change: ", font= ("Century Gothic",20), bg=color,fg='black').grid(row=row+1, column=1,sticky=W)
        self.change_but = Label(self.master, text = "฿ {0}".format(self.newsale.change), font=("Century Gothic",50,'bold','italic'), bg=color,fg='red').\
                           grid(row=row+1, column=1, columnspan=2, sticky=E+W)

        self.exit = Button(self.master,text="\nCheckout",command = lambda: self.final_exit(self.newsale), compound=BOTTOM)
        self.exit.config(image=self.photo1,font=self.bfont,fg='red',height=50, width = 250, highlightbackground=color)
        self.exit.grid(row=row+2, column=0, columnspan=10, sticky=S+N)
##        self.width += 50
##        self.height += 50
##        self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))
        self.master.unbind("<Triple-Return>")
        self.master.bind("<Double-Return>", self.exitbind)
        self.master.geometry('{}x{}+{}+{}'.format(self.width, self.height+120, self.x, self.y))



    def final_exit(self, newsale):
        newsale.saleobj[-1].payment_type = newsale.payment_type
        newsale.dailysale.add_sales(newsale.saleobj)
        add_to_file_obj(newsale.dailysale) #Updates Daily Sale object into a file
        messagebox.showinfo('Successful!', "Sale Successful!")
        self.master.destroy()

    def exitbind(self,event):
        self.final_exit(self.newsale)
        
    
class Payment:
    def __init__(self, master, newsale, checkout):
        Frame(master)
        color = 'light pink'
        master.config(bg=color)
        self.bfont = ("Century Gothic",20, 'bold', 'italic')
        Label(master, text="Payment Type: ", font= ("Century Gothic",40, 'bold'), bg=color,fg='black').grid(row=0, column=0, columnspan=10)
        self.photo1=PhotoImage(file='Images/grey.gif')
        h = 150
        w = 150
        cash = Button(master,text="\n\n\nCash",command=self.cash,compound=BOTTOM)
        cash.config(image=self.photo1,font=self.bfont,height=h, width = w,highlightbackground=color)
        cash.grid(row=2, column=0)
        self.checkout = checkout
        credit = Button(master,text="\n\n\nCredit\n(Visa/Master)",width=w,command=self.credit,compound=BOTTOM)
        credit.config(image=self.photo1,font=self.bfont,height=h, width = w, highlightbackground=color)
        credit.grid(row=2, column=1)
        self.newsale = newsale
        self.master = master
        master.update_idletasks()
        width = master.winfo_width()
        height = master.winfo_height()
        x = int((master.winfo_screenwidth() // 2))
        #y = (master.winfo_screenheight() // 2) - (height // 2)
        y = 112
        master.bind("<Return>", self.cash_event)
        master.bind("c", self.cred_event)
    
        master.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    def cash(self):
        self.newsale.payment_type = 'cash'
        new = Toplevel()
        gui = SecondNumPad(new, self.newsale, 'Enter Given:', self.checkout)
        self.checkout.set_change()
        self.master.destroy()

    def cash_event(self, event):
        self.cash()

    def credit(self):
        self.newsale.payment_type = 'credit'
        self.checkout.set_change()
        self.master.destroy()

    def cred_event(self, event):
        self.credit()

        
def start_sale(newsale, new):
    x = newsale
    #start = NumPad(root, x, 'Enter Quantity:')
    #step1
    start = OptionalInfoGUI(new, x)
    new.update_idletasks()
    x = 140
    y = 112
    width = new.winfo_width()
    height = new.winfo_height()
    new.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    new.mainloop()
     
if __name__ == '__main__':
    d = DailySales()
    x = NewSale(d)
    root = Tk()
    #NumPad(root, x, 'Enter Quantity:')
##    Payment(root, x)
##    start_sale(x, root)
    #OptionalInfoGUI(root, x)
    checkout = CheckOut(root, x)
    #root.mainloop()
#                #new = Toplevel()
    #GoodsType(root, x, 'first')              
        
