import requests
from bs4 import BeautifulSoup

URL = "insert the url of the wanted site"

# These are the css classes I need for my research
CLASS_TITLES = ""
CLASS_PRICES = ""
CLASSs_LINKS = ""

r = requests.get(URL).text
soup = BeautifulSoup(r, "html.parser")

# Retrieving the informations I need to filter the cars
titles_list = [title.text for title in soup.find_all("h2", class_=CLASS_TITLES)]
prices_list = [price.text for price in soup.find_all("p", class_=CLASS_PRICES)]
links_list = [link["href"] for link in soup.find_all("a", href=True, class_=CLASS_LINKS)]

# Merging the 3 lists into one dictionary
car_dict = dict(zip(zip(titles_list, prices_list), links_list))
for car in car_dict.items():
    print(car)
