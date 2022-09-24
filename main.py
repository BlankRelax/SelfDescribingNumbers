num_to_test = 	6210001005
no_of_zeros = 0
no_of_ones = 0
no_of_twos = 0
no_of_threes = 0
no_of_fours = 0
no_of_fives = 0
no_of_sixs = 0
no_of_sevens = 0
no_of_eights = 0
no_of_nines = 0

digitsarray = []
for digit in str(num_to_test):
    digitsarray.append(int(digit))
    if digit ==str(2):
        no_of_twos+=1
    elif digit ==str(1):
        no_of_ones+=1
    elif digit == str(0):
        no_of_zeros+=1
    elif digit == str(3):
        no_of_threes+=1
    elif digit == str(4):
        no_of_fours+=1
    elif digit == str(5):
        no_of_fives+=1
    elif digit == str(6):
        no_of_sixs+=1
    elif digit == str(7):
        no_of_sevens+=1
    elif digit == str(8):
        no_of_eights+=1
    elif digit == str(9):
        no_of_nines+=1
print(digitsarray)
if digitsarray[0] == no_of_zeros and digitsarray[1] == no_of_ones and digitsarray[2] == no_of_twos and digitsarray[3] == no_of_threes and digitsarray[4] == no_of_fours and digitsarray[5] == no_of_fives and digitsarray[6] == no_of_sixs and digitsarray[7] == no_of_sevens and digitsarray[8] == no_of_eights and digitsarray[9] == no_of_nines:
    print("y")
else:
    print("n")
