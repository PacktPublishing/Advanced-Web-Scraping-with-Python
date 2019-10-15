from bs4 import BeautifulSoup
import requests
import csv

url = "http://packtpub.com"

csv_file = csv.writer(open("data_links.csv", "w"))
csv_file.writerow(["Section" , "Link"])

# Getting the webpage, creating a Response object.
response = requests.get(url)

# Extracting the source code of the page.
data = response.text

# Passing the source code to Beautiful Soup to create a BeautifulSoup object for it.
soup = BeautifulSoup(data, 'html.parser')

# use the 'find_all' function to bring back all instances of the 'a' tag in the HTML and store in 'tags' variable
# Extracting all the <a> tags into a list.
tags = soup.find_all('a')
tags = soup.find_all('a', {'class': 'nav-anchor'}) # only for url = "http://packtpub.com"

# Extracting URLs from the attribute href in the <a> tags.
for tag in tags:
	print(tag.get('href'))
	link = tag.get('href')
	text = tag.get_text()
	csv_file.writerow([text, link])
	
