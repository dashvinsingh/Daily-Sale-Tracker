#MainClass
from MainFiles.Daily_Class import DailySales
import pickle

dic = {}

def get_days():
    return len(dic)

def get_latest():

    daily = DailySales()
    if daily.date_string not in dic:
        dic[daily.date_string] = daily
    else:
        daily = dic[self.date_string]
        

    f = open('MainData.py')
    return daily

def handler(x):
    if isinstance(x, DailySales):
        return x.isoformat()
def get_daily(daily):
    # load from file:
    
    with open('Logs/logs.txt', 'wb') as output:
        daily = daily
        pickle.dump(daily,output, 0)

##    # save to file:
    with open('Logs/logs.pkl', 'rb') as input:
        daily = pickle.load(input)

    return daily

if __name__ == '__main__':
    d = DailySales()
    get_daily(d)
