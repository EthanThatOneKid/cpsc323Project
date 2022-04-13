txt = open("finalp1.txt")
f = open("finalp2.txt", "w")

line = txt.readline()
while(len(line)):
    if line != '\n':
        f.write(line)
    line = txt.readline()
