import urllib.request
import time
import math
from bs4 import BeautifulSoup
add = 50
val=100
while val<1200:
    add+=50
    data = urllib.request.urlopen("https://api.thingspeak.com/update?api_key=Q0P8D9GLKCHSMR7B&field1="+str(val))
    print(data)
    val += add + 50
    time.sleep(5)
