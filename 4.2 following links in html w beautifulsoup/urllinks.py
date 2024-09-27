import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
position = int(input('Enter position: ')) - 1 # decrease number by 1 to get index
count = int(input('Enter count: '))

tag = soup('a') # anchor tag

for i in range(count): # for i in the range given by the position
    link = tag[position].get('href', None) # get the anchor tag in position input, find attribute href
    print('Retrieving: ', link) # print url retrieved

    html = urllib.request.urlopen(link, context=ctx).read() # reiterate code we initially used for reading URL input, but using link retrieved per iteration
    soup = BeautifulSoup(html, 'html.parser') # parse code from URL received
    tag = soup('a') # save links parsed as the new anchor tags