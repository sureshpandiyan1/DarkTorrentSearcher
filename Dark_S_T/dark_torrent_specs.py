import functools
import os
from tkinter import *

def gtseError(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        x = func(*args, **kwargs)
        match(x):
            case 200:
                return 'O.K.'
            case 401 |  403:
                return 'cant get a data'
            case 404:
                return 'data not exist'
            case '_':
                return 'cant access the data'
    return wraps
    

def gtseData(f):
    @functools.wraps(f)
    def wraps(*args, **kwargs):
        x = f(*args, **kwargs)
        try:
            for xx, yy in x.items():
                if 'data' in xx: return bool(1) if len(yy) != 0 else bool(0)
        except:
            return 'sadfsadf'
    return wraps


def gtseGet(func):
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        s = func(*args, **kwargs)
        a = []; b = []; c = []; d = []; 
        lo = []
        
        def runs():
            for x in s.find_all("table")[0].find_all("td"):
                if x['class'][0] == "coll-1":
                    from bs4 import BeautifulSoup
                    thatget = BeautifulSoup(str(x), 'html.parser')
                    that_hf = thatget.find_all("a")[1]
                    d.append(that_hf)
                    for the in d:
                        lll = BeautifulSoup(str(the), 'html.parser')
                        ll = lll.find("a").get("href")
                        lo.append("https://1337x.unblockit.ink" + ll)
                if x['class'][0] == "coll-1":
                    a.append(str(x.text).replace(","," "))
                elif x['class'][0] == "coll-2":
                    b.append(x.text)
                elif x['class'][0] == "coll-3":
                    c.append(x.text)
        
        try:
            runs()
        except:
            pass
        
        with open("tt.txt", "a", encoding="utf-8") as m:
            for x, y, z,o in zip(a,b,c,lo):
                print("%s,%s,%s,%s" % (x,y,z,o), file=m)
            
    return wraps