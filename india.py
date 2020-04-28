import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime
from PIL import ImageTk,Image


def get_html_data(url):
  data=requests.get(url)
  return data

def get_corona_detail_of_india():
  url="https://www.mohfw.gov.in/"
  html_data=get_html_data(url)
  bs=bs4.BeautifulSoup(html_data.text,'html.parser')
  info_div=bs.find("div",class_="site-stats-count").find("ul").find_all("li")
  all_detail=""
  for item in info_div[0:4]:
    count=item.find("strong").get_text()
    text=item.find("span").get_text()
    print(text," : ",count)
    all_detail+=text+" : "+ count +"\n"
    #print(item)
    #print()
  return all_detail

def refresh():
  new_data=get_corona_detail_of_india()
  print("Refreshing...")
  mainLabel['text']=new_data


#print(get_corona_detail_of_india())

root=tk.Tk()
root.geometry("600x550")
root.iconbitmap("corona.ico")
root.configure(background="pink")
root.title("COVID-19 LIVE TRACKER-INDIA")
f=("poppins",25,"bold")

banner =ImageTk.PhotoImage(Image.open('banner.png'))
bannerLabel = tk.Label(root,image=banner)
bannerLabel.pack()

mainLabel=tk.Label(root,text=get_corona_detail_of_india(),font=f,bg='pink')
mainLabel.pack()

rebtn=tk.Button(root,text="REFRESH",font=f,relief='raised',command=refresh)
rebtn.pack()

root.mainloop()

