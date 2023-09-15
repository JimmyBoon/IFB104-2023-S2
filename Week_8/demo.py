from urllib.request import urlopen
from re import findall

import urllib.request


url = "https://www.nasaspaceflight.com/"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

space_flight_file = urllib.request.urlopen(req)
space_flight_raw_bytes = space_flight_file.read()
space_flight_source_code = space_flight_raw_bytes.decode("UTF-8")
space_flight_file.close()

#print(space_flight_source_code)

titles = findall("<h2 class=.+?>.+?>(.*)?</a>", space_flight_source_code)
pages = findall("<h2 .+><a.+(https://.+)\">.+</a></h2>", space_flight_source_code)


for count in range(0, len(titles)):
    print(f"Story number {count + 1}:")
    print(titles[count])
    print("You can access this page here:")
    print(pages[count])
    print("\n\n")

    