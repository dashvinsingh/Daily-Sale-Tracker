#MainClass
from main_files import *
from datetime import datetime as dt


class MainClass:
    def __init__(self):
        self.dict = {} #date:daily_sale_obj
        self.monthly = 0
        t = dt.today()
        self.date_string = '{0}-{1}-{2}'.format(t.day,\
                                        t.month,\
                                        t.year)

    def add_to_dict(self, dailyobj):
        self.dict[self.date_string] = dailyobj


if __name__ == '__main__':
    d = MainClass()
    #create_main_file
    #add_to_main
    #get_main_class
