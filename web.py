import requests  #requests for web scraping
from bs4 import BeautifulSoup  #manipulate web scraping 
import pandas as pd  # change it in tabular data

current_page=1  # choose the page to start

data=[] #given data in list form

proceed=True  # if the proceed data is true

while(proceed): #making a while as the proceed is true
    print("Currently scraping page: "+str(current_page)) # as the current_page = 1 and the current page in string

    url="https://books.toscrape.com/catalogue/page-"+str(current_page)+".html" # html page of the url

    proxies="" # to make your IP address hidden

    page=requests.get(url,proxies=proxies) #requesting the web page by the given url, as the proxies and url is requested to get

    soup=BeautifulSoup(page.text,"html.parser") #by beautifulsoup, parser the html page in text
    
    if soup.title.text == "404 Not Found": #if proceed=false as page doesn't exist
        proceed = False
    else: #if proceed=true 
        all_books = soup.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") #find all the pages in web, the "class" is extracted from inspect of web

        for book in all_books: # detailing evey book
            item = {} # given item in dictionary 

            item['Title'] = book.find("img").attrs["alt"] #from item find: title,image,attributes 

            item['Link'] = "https://books.toscrape.com/catalogue/"+book.find("a").attrs["href"] #place the href from inspect to get link of the item

            item['Price'] = book.find("p", class_="price_color").text[2:] #slysing of the price

            item['Stock'] = book.find("p", class_="instock availability").text.strip() #the item is in stock or not we have to strip it.

            data.append(item) #append the dictionary item to list data

    current_page = current_page+1 #make a loop of pages as it run 
    
df=pd.DataFrame(data) #dataframe is created by pandas
df.to_excel("books.xlsx") # excel sheet is created or we can use csv file instead.
 