#Show Recent
from MainFiles.Daily_Class import DailySales
from NewSale.objects_file_ops import get_object
from tkinter import *
class Recent:
    def __init__(self, master, dailyobj):
        Frame(master)
        color = '#f3e6ff'
        master.config(bg = color)
        Label(master, text="Recent Sales", font= ("Century Gothic",40, 'bold'), bg=color,fg='black').grid(row=1,sticky=W+E, column=0, columnspan=5)
        #Label(master, text = 'Sale #: {0}'.format(self.newsale.sale_num), font= ("Century Gothic",15, 'bold'), bg=color,fg='black').grid(row=1,sticky=W+E, column=4, columnspan=5)
        self.name = Label(master, text = 'Sale #:', font=("Century Gothic",25,'bold'),fg='maroon',  bg=color, pady=10 , padx=20)
        self.name.grid(row=3,column=0, rowspan=1)
        self.phone = Label(master, text = 'Description:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.phone.grid(row=3, column=1, rowspan=1)
        self.address = Label(master, text = 'Quantity:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.address.grid(row=3,column=2, rowspan=1)
        self.des = Label(master, text = 'Price:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.des.grid(row=3,column=3, rowspan=1)
        self.des = Label(master, text = 'Total:', font=("Century Gothic",25,'bold'), fg='maroon',bg=color, pady=5, padx=20)
        self.des.grid(row=3,column=4, rowspan=1)
        self.photo1=PhotoImage(file='Images/grey.gif')
        self.bfont = ("Century Gothic",35, 'bold')
        self.daily = dailyobj
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





    def show_recent(self, max_show=0):
        py = 10
        lst = []
        for item in list(self.daily.sale_num_dict.values()):
            lst += item
        for item in lst:
            if item.sale_num not in self.item_dict:
                self.item_dict[item.sale_num]=[[],'']
                self.num = Label(self.master, text = '{0}'.format(item.sale_num), font=("Century Gothic",20, 'bold'), bg=self.color,fg='dark blue',pady=py , padx=1)
                self.num.grid(row=self.last_row+1,column=0, sticky=N, rowspan=3)

            else:
                self.num = Label(self.master, text = '-', font=("Century Gothic",20, 'bold'), bg=self.color,fg='red',pady=py , padx=1)
                self.num.grid(row=self.last_row+1,column=0, sticky=N, rowspan=3)

                                #APPEND

            self.item_dict[item.sale_num][0].append(self.num)


            if item.description.strip() == '':
                tex = '------------------->'
            else:
                tex = '{0}'.format(item.description.strip())
            self.name = Label(self.master, text = tex, font=("Century Gothic",15,'bold'), bg=self.color,pady=py, padx=1)
            self.name.grid(row=self.last_row+1, column=1, sticky=N)
            #APPEND
            self.item_dict[item.sale_num][0].append(self.name)
            
              
            self.quan = Label(self.master, text = '{0}'.format(item.quantity), font=("Century Gothic",15), bg=self.color,pady=py, padx=1)
            self.quan.grid(row=self.last_row+1,column=2, sticky=N)
            #APPEND
            self.item_dict[item.sale_num][0].append(self.quan)
            
            self.price = Label(self.master, text = '{0}'.format(item.price), font=("Century Gothic",15,), bg=self.color,pady=py, padx=1)
            self.price.grid(row=self.last_row+1,column=3, sticky=N)
            #APPEND
            self.item_dict[item.sale_num][0].append(self.price)

            self.total = Label(self.master, text = '{0}'.format(item.total_sale), font=("Century Gothic",15,'bold'), bg=self.color,pady=py, padx=1)
            self.total.grid(row=self.last_row+1,column=4, sticky=N)
            #APPEND
            self.item_dict[item.sale_num][0].append(self.total)
            self.last_row+=1

    def exit(self):
        self.master.destroy()
    def exitBind(self, event):
        self.master.destroy()


if __name__ == '__main__':
    d = get_object()
    
    new = Tk()
    x = Recent(new, d)
    x.show_recent()
    new.update_idletasks()
    x = 140
    y = 112
    width = new.winfo_width()
    height = new.winfo_height()
    new.geometry('{}x{}+{}+{}'.format(width, height, x, y))


