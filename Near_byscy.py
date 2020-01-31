import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import webbrowser
import re
#import pyrebase
#from flask import Flask , render_template , request



def find_phy(url,ua,url1):
    res=requests.get(url,headers=ua)
    soup = BeautifulSoup(res.content,'html.parser')
    list1=[]
    name = soup.find_all(class_="lng_cont_name")
    available = soup.find_all(class_="distnctxt rsrtopn-1")
    addr=soup.find_all(class_='adWidth cont_sw_addr')
    for i in range(len(addr)):
        list1.append(addr[i].get_text().strip())
    for i in list1:
        for k in i:
            if k==" ":
                k+="-"
        print(i)        


    
    #appointment = soup.find_all('a',attrs={'class':'bookap green-btn result_loader_0 big_dn'})
    print(len(available),len(name))
    #https://www.justdial.com/Mumbai/Dr-Dhara-Kothari-Feet-%20Road/033PXX33-XX33-180601112432-I6P8_BZDET?xid=S29sa2F0YSBQaHlzaWF0cmlzdCBEb2N0b3Jz&tab=book-appointment&reqbk=0
    '''
    for i in range(len(available)):
        print(name[i].get_text())
        print(available[i].get_text())
        print("\n ")
    #print(name.get_text())
    #for i in name:
    '''
        

    contact = soup.find_all(class_=".contact-info a , b")
    print(contact)

    #print(con.attr)
    #for descr in soup.find_all('span', attrs={'class':'mobilesv'}):
        #print(descr)

   

if __name__ == "__main__":

    place = input("Enter the name")
    ua={"User-Agent":'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0'}

    url = "https://www.justdial.com/"+str(place)+"/Physiatrist-Doctors/nct-11105148"
    url1=url
    find_phy(url,ua,url1)
