txt = "Hello World"
x = txt.strip('Hd')
print(x.upper())
fname = 'Joe'
age = 36
name2 = "Mary"
age2 = 32
txt2 = "My name is {}, I'am {}"
txt3 = "My name is {}, I'am {}"
print(txt2.format(fname, age))
print(txt3.format(name2, age2))

#név = input('Hogy híjják kendet? ')
#kor = input('És hány éves kend? ') # itt még stringet kapunk
#kor = int(kor) # átalakítjuk egész számmá, azaz int-té
#születési_év = 2020 - kor
#print(név, ', kend ', születési_év, '-ban született.', sep='')

dict = {'fname': 'Zara', 'lname': 'First'}


def my_function(dict):
    print("His last name is " + dict["lname"])


my_function(dict)

negyzet = lambda x: x * x
print(negyzet(512))

#mindenből mindent beimportálsz
#from math import *
#csak a math-t hívod meg:
import math

# ez csak akkor használható, ha "from math import *" -> print(sqrt(262144))
print(math.sqrt(262144))
