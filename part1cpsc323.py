txt = open("finalp1.txt")
f = open("finalp2.txt", "w")

line = txt.readline()
while(len(line)):
    #removes blank lines
    if line != '\n':
        #remove spaces in the beginning of the string
        line = line.lstrip()
        f.write(line)
    line = txt.readline()
