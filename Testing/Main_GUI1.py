#GUI Class
from tkinter import *
from tkinter import ttk, messagebox
import time
from datetime import datetime as dt

class GUI:
    def __init__(self, master):
        self.frame = Frame(master)
        frame_color = 'light blue'
        master.title('Sale Tracker')
        master.attributes("-fullscreen", True)
        master.config(bg=frame_color)
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
                      grid(row =2, columnspan=6)

        #New Sale
        self.new_sale = Button(master, text='\n\nNew Sale', \
                               padx=px, pady=py, fg='red',compound=BOTTOM)
        self.new_sale.config(image=self.photo1,font=("Century Gothic", 35,'bold'),height=h\
                             ,width = w,command=self.test)
        self.new_sale.grid(row=4, column=0, sticky=E+W)

        #Delete Sale
        self.delete_sale = Button(master, text='\n\nDelete Sale', \
                               padx=px, pady=py, compound=BOTTOM)
        self.delete_sale.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.test)
        self.delete_sale.grid(row=4, column=1, sticky=E+W)

        #Show Recent
        self.recent = Button(master, text='\n\nShow \nRecent', \
                               padx=px, pady=py,compound=BOTTOM)
        self.recent.config(image=self.photo1,font=font_but,height=h\
                             ,width = w,command=self.test)
        self.recent.grid(row=4, column=3, sticky=E+W)

        #Find Sale
        self.find = Button(master, text='\n\nFind Sale', \
                               padx=px, pady=py, compound=BOTTOM)
        self.find.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.test)
        self.find.grid(row=4, column=2, sticky=E+W)

        #Current Sale Revenue
        self.find = Button(master, text='\nCurrent Sale\nRevenue', \
                               padx=px, pady=py, compound=BOTTOM)
        self.find.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.test)
        self.find.grid(row=5, column=0, sticky=E+W)


        #Current Sale Revenue
        self.close = Button(master, text='\nClose Sale\nand\nEmail Report', \
                               padx=px, pady=py, compound=BOTTOM)
        self.close.config(image=self.photo1,font=font_but,height=h\
                             ,width = w, command=self.test)
        self.close.grid(row=5, column=1, sticky=E+W)
        
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
              font=('Century Gothic', 30,'bold'),bg=frame_color).grid(row=5, column=2,\
                                                       sticky=E)


         #Sale Count
##        Label(master, text = "Sale Count"
    
        #Time
        self.time1 = ''
        self.time2 = time.strftime('%H:%M:%S')

        self.watch = Label(master, text=self.time2, font=('Century Gothic',\
                                                          50,'bold'),bg=frame_color)
        self.watch.grid(row=5, column=3)
        self.master = master
        self.changeLabel() #first call it manually

    def changeLabel(self): 
        self.time2 = time.strftime('%H:%M:%S')
        self.watch.configure(text=self.time2)
        self.master.after(200, self.changeLabel) #it'll call itself continuously


    def test(self):
        messagebox.showinfo('Works!', "Button Works")


class _Authen:
    def __init__(self, master):
        frame_color='light blue'
        self.password = 'password'
        master.config(bg = frame_color)
        master.title('Login to Sales System.')
        self.title = Label(master, text = 'Login to Sales System:', font = ("Century Gothic", 40), fg = 'red', bg=frame_color)
        self.title.grid(row=0, columnspan=6)
        self.rec_title = Label(master, text = '\nPassword:', font = ("Century Gothic", 18), fg='red',  bg=frame_color)
        self.rec_title.grid(row=2, column=0, sticky=E)
        self.password_entry = Entry(master, width = 40, show='*', highlightcolor=frame_color, highlightbackground=frame_color, bg = frame_color)
        self.password_entry.grid(row=2, column=1,columnspan=4, sticky=W+S)
        self.button = Button(master, text='Login', command = self.authenticate, width=42,highlightcolor=frame_color, highlightbackground=frame_color)
        self.button.grid(row=3, columnspan=5, sticky=E, pady=15)
        master.bind("<Return>", self.enter_key)
        self.master = master

    def authenticate(self):
        if self.password_entry.get() == self.password:
            self.master.destroy()
            root = Tk()
            main = GUI(root)
        else:
            messagebox.showerror('Invalid Password', 'Invalid Password!')
            

    def enter_key(self, event):
        self.authenticate()

if __name__ == "__main__":
    auth = True
    root = Tk()
    if auth == True:
        _Authen(root)
    else:
        GUI(root)
