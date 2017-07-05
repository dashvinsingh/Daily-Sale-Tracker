#test_file
from NewSale.new_sale_gui import *
from tkinter import *
from MainFiles.Daily_Class import DailySales

if __name__ == '__main__':
    d = DailySales()
    x = NewSale(d)
    root = Tk()
    checkout = CheckOut(root, x)
