import pandas as pd
from bs4 import BeautifulSoup, NavigableString
from urllib import request
import requests
import os
assert 'SYSTEMROOT' in os.environ
import socket
import lxml
import lxml.etree
from lxml import etree
import re
from lxml import html
import numpy
import time
from verify_email import verify_email
from wrapt_timeout_decorator import *
import socket
from email_validator import validate_email
@timeout(300, dec_hard_timeout=True)
def verify(email):
    return verify_email(email, debug=True)#verify_email(email)

def waitUntil(condition, output): #defines function
    wU = True
    while wU == True:
        if condition: #checks the condition
            output
            wU = False
        time.sleep(60) #waits 60s for preformance
def internet(host="8.8.8.8", port=53, timeout=3):
    """
    Host: 8.8.8.8 (google-public-dns-a.google.com)
    OpenPort: 53/tcp
    Service: domain (DNS/TCP)
    """
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error as ex:
        print(ex)
        return False

df=pd.read_csv("LinkJobs-pt2.csv")


def emailz(b):
    df=b
    emails=b["Email"].tolist()
    domain=b["Website"].tolist()
    fname=b["Last Name"].tolist()
    #emails=["agneynalapat@gmail.com","bc@xyz.com","ab@xyz.com","c@xyz.com","b@xyz.com","a@xyz.com","abc@xyz.com","asd@xyz.com","bc@xyz.com","bc@xyz.com","agneynalapat123@gmail.com"]
    y2=0
    count=0
    flag=0
    dflag=0
    nflag=0
    catchflag=0
    #val=0
    for y1 in emails:
        
        #if(internet()==False):
                #waitUntil(internet()==True, emailz(b))
        print(y1)
        
        print("Count=",count)
        #print(domain[count])
        #print(y1)
        
        if fname[count] in y1:
            print("Same Name")
            nflag=1
        else:
            print("Name changed")
            nflag=0
        if domain[count-1] in y1:
                    
            print("Same Domain")
            dflag=1
        else:
            print("Domain Changed")
            dflag=0
        if count==0:
            nflag=0
            dflag=0
        print("NameFlag: ",nflag)
        print("DomainFlag: ",dflag)
        if(count%6==0 and dflag==0 or 1 and nflag==0):
            print("set flag 0")
            flag=0
        if(flag==0):
            time.sleep(5)
            try:
                
                
                if dflag==0:
                    test1, log1=verify_email("sad34"+y1)#, debug=True)
                    print("Test1")
                    time.sleep(5)
                    test2, log2=verify_email("5adasd34"+y1)#, debug=True)
                    print("Test2")
                    time.sleep(5)
                    val=test1 and test2
                    print(val)
                    df.at[y2,"Catch-All"]=val
                else:
                    df.at[y2,"Catch-All"]="False"
                        
                b, log3=verify_email(y1)#, debug=True)
                print(b)
                print(log3)
                df.at[y2,"LOG"]=log3
                
                
                df.at[y2,"Verify_Email"]=b
                
                    #df.at[y2,"Catch-All"]="catch"    
                    #print(df)    
                df.to_csv("VLinkJobs-pt2.csv", index=False)
                
                count=count+1 
                if(b==True):
                    if(val==False):
                        flag=1
                        df.at[y2,"Catch-All"]="True"
                        
                    else:
                        flag=1
                y2=y2+1
                if "Timeout" in log3:
                    time.sleep(600)       
                
                
                        
                    
            except Exception as e:
                print(e)
                y2=y2+1
                count=count+1 
                continue
        else:
            y2=y2+1
            count=count+1 
            continue
        
    return df

emailz(df)
#c.to_csv("BLR-Health&Social.csv", index=False)

    
