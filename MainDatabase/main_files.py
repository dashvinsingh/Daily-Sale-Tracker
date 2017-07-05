#Object File Operations
from datetime import datetime as dt
from MainData import *
from objects_file_ops import *

import pickle
import os

t = dt.today()
date_string = '{0}-{1}-{2}'.format(t.day,\
                                        t.month,\
                                        t.year)
months = {1:'January', 2:'February', 3:'March', 4:'April',\
               5:'May', 6:'June', 7:'July', 8:'August', 9:'September',\
               10:'October', 11:'November', 12:'December'}

PATH = 'Object_Logs/{0}/{1}/'.format(t.year,\
                                            months[t.month])
FILENAME = 'main_log.pkl'

def create_main_file():
    file = open(FILENAME, 'wb')
    file.close


def add_to_main(mainclass):
    file = open(FILENAME, 'wb')
    pickle.dump(mainclass, file, 0)
    file.close()

def get_main_class():
    file = open(FILENAME, 'rb')
    daily = pickle.load(file)
    return daily
