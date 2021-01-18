import requests
from bs4 import BeautifulSoup
import time 
from plyer import notification
import re
  

def notify(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="virus.ico",
        timeout=120
    )

def getData(url):
    r=requests.get(url)
    return r.text

if __name__ == "__main__":
    while True: 
            myHtml=getData('https://www.mohfw.gov.in/')
            soup = BeautifulSoup(myHtml, 'html.parser')
            myData = []
            for span in soup.find_all('span',{'class':'mob-show'}):
                    d=span.get_text()
                    myData += d.split('\n')
                    
            print("Running Successfully")
            acti=myData[2].split('(')
            active=acti[0]
            discha=myData[5].split('(')
            discharged=discha[0]
            deat=myData[8].split('(')
            deaths=deat[0]
            

            msg=f"Total Cases : {int(active)+int(discharged)+int(deaths)} \nActive Cases : {active} \nDischarged : {discharged}\nDeaths : {deaths} "
            notify("Covid-19 RealTime India Update",msg)
            #it sleeps the code for the time(in seconds) given.
            time.sleep(10)