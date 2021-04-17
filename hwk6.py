'''--------By: PJ Sheldon---------
	--------Date: 8/15/20---------
	hwk6.py programming assignment 6
	SEC-290 Wilmington University'''

# Dictionary for the program
nameofnames = {}                         

def usernamefind():
	with open("auth.log.1") as t:                # opening the file 
		datafile = t.readlines()                 # variable of what to read

	for line in datafile:                        # for loop for each in read
		
		if "Failed password" in line:            # if the line keyword "Failed password" is present in the line read
			start = line.find("invalid user ")   # find method for the start of the splice
			count = len('invalid user ')         # The index number of characters in "invalid user "
			namestart = start + count            # The index of the start of the splice + the number of charcters 
			end = line.find(" from")             # the end of the splice
			username = line[namestart : end]     # the splice 
			
			if username not in nameofnames:      # if the user name is not in dictionary
				value = 1                        # value will be equal to 1 the first time
				nameofnames[username] = value    # add the key (username) and value to the disctionary
			
			elif username in nameofnames:        # if the user name is in the dictionary
				value += 1                       # the value is added by one.
				nameofnames[username] = value    # add the key and value to dictionary
	t.close()                                    # closes the file 

# Self defined function 
usernamefind()                    

keys = nameofnames.keys() # syntax for the keys

for key in keys:          # for loop for the key of the dictionary 
# Display the statement 
	print('Attacker tried {} time(s) to log in as {}'.format(nameofnames[key], key))