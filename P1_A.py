line = input()

newline = ""

for i in range(len(line)):
    newline =  newline + line[len(line)-1-i]

print (newline)
