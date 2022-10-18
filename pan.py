# import pandas as pd
#
# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }
#
# df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
#
# print(df)

# lst = [1,1,1,2,2,3,3,3]
# content = []
# for i in lst:
#     if str(i)+" is repeated "+str(lst.count(i))+" times" not in content:
#         content.append(str(i)+" is repeated "+str(lst.count(i))+" times")
# for i in content:
#     print(i)

num = int(input("enter number:"))
if num%3 == 0:
  print("fizz - divisible by 3")

if num%5 == 0:
  print("fizz - divisible by 3")

if num%3 == 0 and num % 5 ==0:
  print("fizz - divisible by both 5 and 3")