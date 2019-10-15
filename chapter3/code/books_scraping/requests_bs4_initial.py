from bs4 import BeautifulSoup
import requests

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

        # We pass the HTML content of the web to a BeautifulSoup() object
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
    # Decide here what you want to do with the content
    return



