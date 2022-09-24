num_to_test = 21200
no_of_twos = 0
no_of_ones = 0
no_of_zeros = 0
digitsarray = []
for digit in str(num_to_test):
    digitsarray.append(int(digit))
    if digit ==str(2):
        no_of_twos+=1
    elif digit ==str(1):
        no_of_ones+=1
    elif digit == str(0):
        no_of_zeros+=1

if digitsarray[0] == no_of_zeros and digitsarray[1] == no_of_ones and digitsarray[2] == no_of_twos:
    print("y")
else:
    print("n")
