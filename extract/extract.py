#PROGRAM TO EXTRACT EMAILS AND PHONE NUMBERS FROM A SITE

import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def extract_data(url):
	# Send a GET request to the website
	response = requests.get(url)

	# Create BeautifulSoup object for parsing the HTML content
	soup = BeautifulSoup(response.content, 'html.parser')

	# Extract phone numbers using regular expression
	phone_numbers = re.findall(r'\b(?:\+?\d{1,3}[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}\b', soup.get_text())

    # Extract email addresses using regular expression
	email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', soup.get_text())

	# Extract links using regular expression
	links = []
	for a_tag in soup.find_all('a', href=True):
		link = a_tag['href']
		if link.startswith(('http://', 'https://')):
			links.append(link)
		else:
			absolute_link = urljoin(url, link)
			links.append(absolute_link)

	return phone_numbers, email_addresses, links

# Example usage
website_url = input("enter website: ")
phone_numbers, email_addresses, links = extract_data("https://www."+ website_url)

# Get the desired file name from the user
file_name = input("Enter the file name to store the details: ")

print("\nPhone Numbers:")
for number in phone_numbers:
    print(number)

print("\nEmail Addresses:")
for email in email_addresses:
    print(email)

print("\nLinks:")
for link in links:
    print(link)

# Write the extracted details to the file
with open(file_name, 'w') as file:
    file.write("Phone Numbers:\n")
    for number in phone_numbers:
        file.write(number + "\n")
   
    file.write("\nEmail Addresses:\n")
    for email in email_addresses:
        file.write(email + "\n")
   
    file.write("\nLinks:\n")
    for link in links:
        file.write(link + "\n")
        
print("Extraction on", website_url, "completed. Details are stored in the file:", file_name)
