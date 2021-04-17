'''--------By: PJ Sheldon---------
	--------Date: 8/15/20---------
	step_1.py programming assignment 6
	SEC-290 Wilmington University'''

#
# opening file for reading
#

text_file = open("auth.log.1b")

#
# Read each line
#

contents = text_file.read()

#
# Display each line
#

print(contents)

#
# close the file
#

text_file.close()