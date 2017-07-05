import pickle
from Daily_Class import DailySales
class Test:
    def __init__(self, name, number):
        self.name = name
        self.number = number


def write(daily):
    # load from file:
    
    with open('logs.txt', 'wb') as output:
        daily = daily
        pickle.dump(daily,output, 0)

def get_daily():
    ##    # save to file:
    with open('logs.txt', 'rb') as input:
        daily = pickle.load(input)

    return daily

if __name__ == '__main__':
    d = Test("dash", 1)
    d2 = Test('kavin', 3)
    d3 = DailySales()
    write(d)
    write(d2)
    write(d3)
    x = get_daily()
    y = get_daily()
