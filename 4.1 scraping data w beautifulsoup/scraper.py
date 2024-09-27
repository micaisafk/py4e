from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
sum = 0
tags = soup('span')
for tag in tags:
    # Code provided by instructor:
    #print('TAG:', tag)
    #print('Attrs:', tag.attrs)
    #print('Contents:', tag.contents[0])

    sum = sum + int(tag.contents[0])

print(sum)
