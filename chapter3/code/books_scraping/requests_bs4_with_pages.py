from bs4 import BeautifulSoup
import requests
import pandas as pd

# Class names representing product ratings
star = ["One", "Two", "Three", "Four", "Five"]

bookList = []
url_page = "http://books.toscrape.com/catalogue/page-{}.html"
url = "http://books.toscrape.com/catalogue/"

def starToInt (rating):
    """
    Convert a textual rating to a numerical rating
	Returns the equivalent number, or 0, if the rating is not valid
    """
    try:
        return star.index(rating) + 1
    except:
        return 0
		
		
def processUrl(url):
    """
    Upload and process the content of a URL using request.
    Show an error message if you cannot load the page
    """
    # http request
    req = requests.get(url)

    # We verify the request returns a Status Code = 200
    statusCode = req.status_code
    if statusCode == 200:

        # We pass the HTML content of the web to a BeautifulSoup () object
        html = BeautifulSoup(req.text,"lxml")

        # We process the downloaded HTML
        return processHTML(html,url)        

    else:
        print ("ERROR {}".format(statusCode))

def processHTML(html, url=""):
    """
    Process the HTML content of a web page
    html is a BS4 object
    url is the URL of the page contained in html_doc
    """
    book = {}
    
    productMain = html.select_one(".product_main")

    # Title
    title = productMain.select_one("h1").text
    book['title'] = title

    # Price
    price = productMain.select_one("p.price_color").text
    book['price'] = price[2:]
    
    # Assessment
    # 1. Get class
    ratingClasses = productMain.select_one("p.star-rating")["class"]
    
    # 2. We get with the intersection
    ratingText = list(set(ratingClasses).intersection(set(star)))
    
    # 3. We convert it to a numerical value
    if (len(ratingText)==1):
        book['assessment'] = starToInt(ratingText[0])
    else:
        book['assessment'] = 0
		
	# Processing the description makes us look for the sibling of an element
	# Product description
    # 1. We look for the element that takes product product description
    productDescription = html.find(id="product_description")
    
    # 2. We are looking for the next sibling with tag p
    if productDescription is None:
        book['descripcion'] = ""
    else:
        book['descripcion'] = productDescription.find_next_sibling('p').text
        
    print(book)
	
    return book

	
def processCatalog(url, prefix):
    """
    Returns False if we have reached the end of the catalog, True otherwise
    """
    # We make the request to the web
    response = requests.get(url)

    # We verify that the request returns a Status Code = 200
    statusCode = response.status_code
    if statusCode == 200:

        # We pass the HTML content of the web to a BeautifulSoup () object
        html = BeautifulSoup(response.text,"lxml")
        
        # We process the downloaded HTML
        books = html.select('article.product_pod')
        for prod in books:
            link = prod.select_one('h3 > a')
            book = processUrl(prefix+link['href'])
            book['link'] = prefix+link['href']
            bookList.append(book)
        return True
    
    if statusCode == 404:
        return False
 
if __name__ == "__main__":

	processUrl("http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html")
	
	for i in range(1,5):
		processCatalog(url_page.format(i), url)
		
	for book in bookList:
		print(book)
	
	#Finally we will load all the data in a panda dataframe to process it, extract information and save it to a CSV

	df = pd.DataFrame(bookList)
	df.to_csv("bookList.csv", sep=";", index=False)



