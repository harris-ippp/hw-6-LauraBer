import requests
from bs4 import BeautifulSoup

url =  "http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2015/office_id:1/stage:General"
req = requests.get(url)
html = req.content
soup = BeautifulSoup(html, 'html.parser')

with open("ELECTION_ID", "w") as out: # we generate an empty file, and call it "out"
    for result in soup.find_all("tr", "election_item"): #loop over the elements in our defined url (soup) and find all rows that contain election_item.
        id_number = result["id"].split("-")[2] #create a new variable called id_number, store in it "id" from the URL, but only take position 2 once we seperated the content of "id" string with dashes (because we only want the number of "id")
        year = result.find("td", "year first").contents[0] #create a new variable called year, search for the cell called "year first" in each row in our results, return the content of this at position 0.
        out.write("{} {}\n".format(id_number, year)) #saves a file for everything now stored in "out" file, put it in a format that returns id_number and year
