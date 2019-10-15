from urllib.request import urlopen, Request

# Specify the url
url = "http://www.packtpub.com"
# This packages the request
request = Request(url)
# Sends the request and catches the response: response
response = urlopen(request)
# Extract the response using read()
html = response.read()
# Print the html
print(html)
# Closing the response
response.close()