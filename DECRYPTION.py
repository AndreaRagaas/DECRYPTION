#Pseudocode
#ask the user for input
input_str = input("Write the text that you wanted to decrypt: ")
output_str = ""
#check each character
for i in range(len(input_str)):
#if *, change to a
    if input_str[i] == "*":
        output_str += "a"
#if &, change to e
    elif input_str[i] == "&":
        output_str += "e"
#if #, change to i
    elif input_str[i] == "#":
        output_str += "i"
#if +, change to o
    elif input_str[i] == "+":
        output_str += "o"
#if !, change to u
#print output