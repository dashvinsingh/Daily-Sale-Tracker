#Sale Class
from datetime import datetime as dt
class Sale:
    def __init__(self, num, name='', phone='', address='',\
                 description = '', quantity=0, price=0, change=0, payment_type=''):

        self.sale_num = num
        self.payment_type = payment_type #cash/credit
        self.name = name
        self.phone = phone
        self.address = address
        self.description = description
        self.quantity = quantity
        self.price = price
        self.change = change
        self.total_sale = self.quantity*self.price
        self.t = dt.today()
        self.date_string = '{0}/{1}/{2} {3}:{4}:{5}'.format(self.t.day,\
                                                            self.t.month,\
                                                            self.t.year,\
                                                            self.t.hour,\
                                                            self.t.minute,\
                                                            self.t.second)


    def compute_total(self):
        self.total_sale = self.quantity*self.price
    def __repr__(self):
        return "Sale: {0}".format(self.sale_num)
    def __str__(self):
        return "Sale #: {5}\nDate: {6}\nName: {0}\nDescription: {1}\n\
Quantity: {2}\nPrice: {3}\nTotal: {4}\n".format(\
    self.name, self.description, self.quantity, self.price, self.total_sale, \
    self.sale_num, self.date_string)

    def info(self):
        return self.__str__()

    def brief(self):
        return "Sale #: {0}, Name: {1}, QTY: {2}, Price: {3}, Total: {4}".format\
               (self.sale_num, self.name, self.quantity, self.price, self.total_sale)
    


        
    def csv_format(self):
        #salenum, date, name, quantity, price, total, payment_type
        return '\n{0}, {1}, {7}, {2}, {3}, {4}, {5}, {6}\n'.format(self.sale_num,\
                                                       self.date_string,\
                                                       self.name,\
                                                       self.quantity,\
                                                       self.price,\
                                                       self.total_sale,\
                                                       self.payment_type,\
                                                        self.description)

if __name__ == "__main__":
    x = Sale(1,name = 'Dash', phone='0819109888', description = 'Satin', quantity = 4, price=1000)
    y = Sale(2,name = 'kavin', phone='01293', description = 'lace', quantity = 15, price=80, payment_type='credit')
    print(x)
    print(y)
    f = open('test.csv', 'w')
    f.write('\nsalenum, date, name, quantity, price, total, payment type')
    f.write(x.csv_format())
    f.write(y.csv_format())
    f.close()
