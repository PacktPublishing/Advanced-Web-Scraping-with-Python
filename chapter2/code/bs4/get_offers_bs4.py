from bs4 import BeautifulSoup
import requests

def getOffers(url):
  # We make the request to the page
  req = requests.get(url)
  # We verify that the request returns a Status Code = 200 (200 = Ok)
  statusCode = req.status_code
  if statusCode == 200:
    # We pass the HTML content of the web to a BeautifulSoup object
    html = BeautifulSoup(req.text, "html.parser")
    # We get all the div elements with class "offer-box"
    elements = html.find_all('div', {'class': 'offer-box'})
    # We go through all the entries to extract the title, description and link
    for item in elements:
      title = item.find('h3').getText()
      description = item.find('p').getText()
      link = item.find('a').get('href')

      # Print title,link and description
      print("Title....: " + title)
      print("Link:.....: " + link)
      print("Description:.....: " + description)
      print("**********************************")
  else:
    # If the page does not exist we show the error
    print("The url " + url + " gives an error %d" % statusCode)

getOffers("https://www.packtpub.com/offers")