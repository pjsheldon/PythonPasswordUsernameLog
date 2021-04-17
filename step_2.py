'''--------By: PJ Sheldon---------
	--------Date: 8/15/20---------
	step_2.py programming assignment 6
	SEC-290 Wilmington University'''


# check to see "Failed password" is in each line 

def passwordfind():
	with open("auth.log.1b") as t:      # opening the file
		datafile = t.readlines()        # variable of what to read 
	for line in datafile:               # for loop for each in read
		if "Failed password" in line:   # if the line keyword "Failed password" is present in the line read
			print(line)                 # display the line that has the keyword 
	t.close()                           # make sure to close the file at theend of the search

passwordfind()                          # self defined function