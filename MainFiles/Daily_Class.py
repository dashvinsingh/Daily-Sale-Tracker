#DailySale Class
from datetime import datetime as dt
from MainFiles.Sale_Class import Sale
from file_operations import *
from NewSale.objects_file_ops import add_to_file_obj
import os

class DailySales:
    def __init__(self):
        self.sales = []
        self.sale_num_dict = {}
        self.total_sale_today = len(self.sale_num_dict)
        self.daily_total = 0
        self.daily_qty = 0
        self.months = {1:'January', 2:'February', 3:'March', 4:'April',\
                       5:'May', 6:'June', 7:'July', 8:'August', 9:'September',\
                       10:'October', 11:'November', 12:'December'}

        #create_file()
        self.t = dt.today()
        self.date_string = '{0}-{1}-{2}'.format(self.t.day,\
                                                self.t.month,\
                                                self.t.year)

##        self.path = 'Logs/{0}/{1}/'.format(self.t.year,\
##                                                    self.months[self.t.month])
##        self.file_name = '{0}.csv'.format(self.date_string)
##        if not os.path.exists(self.path):
##            os.makedirs(self.path)
##        self.file = open(os.path.join(self.path, self.file_name), 'w')
##        self.file.close

    def add_sales(self, sale_object):
        sale_num = sale_object[0].sale_num
        if isinstance(sale_object, Sale):
            self.sales.append(sale_object)
            self.daily_total += sale_object.total_sale
            self.daily_qty += sale_object.quantity
            self.total_sale_today += 1
            self.sale_num_dict[sale_num] = [sale_object]
            #add_to_file(sale_object)
##            self.file = open(os.path.join(self.path, self.file_name), 'a')
##            self.file.write(sale_object.csv_format())
##            self.file.close()
        if isinstance(sale_object, list):
            self.sale_num_dict[sale_num] = sale_object
            for item in sale_object:
                self.sales.append(item)
                self.daily_total += item.total_sale
                self.daily_qty += item.quantity
                #add_to_file(item)
##                self.file = open(os.path.join(self.path, self.file_name), 'a')
##                self.file.write(item.csv_format())
##                self.file.close()
            self.total_sale_today += 1
        else:
            return "Incorrect input, not sale object"

#NEED TO FIX
    def delete_sales(self, number):
        for i in range(len(self.sales)):
            if self.sales[i].sale_num == number:
                self.daily_total -= self.sales[i].total_sale
                self.daily_qty -= self.sales[i].quantity

                f = open(os.path.join(self.path, self.file_name))
                lst = f.readlines()
                f.close()
                lst.pop(number)
                f = open(os.path.join(self.path, self.file_name), 'w')
                for item in lst:
                    f.write(item)
                self.sales.pop(i)
                break

    def clear_file(self):
        create_file()
        add_to_file_obj(self)

    def create_csv(self):
        dic = self.sale_num_dict
        lst = []
        for item in dic.values():
            lst += item

        for sale in lst:
            add_to_file(sale)
    def close_today(self):
        pass

    def __repr__(self):
        return "Daily Sale: {0}".format(self.date_string)

if __name__ == '__main__':
    x = DailySales()
##    from Sale_Class import Sale
##    s1 = Sale(1, 'Dash', quantity=10, price=80)
##    s2 = Sale(2, 'kavin', quantity=55, price=53)
##    s3 = Sale(3, 'Abhin', quantity=150, price=100)
##    s4 = Sale(4, 'Kawal', quantity =3600, price=1.5)
##    lst = [s1, s2, s3]
##    x.add_sales(lst)
