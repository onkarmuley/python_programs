#This program is to use functions available in re package for regular expressions
import re

#example 1 - search a word that starts with m and having 3 characters
str = 'man net mop the let'
obj = re.search(r'm\w\w', str)
if obj:
    print(obj) # this will give index where 1st occurrence matched 0 to 3
    print(obj.group()) # this will give man as output
else:
    print('Not found')

#example 2 - to find all words where starts with m and having 3 characters
str = 'man net mop the let'
lst = re.findall(r'm\w\w', str)
print(lst) #output - man mop in list

#example 3 - to find if starts with m and having 3 characters
str = 'man net mop the let'
obj = re.match(r'm\w\w', str)
if obj:
    print(obj) # this will give index where 1st occurrence matched 0 to 3
    print(obj.group()) # this will give man as output
else:
    print('Not found')

#example 4 - get all non-numeric from below string
str = 'gopi 2222 vinay 2345 abc 89834'
lst = re.findall(r'\D+',str)
print(lst)

#example 5 - get all names starting with 'an' or 'ak'
str = 'anil akhil anant arun arundhati abhijit ankur aniket arav'
lst = re.findall(r'a[nk]\w+',str)
print(lst)

#example 6 - get DOB from below list
str = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000, Ram 9 9-9-1988'
lst = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(lst)

#example 7 - get id from below list
str = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000, Ram 9 9-9-1988'
lst = re.findall(r' \d{1,2} ',str)
print(lst)

#example 8 - get name from below list
str = 'Vijay 20 1-5-2001, Rohit 21 22-10-1990, Sita 22 15-09-2000, Ram 9 9-9-1988'
lst = re.findall(r'\D+ ',str)
print(lst)

#example 9 - split a string when number is found
str = 'gopi 2222 vinay 9228 subba rao 898998'
list = re.split(r'\d+',str)
print(list)

#example 10 - substitute string with another string
str = 'he is smart'
str1 = re.sub('smart','clever',str)
print(str1)
