import re
writeto = open("newtxt.txt", "a+")
readfrom = open("pcj_bounds_blue.txt", "r")

for line in readfrom: 
	if "background" in line: 
		writeto.write(line)

readfrom.close()
writeto.close()
writeto = open("newtxt.txt", "r+")

data=writeto.read().replace('\n', '')

match = re.sub(r"[a-zA-Z]+", "", data)
writeto.write(match)

writeto.close()

