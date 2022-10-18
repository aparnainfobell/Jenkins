# import pandas as pd
#
# data = {
#     'apples': [3, 2, 0, 1],
#     'oranges': [0, 3, 7, 2]
# }
# dataa = pd.DataFrame(data)
#
# dataa
# print(dataa)
#
# purchases = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])
#
# purchases
# print(purchases)
# print(pd.__version__)
#
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a)
#
# print(myvar,"myvarrrr")
# print(myvar[0],"000000000")
# # purchases.loc['june']
#
# a = [1, 7, 2]
#
# myvar = pd.Series(a, index = ["x", "y", "z"])
#
# print(myvar,"999999999")

#to save as json fotmat
#df.to_json('new_purchases.json')
# to save it as csv format
# data.to_csv('test.csv')
#
# first,second=0,1
# n = int(input("please give a number for fibonacci series : "))
# print("fibonacci series are : ")
# for i in range(0,n):
#     if i<=1:
#         result=i
#     else:
#       result = first + second;
#       first = second;
#       second = result;
#     print(result)

#taking input from the user
string = input("Enter a String : ")
vowels = 0  #variable to count number of vowels
consonants = 0 #variable to count number of consonants
for i in string:  #string iteration
    if i in ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):  #if character in string is vowel
        vowels+=1 #if vowel increment variable ‘vowel’ with one
    elif i.isalpha():  #checking if the character is alphabet
        consonants+=1  #if consonant increment variable ‘consonants’ with one
print("Vowels :",vowels,"Consonants:",consonants)
