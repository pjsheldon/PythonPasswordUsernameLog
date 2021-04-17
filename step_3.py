'''--------By: PJ Sheldon---------
	--------Date: 8/15/20---------
	step_3.py programming assignment 6
	SEC-290 Wilmington University'''

def usernamefind():
	with open("auth.log.1b") as t:              # opening the file 
		datafile = t.readlines()                # variable of what to read
	for line in datafile:                       # for loop for each in read
		if "Failed password" in line:           # if the line keyword "Failed password" is present in the line read
			start = line.find("invalid user ")  # find method for the start of the splice
			count = len('invalid user ')        # The index number of characters in "invalid user "
			namestart = start + count           # The index of the start of the splice + the number of charcters 
			end = line.find(" from")            # the end of the splice
			username = line[namestart : end]    # the splice 
			print(username)                     # display the spliced user name 
	t.close()                                   # close the file 

usernamefind()