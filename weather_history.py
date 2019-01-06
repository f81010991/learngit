import requests
from BeautifulSoup import BeautifulSoup
import re
import time


url='http://www.tianqihoubao.com/lishi/ningbo/month/%s.html'

for year in range(2011,2019):
    for mon in range(1,13):
        if len(str(mon))==1:
            mon='0'+str(mon)
        else:
            mon=str(mon)
        date=str(year)+mon

        time.sleep(3)

        content=requests.get(url%date)
        soup=BeautifulSoup(content.text)
        table=soup.find(id='content').table

        for tr in table:
            for td in tr:
                try:
                    print re.sub('[\s]*','',td.text),'~',
                except:
                    pass
            print
