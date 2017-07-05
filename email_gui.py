#Sending Daily Sales Email
import mimetypes
import email
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib
from NewSale.objects_file_ops import get_object
from MainFiles.Daily_Class import DailySales
from file_operations import *
from tkinter import *


class Email_GUI:
    def __init__(self, master):
        self.frame = Frame(master)
        master.minsize(width = 200, height = 200)
        master.config(bg = 'cyan')
        master.title('Python Email Authentication')
        self.title = Label(master, text = 'Python Email Authentication', font = ("Century Gothic", 40), fg = 'black', bg = 'cyan')
        self.title.pack()
        text1 = 'Login to the email system! \nSupported Services: UtorMail, Gmail, Outlook, Yahoo'
        self.detail = Label(master, text = text1, font = ("Century Gothic", 15), fg = 'black', bg = 'cyan')
        self.detail.pack()
        #email Client
        self.variable = StringVar(master)
        self.variable.set('Choose One')
        self.w = OptionMenu(master, self.variable, 'Choose One', 'UtorMail', 'Gmail', 'Outlook', 'Yahoo')
        self.w.pack()
        #Username
        self.rec_title = Label(master, text = '\nEmail Address/Username', font = ("Century Gothic", 18), bg = 'cyan')
        self.rec_title.pack()
        self.rec_email = Entry(master, width = 40)
        self.notice = Label(master, text = 'Use your UtorMail if you wish you use the Uoft Servers', font = ("Century Gothic", 10), bg = 'cyan')
        self.rec_email.pack()
        self.notice.pack()
        #Password
        self.password_title = Label(master, text = '\nPassword', font = ("Century Gothic", 18), bg = 'cyan')
        self.password_title.pack()
        self.password_entry = Entry(master, show='*', width = 40)
        self.password_entry.pack()
        #button
        self.auth = Label(master, text = '\nAuthenticate', font = ("Century Gothic", 18), bg = 'cyan')
        self.auth.pack()
        self.button = Button(master, text='Authenticate', command = self.make_connection)
        self.button.pack()
        master.bind("<Return>", self.enter_key)
        master.bind("<Shift-Return>", self.triple_enter)
        self.master = master
        self.object = [ self.detail, self.rec_title,\
                       self.rec_email, self.notice,self.w, self.password_title,\
                       self.password_entry, self.auth, self.button]

        self.rec = None
        self.connect = None

    def make_connection(self):
        client = self.variable.get()
        if client == 'Choose One':
            messagebox.showerror('Invalid Email Client.' ,'Please choose a valid email client.')
        else:
            user = self.rec_email.get()
            password = self.password_entry.get()
            self.connect = Email(user, password, client)
            #print(client, user, password)
            x = self.connect.login()
            if x is not False and client is not 'Choose One':
                success = messagebox.showinfo('Connection Successful!',\
                                              'Connected to: \n{0}\nOK to proceed'.format(user))
                self.pop_items()
                self.create_new()
##                d = get_object()
##                create_file()
##                d.create_csv()
##                e = Email_first(d)
##                msg = e.get_msg()
##                connect.new_send('circleline10@gmail.com', msg)
##                #connect.new_send('dashvin_10@hotmail.com', msg)
##                messagebox.showinfo('Send!', 'Email Report Sent!')
                #self.master.destroy()
                
            else:
                messagebox.showerror('Connection Fail, try again',\
                                           "Invalid Username, Password, or Client, Please Try Again.")



    def send_gui(self):
        d = get_object()
        create_file()
        d.create_csv()
        e = Email_first(d)
        msg = e.get_msg()
        lst = self.rec.get(1.0,END).strip().split(',')
        for item in lst:
            if self.verify_email(item):
                self.connect.new_send(item, msg)

        messagebox.showinfo('Sent!', 'Email Report Sent!')
        self.master.destroy()


    def verify_email(self, email):
        import re
        valid_re = re.compile(r'^.+@.+')
        if valid_re.match(email):
            return True
        else:
            return False
    def send_gui_event(self, event):
        self.send_gui()
    def send_direct(self):
        user = ''
        password = ''
        client = 'Gmail'
        connect = Email(user, password, client)
        connect.login()
        d = get_object()
        create_file()
        d.create_csv()
        e = Email_first(d)
        msg = e.get_msg()
        connect.new_send('circleline10@gmail.com', msg)
        #connect.new_send('dashvin_10@hotmail.com', msg)
        messagebox.showinfo('Send!', 'Email Report Sent!')
        self.master.destroy()
                        
    def enter_key(self, event):
        self.make_connection()

    def triple_enter(self, event):
        self.send_direct()

    def pop_items(self):
        for item in self.object:
            item.destroy()

    def create_new(self):
        self.title = Label(self.master, text = 'Enter Recipients:', font = ("Century Gothic", 25), fg = 'maroon', bg = 'cyan')
        self.title.pack()
        self.note = Label(self.master, text = 'Email Addresses; Separated by comma',  font = ("Century Gothic", 15), fg = 'maroon', bg = 'cyan')
        self.note.pack()
        self.rec = Text(self.master, width = 50, height=5)
        self.rec.pack()
        self.send = Button(self.master, text = 'Send Email', command=self.send_gui)
        self.send.pack()
        self.master.unbind("<Return>")
        self.master.bind("<Return>", self.send_gui_event)
class Email_first:
    def __init__(self, daily_sales_obj):
        msg = MIMEMultipart()
        msg['Subject'] = 'Daily Sale Report'
        msg['From'] = 'Daily Sale Report'
        msg['To'] = 'do_not_reply@do_not_reply.com'
        msg['Subject'] = 'Daily Sale Report'
        self.daily = daily_sales_obj
        
        text = "Today's Sale Report: \n\nDate: {0}\
\n\nApproximate Number of Sales: {1}\
\n\nTotal Revenue: {2}".format(date_string, self.daily.total_sale_today, self.daily.daily_total)

        msg.attach(MIMEText(text))
        
        filename = NEW_NAME
        with open(filename, 'rb') as f:
            part = MIMEApplication(f.read(), Name=basename(filename))
            part['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
            msg.attach(part)
        self.msg = msg

    def get_msg(self):
        return self.msg

class Email():
    def __init__(self, username, password, cl='Gmail'):
        self._username = username
        self._password = password
        self._email = username
        self.client = {'UtorMail':['smtp.office365.com', 587], 'Gmail':['smtp.gmail.com', 587], 'Outlook':['smtp.live.com', 587], 'Yahoo':['smtp.mail.yahoo.com', 465]}
        import smtplib
        self.email_client=self.client[cl][0]
        self.port = self.client[cl][1]
        self.smtp = smtplib.SMTP(self.email_client, self.port)
        self.cl = cl
    def login(self):
        try:
            self.smtp.connect(self.email_client, self.port)
            self.smtp.ehlo()
            self.smtp.starttls()
            self.smtp.login(self._username, self._password)
            return True
##            from imaplib import IMAP4_SSL
##            self.imap = IMAP4_SSL('outlook.office365.com', 993)
##            self.imap.login(self._email, self._password)
##            print('IMAP Connection Successful')
        except:
            return False
    def send(self, to, subject='', message='', eom="Sent Using Python App"):
        new = "Subject: {0}\n{1} \n\n{2}".format(subject, message, eom)
        try:
            self.smtp.sendmail(self._email, to, new)
            return True
        except:
            return False

    def new_send(self, to, msg):
        self.smtp.sendmail(self._email, to, msg.as_string())



if __name__ == '__main__':
    root = Tk()
    x = Email_GUI(root)
