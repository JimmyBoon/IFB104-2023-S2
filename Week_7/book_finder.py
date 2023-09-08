#---------------------------------------------------------------------
#
# Book Finder
#
# This exercise gives you practice at extracting elements from web
# documents and using them to create your own HTML file.
#
# Here we will extract some simple elements from the Project Gutenberg
# web site.  Project Gutenberg is an online library of books which
# are in the public domain and hence are free to download.  Its
# home page displays several of the latest books added to the library.
# Our goal is to extract the titles and authors of the latest
# three books and write them to a new web document.
#
# By examining the HTML source code of the Project Gutenberg home page
# (https://www.gutenberg.org/), we can discover that the latest
# book titles and authors appear in the following mark-up:
#
#   <h5>TITLE by AUTHORS</h5>
#
# These fifth level headings are easy to find because there
# are no other mark-ups of this form in the page.
# 
# Your task is to extract details of the three latest books
# marked-up in this way and use them to generate a new web
# document that lists them.  The generated document must contain
# all the standard sections used in HTML documents.
#
# Complete the code below by replacing the "pass" statements.
#

# Import the necessary URL function
from urllib.request import urlopen


# ----------
# Step 1: Get the source HTML document

# # Download and open the source document from Project Gutenberg
url = 'https://www.gutenberg.org/'
gutenberg_file = urlopen(url) # access web document
gutenberg_raw_bytes = gutenberg_file.read() # extract raw data
gutenberg_source_code = gutenberg_raw_bytes.decode("UTF-8") # interpret as Unicode chars
gutenberg_file.close() # close the web document

# ----------
# Step 2: Extract the first three book's titles & authors

# Define the HTML tags we want to find in the source document
pass

# Use the string "find" function to locate the position of the
# title & authors of the first book in the source document
pass

# Slice out the first book's title & authors from the source
# document and save the details in a variable
pass

# Use the string "find" function to locate the position of the
# title & authors of the second book in the source document,
# remembering to start searching after the position of the first
# book
pass

# Slice out the second book's title & authors from the source
# document and save the details in a variable
pass

# Use the string "find" function to locate the position of the
# title & authors of the third book in the source document,
# remembering to start after the position of the second book
pass

# Slice out the third book's title & authors from the source
# document
pass


# ----------
# Step 3: Create the contents for the target HTML document

# Define the contents of the HTML document, with placeholders for
# the book details

books_html = '''<!DOCTYPE html>

<!-- This is an automatically generated HTML document -->

<html>

  <head>
      <title>New Books from Project Gutenberg</title>
  </head>
  
  <body>
  
      <h1>New Books available from
      <a href="https://www.gutenberg.org/">Project Gutenberg</a></h1>

      <!-- The following list was extracted automatically from
           https://www.gutenberg.org/ -->

      <ol>
        <li>FIRSTBOOK</li>
        <li>SECONDBOOK</li>
        <li>THIRDBOOK</li>
      </ol>

  </body>
</html>'''

# Replace the three placeholders with the actual book details
pass


# ----------
# Step 4: Write the target HTML document

# Open the target HTML file for writing as Unicode
target_file = 'new_books.html'
books_file = open(target_file, 'w', encoding = 'UTF-8')

# Write the document's contents to the file and tell the
# user
books_file.write(books_html)
print('\nDone!\n\nYou can view the output in file', target_file, '\n')

# Close the target HTML file (which you can now view in
# your favourite web browser)
books_file.close()

