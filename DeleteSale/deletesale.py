from NewSale.new_sale_gui import NumPad
from tkinter import *
from MainFiles.Daily_Class import DailySales
from NewSale.objects_file_ops import add_to_file_obj


class SaleNum(NumPad):
    def __init__(self, master, newsale, title, dailysale):
        NumPad.__init__(self, master, newsale, title)
        self.color = 'maroon'
        self.daily = dailysale
        self.master = master

    def enter(self):
        new = self.e.get(1.0, END)
        self.e.delete(1.0,END)
        try:
            x = messagebox.askyesno('Delete Sale', 'Are you sure you want to \
delete?\n{0}'.format([item.brief() for item in self.daily.sale_num_dict[int(new)]]))
            if bool(x) == True:
                lst = self.daily.sale_num_dict[int(new)]
                subtract_total = 0
                for sale in lst:
                    subtract_total += sale.total_sale
                self.daily.sale_num_dict.pop(int(new))
                self.daily.total_sale_today -=1
                self.daily.daily_total -= subtract_total
                add_to_file_obj(self.daily)
                self.master.destroy()
                messagebox.showinfo('Success!', 'Deleted Sale!')
        except KeyError:
            messagebox.showerror('Invalid Input', 'This is an invalid sale number')
        except ValueError:
            messagebox.showerror("Invalid Input", 'Only Integer Sale Numbers Allowed')
        

if __name__ == '__main__':
    x = Tk()
    d = DailySales()
    SaleNum(x, None, 'Enter Sale Number', d)
