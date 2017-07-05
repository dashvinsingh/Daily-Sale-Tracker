#CSV File Operations
from datetime import datetime as dt
import os

t = dt.today()
date_string = '{0}-{1}-{2}'.format(t.day,\
                                        t.month,\
                                        t.year)
months = {1:'January', 2:'February', 3:'March', 4:'April',\
               5:'May', 6:'June', 7:'July', 8:'August', 9:'September',\
               10:'October', 11:'November', 12:'December'}

PATH = 'Logs/{0}/{1}/'.format(t.year,\
                                            months[t.month])
FILE_NAME = '{0}.csv'.format(date_string)
NEW_NAME = os.path.join(PATH, FILE_NAME)

def create_file():
    t = dt.today()
    date_string = '{0}-{1}-{2}'.format(t.day,\
                                            t.month,\
                                            t.year)

    path = 'Logs/{0}/{1}/'.format(t.year,\
                                                months[t.month])
    file_name = '{0}.csv'.format(date_string)
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    file = open(os.path.join(PATH, FILE_NAME), 'w')
    file.write('\nSALE REPORT, {0}\nSalenum, Date, Goods Type, Name, Quantity, Price, Total, Payment Type'\
               .format(date_string))
    file.close


def add_to_file(sale_object):
    file = open(os.path.join(PATH, FILE_NAME), 'a')
    file.write(sale_object.csv_format())
    file.close()

    
    

##def remove_from_file(sale_object):
##    self.file = open(os.path.join(PATH, FILE_NAME), 'a')
##    self.file.write(sale_object.csv_format())
##    self.file.close()
