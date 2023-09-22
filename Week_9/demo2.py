from urllib.request import urlopen
from re import findall
import urllib.request
import database

def get_website_source_code(url):
    """Returns the source code of a website as a string."""

    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

    file = urllib.request.urlopen(req)
    raw_bytes = file.read()
    source_code = raw_bytes.decode("UTF-8")
    file.close()
    return source_code


def get_titles():
    """Returns a list of titles from the website."""

    source_code = get_website_source_code("https://www.executivetraveller.com/")

    titles = findall("class=\"margin-btm-half\"><a href=\"https:.+?>(.+)<\/a>", source_code)
    return titles

#database.create_title_database("Headline.db")

for title in get_titles():
    database.add_title_to_database("Headline.db", title)

for title in database.get_titles_from_database("Headline.db")[0:4]:
    print(title)




