#GUI Class
from tkinter import *
from tkinter import ttk, messagebox
import time
from settings import MainConfig as c
from datetime import datetime as dt
from NewSale.new_sale_gui import *
from MainFiles.Daily_Class import DailySales
from MainFiles.MainData import get_latest, get_days
from NewSale.objects_file_ops import *
from DeleteSale.deletesale import SaleNum
from show_recent_gui import Recent
from current_revenue import CurrentRevenue
from email_gui import *

class GUI:
    def __init__(self, master, dailysalesobj, fs=False, trial=None):
        self.frame = Frame(master)
        self.frame.focus_set()
        self.daily = dailysalesobj
        frame_color = '#80ffe5'#c().color
        master.title('Sale Tracker')
        if fs==True:
            master.attributes("-fullscreen", True)
        master.config(bg=frame_color)
        master.focus_force()
        master.protocol('WM_DELETE_WINDOW', self.exit_destroy)
        self.style = ttk.Style()
        self.style.configure('TButton', highlightbackground=frame_color,  highlightcolor=frame_color,bg = frame_color,\
                              font = ("Century Gothic", 25), height=100, width=10)

        self.photo1=PhotoImage(file='Images/grey.gif')
        font_but = ("Century Gothic", 35,'bold')
        h = 180
        w = 150
        px = 60
        py = 60
        Label(master, text='Daily Sale Tracker', font = ("Century Gothic", 70), bg=frame_color).\
                      grid(row =0, columnspan=6)
        
        #New Sale
        self.new_sale = Button(master, text='\n\nNew Sale', \
                               padx=px, pady=py, fg='red',compound=BOTTOM)
        self.new_sale.config(image=self.photo1,font=("Century Gothic", 35,'bold'),height=h\
                             ,width = w,command=self.new_sale_func, highlightbackground=frame_color)
        self.new_sale.grid(row=2, column=0, sticky=E+W)
        

        #Delete Sale
        self.delete_sale = Button(master, text='\n\nVoid Sale', \
                               padx=px, pady=py, compound=BOTTOM)
        self.delete_sale.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.del_sale_func, highlightbackground=frame_color)
        self.delete_sale.grid(row=2, column=1, sticky=E+W)

        #Show Recent
        self.recent = Button(master, text='\n\nShow \nRecent', \
                               padx=px, pady=py,compound=BOTTOM)
        self.recent.config(image=self.photo1,font=font_but,height=h\
                             ,width = w,command=self.show_recent, highlightbackground=frame_color)
        self.recent.grid(row=2, column=3, sticky=E+W)

        #Find Sale
        self.find = Button(master, text='\n\nFind Sale', \
                               padx=px, pady=py, compound=BOTTOM)
        self.find.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.test, highlightbackground=frame_color)
        self.find.grid(row=2, column=2, sticky=E+W)

        #Current Sale Revenue
        self.find = Button(master, text='\nCurrent Sale\nRevenue', \
                               padx=px, pady=py, compound=BOTTOM)
        self.find.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.current_sale_func, highlightbackground=frame_color)
        self.find.grid(row=4, column=0, sticky=E+W)


        #Close and Email
        self.close = Button(master, text='\nClose Sale\nand\nEmail Report', \
                               padx=px, pady=py, compound=BOTTOM)
        self.close.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.close_and_email, highlightbackground=frame_color)
        self.close.grid(row=4, column=1, sticky=E+W)
        
        #Date
        weekday = {0:"Monday", 1:"Tuesday",2:"Wednesday", 3:"Thursday",\
                   4:"Friday", 5:"Saturday", 6:"Sunday"}
        months = {1:'January', 2:'February', 3:'March', 4:'April',\
               5:'May', 6:'June', 7:'July', 8:'August', 9:'September',\
               10:'October', 11:'November', 12:'December'}
        self.t = dt.today()
        Label(master, text="{0}, \n{1} {2}, {3}".format(weekday[self.t.weekday()]\
                                                      ,self.t.day, months\
                                                      [self.t.month], \
                                                      self.t.year),\
              font=('Century Gothic', 30,'bold'),bg=frame_color).grid(row=3, column=2,\
                                                       sticky=E,rowspan=5)

        self.count1 = self.daily.total_sale_today
        self.count2 = self.daily.total_sale_today
         #Sale Count and Daily Sale
        self.sale_count = Label(master, font=('Century Gothic', 15,'bold'),bg=frame_color, \
                      text = "{0}, Sale Count: {1}".format(self.daily.__repr__(),\
                                                           self.count1))
        self.sale_count.grid(row=4, rowspan=5,column=3, columnspan=6 ,sticky=S+W)
    
        #Time
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')

        self.watch = Label(master, text=self.time2, font=('Century Gothic',\
                                                          50,'bold'),bg=frame_color)
        self.watch.grid(row=3, column=3, rowspan = 5)
        self.master = master
        self.changeLabel() #first call it manually
        self.get_count()
        self.newsale = None
        self.trial = trial

        self.master.bind("s", self.new_sale_key)
        self.master.bind("d", self.del_sale_key)
        self.master.bind("f", self.find_sale_key)
    def get_count(self):
        self.count2 = self.daily.total_sale_today
        self.sale_count.configure(text = "{0}, Sale Count: {1}".format(self.daily.__repr__(),\
                                                           self.count2))
        self.master.after(200, self.get_count)
    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
        self.master.after(200, self.changeLabel) #it'll call itself continuously

    
    def test(self):
        messagebox.showinfo('Works!', "Button Works")

    #New Sale
    def new_sale_func(self):
        if self.trial == True and self.daily.total_sale_today < 3:
            master = Toplevel()
            self.newsale = NewSale(self.daily)
            start = start_sale(self.newsale, master)
            master.mainloop()
        elif self.trial == False:
            master = Toplevel()
            self.newsale = NewSale(self.daily)
            start = start_sale(self.newsale, master)
            master.mainloop()
        else:
            messagebox.showerror('Trial Expired', 'TRIAL MODE LIMITATION: \nOnly Three sale objects allowed, please delete at least one sale object.')
        #x = NewSale().getsaleobj()
    def new_sale_key(self, event):
        self.new_sale_func()

    #Delete Sale
    def del_sale_func(self):
        if self.daily.total_sale_today == 0:
            messagebox.showerror('No Sale!', "There are no sale objects to void")
        else:
            new = Toplevel()
            SaleNum(new, self.newsale, 'Enter Sale #', self.daily)
            new.mainloop()
    def del_sale_key(self, event):
        self.del_sale_func()

    #Find Sale
    def find_sale_func(self):
        messagebox.showinfo('FIND Sale', 'FIND SALE')
    def find_sale_key(self, event):
        self.find_sale_func()

    #Show Recent
    def show_recent(self):
        new = Toplevel()
        x = Recent(new, self.daily)
        x.show_recent()
        new.update_idletasks()
        x = 140
        y = 112
        width = new.winfo_width()
        height = new.winfo_height()
        new.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        new.mainloop()


    def find_sale_key(self, event):
        self.show_recent()

    #Current Sale Info
    def current_sale_func(self):
        new = Toplevel()
        x = _Authen(new, 'current_sales', daily=self.daily)
        new.mainloop()

    def close_and_email(self):
        new = Toplevel()
        x = Email_GUI(new)


    def exit_destroy(self):
        self.master.destroy()

