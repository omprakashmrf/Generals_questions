# converting interger into decimal
import decimal
interger=10
a=decimal.Decimal(interger)
print(a)
print(type(a))

# converting string into decimal
string="123456"
b = decimal.Decimal(string)
print(b)
print(type(b))


# reverse string using slice 
main_string="python programming"
reverse_string=main_string[::-1]
print(reverse_string)

# count the vawel
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count=0

for i in range(len(word)):
    if word[i] in vowel:
        count+=1
print(count)

# count the consonant in the word
vowel = ['a', 'e', 'i', 'o', 'u']
word = "programming"
count=0

for i in range(len(word)):
    if word[i] not in vowel:
        count+=1
print(count)


# found the number of occurence
word= "python"
charactor = "p"
count=0

for i in word:
    if i==charactor:
        count+=1
print(count)     

# find the max number in list
aa=[3,44,6,8]
max_number = aa[0]
for i in aa:
    if max_number < i:
        max_number = i
        
#max_number=max(aa)
print(max_number)


aa=[3,44,6,8]
min_number = aa[0]
for i in aa:
    if min_number > i:
        min_number=i
        
#min_number=max(aa)
print(min_number)


# find the middle element in the list 
ll=[3,6,80,9,12]
middleplace = int(len(ll)//2)
value=ll[middleplace]
print(value)

# converting list into string 
bb=['3','5','7','8','9']

print("".join(bb))



#max_number=max(aa)
print(max_number)


aa=[3,44,6,8]
min_number = aa[0]
for i in aa:
    if min_number > i:
        min_number=i
        
#min_number=max(aa)
print(min_number)


# find the middle element in the list 
ll=[3,6,80,9,12]
middleplace = int(len(ll)//2)
value=ll[middleplace]
print(value)

# converting list into string 
bb=['3','5','7','8','9']
print("".join(bb))


# check anagram 
str1="Listen"
str2="silent"

abc=list(str1.upper())
cde=list(str2.upper())
abc.sort()
cde.sort()

if abc==cde:
    print(True)
else:
    print(False)

# check polindrom
str1 = "kayak".lower()
str2 = "kayak".lower()

if str1==str2[::-1]:
    print(True)
else:
    print(False)
    

#count spaces in the string     
string = "P r ogramm in g "
print(string.count(" "))

#count space and char and number 
import re 
name = 'Python is 1'
#count_dict = {"char": [], }
digitcount=re.sub("[^0-9]", "", name)
lettercount= re.sub("[^a-zA-Z]", "", name)
spacecount = re.findall("[ \n]", name)
print(len(digitcount), len(lettercount), len(spacecount))
#for i in name:


# find all special charactor    
import re
spChar = "!@#$%^&*()"
allspchar=re.sub("[\w]", "", spChar)
print(len(allspchar))    


string ="C O D E"
spaces = re.compile(r'\s+')
sss=re.sub(spaces, "", string)
print((sss))

floor = 3
h = floor*2-1

for i in range(1, floor*2, 2):
    print(("{:^{}}").format('*'*i, h))

from random import shuffle
lst = ['Python', 'is', 'Easy']
shuffle(lst)
print(lst)
    

        

