import requests

url = "http://www.packtpub.com"
# Packages the request, send the request and catch the response
response = requests.get(url)
# Store the response in html variable
html = response.text
# Print the html
print(html)