class _Authen:
    def __init__(self, master, gui_name, fs=False, trial=None, daily=None):
        self.gn = gui_name
        self.t = dt.today()
        self.date_string = '{0}-{1}-{2}'.format(self.t.day,\
                                                self.t.month,\
                                                self.t.year)
        frame_color=c().color
        self.password = c().password
        master.config(bg = frame_color)
        master.title('Login to Sales System.')
        self.title = Label(master, text = 'Login to Authenticate:', font = ("Century Gothic", 40), fg = 'red', bg=frame_color)
        self.title.grid(row=0, columnspan=6)
        self.rec_title = Label(master, text = '\nPassword:', font = ("Century Gothic", 18), fg='red',  bg=frame_color)
        self.rec_title.grid(row=2, column=0, sticky=E)
        self.password_entry = Entry(master, width = 40, show='*', highlightcolor=frame_color, highlightbackground=frame_color, bg = frame_color)
        self.password_entry.grid(row=2, column=1,columnspan=4, sticky=W+S)
        self.button = Button(master, text='Login', command = self.authenticate, width=42,highlightcolor=frame_color, highlightbackground=frame_color)
        self.button.grid(row=3, columnspan=5, sticky=E, pady=15)
        master.bind("<Return>", self.enter_key)
        master.bind("<Escape>", self.close_window)
        self.master = master
        master.focus_force()
        self.trial= trial
        self.fs = fs
        self.daily2=daily
        self.password_entry.bind("<Tab>", self.focus_next_window)
        self.master = master

    def authenticate(self):
        entry = self.password_entry.get().strip()
        if entry == self.password or entry == 'admin':
            self.master.destroy()
            if self.gn == 'main':
                if not os.path.isfile(os.path.join(PATH, FILE_NAME)):
                    create_file()
                    today = DailySales()
                    add_to_file_obj(today)
                self.daily = get_object()
                root = Tk()
                main = GUI(root, self.daily, self.fs, self.trial)
                root.mainloop()
            if self.gn == 'current_sales':
                if entry == self.password:
                    messagebox.showerror('Invalid Password', 'You do not have access!')
                elif entry == 'admin':
                    new = Toplevel()
                    curr = CurrentRevenue(new, self.daily2)
                    new.update_idletasks()
                    x = 140
                    y = 112
                    width = new.winfo_width()
                    height = new.winfo_height()
                    new.geometry('{}x{}+{}+{}'.format(width, height, x, y))
                    new.mainloop()
                    new.mainloop()



        else:
            messagebox.showerror('Invalid Password', 'Invalid Password!')
            self.password_entry.delete(0, 'end')
            

    def enter_key(self, event):
        self.authenticate()

    def focus_next_window(self, event):
        event.widget.tk_focusNext().focus()
        return("break")

    def close_window(self, event):
        self.master.destroy()

if __name__ == "__main__":
    auth = True
    clear = False
    full_screen = False
    trial = False
    root = Tk()
    if auth == True:
        st = _Authen(root, 'main', full_screen, trial)
        root.update_idletasks()
        x = 140
        y = 112
        width = root.winfo_width()
        height = root.winfo_height()
        root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    else:
        if not os.path.isfile(os.path.join(PATH, FILE_NAME)):
            create_file()
            today = DailySales()
            add_to_file_obj(today)
        if clear == True:
            create_file()
            today = DailySales()
            add_to_file_obj(today)
        daily = get_object()
        st = GUI(root, daily, full_screen, trial)
root.mainloop()
