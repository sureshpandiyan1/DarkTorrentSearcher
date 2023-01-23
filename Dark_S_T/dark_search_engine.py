from user_agent import *
import requests, json, bs4
from Dark_S_T.dark_torrent_specs import *
from Dark_S_T.dark_torrent_ls import the_urls
from Dark_S_T.dark_torrent_s import dark_splash, enters, not_compt
import os, sys


class gtse:

    __slots__ = ["gtse_engine"]

    def __init__(self, surl):
        try:
            self.gtse_engine = requests.get(the_urls['XUN234DSF']['M_URL'] + surl)
        except Exception as GTSE: 
            @gtseError
            def excgts():
                try: 
                    status, message = GTSE.args
                    return  status if (GTSE.args != 2) else GTSE.args
                except:
                    return '_'
            
            print(excgts())

    
    @gtseData
    def get_json(self):
        x_gtse = json.loads(self.gtse_engine.text)
        return x_gtse


    
    def run_through(self, name):
        t_url = f"{the_urls['XUN234DSF']['S_URL']}{name}"
        try:
            t_url_ld =  lambda y: [y + "/" + str(i) + "/"  for i in range(1,9)]
        except:
            t_url_ld =  lambda y: [y + "/" + str(i) + "/"  for i in range(1,6)]
        t_urls = t_url_ld(t_url)
        return list(t_urls)


    @gtseGet
    def save_html(self, url):
        p = requests.get(url, headers={
            "Referer": the_urls['XUN234DSF']['R_URL'],
            "User-Agent": generate_user_agent()
        })
        soup_obj = bs4.BeautifulSoup(p.content, "html.parser")
        return soup_obj

    
    def all_gets(self, name):
        the_urls = self.run_through(name)
        for z in the_urls:
            self.save_html(z)


def run_DTShr():
    if sys.platform[0:3] == "win":
        dark_splash()
        enters(gtse)
    else:
        not_compt()