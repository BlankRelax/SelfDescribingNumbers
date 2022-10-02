def func(num):
    s = str(num)

    for i in range(len(s)):
        temp_char = s[i]
        b = int(temp_char)
        print(b)
        count = 0
        for j in range(len(s)):
            temp = int(s[j])
            if temp ==i: # compares temp with the index of the number
                count+=1
        if (count !=b):
             return False
    return(True)

if func(3211000):
    print("yes")



