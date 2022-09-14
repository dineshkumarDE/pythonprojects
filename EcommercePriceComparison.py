import requests as r
from bs4 import BeautifulSoup
import pandas as pd
from tabulate import tabulate

def read_page(url):
  header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
  response=r.get(url,headers=header)
  soup=BeautifulSoup(response.content,"html.parser")
  return soup

def check_price_amazon(url):
    soup=read_page(url)
    prd_name=soup.find("span" ,{"id" : "productTitle"} ).text
    prd_price=soup.find("span" ,{"id" : "price"}).text
    return(["amazon",prd_name,prd_price])

def check_price_flipkart(url):
    soup=read_page(url)
    prd_name=soup.find("span" ,{"class" : "B_NuCI"} ).text
    prd_name=prd_name.replace('&nbsp;','')
    prd_price=soup.find("div" ,{"class" :"_30jeq3 _16Jk6d"}).text
    return(["flipkart",prd_name,prd_price])
    

prd_dtl_lst=[]

prd_dtl_lst.append(check_price_amazon("https://www.amazon.in/Alchemist-Paulo-Coelho/dp/8172234988/ref=sr_1_3?keywords=alchemist&qid=1663180675&s=books&sprefix=alchemis%2Cstripbooks%2C204&sr=1-3"))
prd_dtl_lst.append(check_price_flipkart("https://www.flipkart.com/alchemist/p/itmfc9jxsc7dckfm?pid=9788172234980&lid=LSTBOK9788172234980YN61C7&marketplace=FLIPKART&q=alchemist&store=bks&srno=s_1_2&otracker=search&otracker1=search&fm=search-autosuggest&iid=85b63d8a-f347-4e0f-a5b3-163bb5d7fbe9.9788172234980.SEARCH&ppt=sp&ppn=sp&ssid=s1u9zzntdc0000001663180689333&qH=132b133aafe31bcf"))
df = pd.DataFrame(prd_dtl_lst,columns=['vendor','product','price'])
print(tabulate(df,headers='keys',tablefmt='psql'))