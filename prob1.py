'''
Write a function to count all the letters,digits and special symbol from given string
input:P@#ynn26at^&i5ve
'''
input_='P@#ynn26at^&i5ve'
letter=digits=special=0
print(len(input_))
for i in range(len(input_)):
    
    if(input_[i].isdigit()):
        digits=digits+1
    elif(input_[i].isalpha()):
        letter=letter+1
    else:
        special=special+1

print("Total Number of letter in this String :", letter)
print("Total Number of Digits in this String :", digits)
print("Total Number of Special Characters in this String :", special)


        

