
import requests

address="http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/"

for line in open("ELECTION_ID"): # run a loop over ELECTION_ID file
    # newvar=line.split() # create new variable and split each line where there are white spaces
    # print(newvar) # prints these lists
  newvar=line.split() # generate a new variable for "ELECTION_ID" that creates a list for each row of that file and splits the cells into elements of that list
  print(newvar[1]) # print the position 1 of each list (which is the year)
  year=newvar[1] # we call this position 'year'
  address_list=address.format(newvar[0]) # create new variable address_list, plug the position 0 of list 'newvar' into address. This generates an address for each of the election id's
  print(address_list) # print this address_list (to see how it looks like)

  response = requests.get(address_list) # create a variable called response, and call on address_list to read in that file
  file_name = year + ".csv" # create a new variable called file_name, its consists of the 'year' and the extension '.cvs' which makes sure that we save it as a .cvs file

  with open(file_name, "w") as out: # we take our file_name and call it "out" (temporarilly)
    out.write(response.text) # we save a file with the response content for each file_name
