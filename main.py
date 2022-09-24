num_to_test = 1210

s = str(num_to_test)


digitsarray = []

for digit in s:
    digitsarray.append(int(digit))
print(digitsarray)
for i in range(len(s)):
    b=0
    temp_char = s[i]
    print(temp_char)
    for k in range(0,len(s)):
        print(s[k])
        if temp_char == s[k]:
            b+=1
    if digitsarray[i] == b:
        print("yes")
    else:
        print("no")


#print(digitsarray)
#if digitsarray[0] == no_of_zeros and digitsarray[1] == no_of_ones and digitsarray[2] == no_of_twos and digitsarray[3] == no_of_threes and digitsarray[4] == no_of_fours and digitsarray[5] == no_of_fives and digitsarray[6] == no_of_sixs and digitsarray[7] == no_of_sevens and digitsarray[8] == no_of_eights and digitsarray[9] == no_of_nines:
 #   print("y")
#else:
 #   print("n")


