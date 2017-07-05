#Current Revenue
from show_recent_gui import Recent
from tkinter import *
from NewSale.objects_file_ops import get_object

class CurrentRevenue(Recent):
    def __init__(self, master, dailysaleobj):
        #Recent.__init__(self, master, dailysaleobj)
        
        Frame(master)
        color = '#f3e6ff'
        master.config(bg = color)
        self.daily = dailysaleobj
        Label(master, text="Current Revenue", font= ("Century Gothic",40, 'bold'), bg=color,fg='black').grid(row=1,sticky=W+E, column=0, columnspan=5)
        #Label(master, text = 'Sale #: {0}'.format(self.newsale.sale_num), font= ("Century Gothic",15, 'bold'), bg=color,fg='black').grid(row=1,sticky=W+E, column=4, columnspan=5)
        self.name = Label(master, text = '\nSale Count:', font=("Century Gothic",25,'bold'),fg='maroon',  bg=color, pady=10 , padx=20)
        self.name.grid(row=3,column=0, rowspan=1)
        self.scount = Label(master, text = '{0}'.format(self.daily.total_sale_today), font=("Century Gothic",25,'bold'),fg='dark green',  bg=color, pady=10 , padx=20)
        self.scount.grid(row=3, column=1, sticky=S)
        self.phone = Label(master, text = '\nRevenue:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.phone.grid(row=3, column=2, rowspan=1)
        self.total = Label(master, text = '{0}'.format(self.daily.daily_total), font=("Century Gothic",25,'bold'),fg='dark blue',  bg=color, pady=10 , padx=20)
        self.total.grid(row=3, column=3, sticky=S)
        self.photo1=PhotoImage(file='Images/grey.gif')

        self.bfont = ("Century Gothic",35, 'bold')
        self.daily = dailysaleobj
        self.last_row = 3
        self.color = color
        self.master = master
        self.item_dict = {}
        self.photo1=PhotoImage(file='Images/grey.gif')
        self.exit = Button(master,text="\nExit",command= self.exit,compound=BOTTOM)
        self.exit.config(image=self.photo1,font=("Century Gothic",45, 'bold'),height=50, width = 600, highlightbackground=color)
        self.exit.grid(row=15, column=0, columnspan=5)
        master.bind("<Return>", self.exitBind)
        master.update_idletasks()
        self.width = master.winfo_width()
        self.height = master.winfo_height()
        self.x = 140
        self.y = 112

        master.geometry('{}x{}+{}+{}'.format(self.width, self.height, self.x, self.y))

    def exit(self):
        self.master.destroy()
    def exitBind(self, event):
        self.master.destroy()



if __name__ == '__main__':
    root = Tk()
    d = get_object()
    CurrentRevenue(root, d)
