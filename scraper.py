from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import json
filename = "recipe.json"
f = open(filename,"w")
url_1="https://www.allrecipes.com/recipe/11701/chicken-and-cold-noodles-with-spicy-sauce/?internalSource=rotd&referringId=95&referringContentType=recipe%20hub"
#url_1="https://www.allrecipes.com/recipe/234592/buffalo-chicken-stuffed-shells/"
#url_1 ="https://www.allrecipes.com/recipe/10137/chocolate-frosted-marshmallow-cookies/?internalSource=rotd&referringId=840&referringContentType=recipe%20hub"
uClient = uReq(url_1)
page_html = uClient.read()

page_soup = soup(page_html, "html.parser")

title = page_soup.find("section",{"class":"recipe-summary clearfix"})
real = title.find("h1",{"class":"recipe-summary__h1"}).text.strip()
stuff = page_soup.findAll("span",{"class":"recipe-ingred_txt added"})
title={"title":real }
print (title) 
json.dump (title,f) 
print("********************************************************************")
for i in stuff:
    output = { "ingedients":i.text.strip()}
    print (output)
    json.dump (output,f)
print("********************************************************************")
direction = page_soup.findAll("span",{"class":"recipe-directions__list--item"})
for i in direction:
    direction = {"direction":i.text.strip()}
    print(direction)
    json.dump(direction,f)
f.close
uClient.close()