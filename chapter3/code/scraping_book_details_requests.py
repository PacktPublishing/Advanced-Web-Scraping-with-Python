from lxml import html
import csv
import json
import requests

def parse(url):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	response = requests.get(url, headers=headers)
	doc = html.fromstring(response.content)
	title_xpath = '//*[@id="maincontent"]/div[3]/div/div[1]/div[1]/h1/span/text()'
	author_xpath = '//*[@id="maincontent"]/div[3]/div/div[1]/div[2]/div[2]/text()'
	date_xpath = '//*[@id="maincontent"]/div[3]/div/div[1]/div[2]/div[3]/text()'
	pages_xpath = '//*[@id="maincontent"]/div[3]/div/div[1]/div[2]/p[1]/text()'
	title = doc.xpath(title_xpath)[0]
	author = doc.xpath(author_xpath)[0]
	date = doc.xpath(date_xpath)[0]
	pages = doc.xpath(pages_xpath)[0]

	title = ' '.join(''.join(title).split()) if title else None
	author = ' '.join(''.join(author).split()) if author else None
	date = ' '.join(''.join(date).split()) if date else None
	pages = ' '.join(''.join(pages).split()) if pages else None
	
	data = {'Title': title,'Author': author,'Date': date,'Pages': pages}
	print(data)
	
	return data



def ScrapingBookData():

    bookList = ['big-data-and-business-intelligence/machine-learning-opencv',
                'big-data-and-business-intelligence/hands-generative-adversarial-networks-keras']

    extracted_data = []

    for i in bookList:
        url = "https://www.packtpub.com/" + i
        print("Processing: " + url)
        # Calling the parser
        parsed_data = parse(url)
        if parsed_data:
            extracted_data.append(parsed_data)
            #Save the collected data into a json file.
            file_json=open('book_data.json','w')
            json.dump(extracted_data,file_json,indent=4)

    # Writing scraped data book to csv file
    with open('scraped_book_data.csv', 'w') as csvfile:
        fieldnames = ['Title','Author','Date','Pages']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for data in extracted_data:
            writer.writerow(data)

if __name__ == "__main__":
    ScrapingBookData()