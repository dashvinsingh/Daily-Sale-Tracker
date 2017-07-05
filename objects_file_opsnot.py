#Object File Operations
from datetime import datetime as dt
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
FILE_NAME = '{0}.pkl'.format(date_string)

def create_file():
    t = dt.today()
    date_string = '{0}-{1}-{2}'.format(t.day,\
                                            t.month,\
                                            t.year)

    path = 'Object_Logs/{0}/{1}/'.format(t.year,\
                                                months[t.month])
    file_name = '{0}.pkl'.format(date_string)
    if not os.path.exists(PATH):
        os.makedirs(PATH)
    file = open(os.path.join(PATH, FILE_NAME), 'wb')
    file.close


def add_to_file_obj(daily_saleobj):
    file = open(os.path.join(PATH, FILE_NAME), 'wb')
    pickle.dump(daily_saleobj, file, 0)
    file.close()

def get_object():
    file = open(os.path.join(PATH, FILE_NAME), 'rb')
    daily = pickle.load(file)
    return daily

def date_object(date):
    #try:
    d = '{0}.pkl'.format(date)
    file = open(d, 'rb')
    daily = pickle.load(file)
    return daily
    #except:
        #print('Invalid Date format')

