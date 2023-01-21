# Numbers
# integers 1,6,9
# float 1.5 6.90
# complex 5+2j .... 
# print(500+890*6-5)
# print(7+9.08)
# print(8**2)
# print(6/4)
# print(6//4)
# print(6%4)

# variables
#watch = 300+40
#name = 'mayuri'
#watch1, watch2=34, 67
#print(watch1/8)
#print(name)

# Strings

word='  , im mayuriPalasingam  '
#word2='hi dude ,whys didn't you come'  ... single code not work 
word2="hi dude ,whys didn't you come"
para="""this  
is 
my
""" # want to write 3 lines
print(word2)
print(para)

# araays
print(word[2])
print(word[-7:-1]) # start & end - mean start wid last / positive number ; start wid first
print(len(word)) # no of letters
print(word.strip()) # can delete the space
print(word.upper()) # capital letter
a="puvishana"
print(a)
print(a.replace('u','a')) # methods
print('a' in word)
print(word2+word)

# boolean

print(1==78)

# operations arithmetic, =,< > >= <= and or not 
num1 = 10
num2 = num1 + 20
print(num2)
 # casting 
a=float (100)
b=int(10.09) # without int output is 10.09
print(a, b)
print(type(a))


#list
fruits = ['apple', 'mango', 'orange']
print(fruits)
fruits[1]='sana'
fruits.append("new")
print(fruits)

number=[1,6,7,3,5]
number.sort()
print(number)

#tuples
fruits = ('apple', 'mango', 'orange')# list and tuble are equal bt we cant assignt the item from tupes(list can modify ,delete)

#set
fruits = {'apple', 'mango', 'orange'} #  not fixed index number, output will come randomly

#dictionary can strore data then can use
ma_data={
    "name":"puvi akka" ,# value,key
    "age" : "34"

}
print(ma_data)

print(ma_data.get("name"))

#functions def(key word)
def addiing(a, b):

    print(a+b)

addiing(4,45)
addiing(1,2)


#loops
#for
name='mayuriii'
for letters in name:
    print(letters)

a=[2,3,4]
for number in a:
    print(number)

b='............................................................................'
print(b)
for num in range(3):
    print(num)