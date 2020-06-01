line = input()

output = ""

word_list = line.split()

for i in range(len(word_list)):
    newline = ""
    for j in range(len(word_list[i])):
        newline = newline + word_list[i][len(word_list[i])-1-j]
    output = output + newline
    if(i != len(word_list)-1):
        output = output + " "

print (output)
