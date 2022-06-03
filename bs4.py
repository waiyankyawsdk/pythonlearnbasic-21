import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.thedigitalcatonline.com/blog/2014/05/19/method-overriding-in-python/")
# print(response)
# print(response.content)
# print(response.status_code)

soup = BeautifulSoup(response.content, "html.parser")
print(soup)
#prettify
print(soup.prettify())

# find('a')
# find_all("img") #file type
# find_all("div") #div tag
# find_parent("a")
# find_next_siblings("a")

cards = soup.find_all("div",attrs={"class":"m-srp-card__container"})

for card in cards:
#print(card)

    price = card.find("div",attrs={"class":"m-srp-card__price"})
    print(price.text)

    title = card.find("div",attrs={"class":"m-srp-card__title__bhk"})
    print(title.text)

    title = card.find("div",attrs={"class":"m-srp-card__title__bhk"})
    print(title.text.strip("\n"))

    carpet_area = card.find("div",attrs={"class":"m-srp-card__summary__info"})
    print(carpet_area.text)

    data = "{} {} {}".format(title.text.strip("\n"),price.text,carpet_area.text)