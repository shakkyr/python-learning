# -----------------------------
# -- Strings Methods --
# ------------------------------

#  strip() rstrip()  lstrip()

a = "         I Love Python    "
print(a.strip())   # removes the white space from the string
print(a.rstrip())  #remove white space from  the right
print(a.lstrip())  # remove white space from left


a = "#@#@        I Love Python @#@#@#"

print(a.strip('@#'))

# title()  capitalize()

b = " i love 2d graphics and 3g design"

print(b.title())
print(b.capitalize())


## zfill()

j , k , l = '1' , '11' , '111'
print(j)
print(k)
print(l)

print(j.zfill(3))
print(k.zfill(3))
print(l.zfill(3))

# upper() lower()

n = 'shadi'
print(n.upper())
print(n.lower())

# split() rsplit() lsplit()

r = "I Love Python and php and mysql"
t = "I-Love-Python-and-php-and-mysql"

print(r.split())
print(r.split(' ', 2))
print(t.split('-', 2))
print(t.split('-'))

# center() takes 2 arguments

e = "Shadi"

print(e.center(8)) # adds spaces arround the string
print(e.center(9, '@')) # adds @ arround the string

# count()

a = (10,11,10,11,22)
b = 'shadi is learning python and react native and'
print(b.count('and'))
print(b.count('and',0,20)) # 0 "and"
print(b.count('and',0,40)) # 1 "and"
print(a.count(10))

# swapcase()

b = 'ShadI Is lEaRniNg pYtHon aNd rEacT'
print(b.swapcase())

# startswith() endswith()

b = 'ShadI Is lEaRniNg pYtHon aNd rEacT'
print(b.startswith('Is'))
print(b.startswith('Is',6,20))

# index(subString, Start, End)
print(b.index('I')) # index 4
print(b.index('I',5,40)) # index 6
# print(b.index('I',10,20)) # not found returns error stops the code

# find(subString, Start, End)

print(b.find('I')) # index 4
print(b.find('I',5,40)) # index 6
print(b.find('I',10,20)) # -1 it's not found

# rjust() ljust() adds spaces or charatcters befor/ after the string
n = "shadi"
print(n.rjust(10,"@"))
print(n.ljust(10,"2"))

# splitlines() returns a list from the string's lines 

e = """ First Line
Second line
Third Line
"""
r = "First Line \n Second Line \n Third Line"

print(e.splitlines())
print(r.splitlines())

# expandtabs() controll the added tabs

b = 'ShadI\tIs\tlEaRniNg\tpYtHon\taNd\trEacT' #false
c= 'Shadi Rada ' #true
d= 'Shadi rada ' #false
e= 'sjadi rada'

print(b.expandtabs(5))

# istitle()  isspace()

print(b.istitle())
print(c.istitle())
print(d.istitle())
print(e.isspace())

# isidentifier()
one = "ShadiRada"
two = "shad_Rada"
three = "shadi-Rada" # cant be as an identifier

print(one.isidentifier())
print(two.isidentifier())
print(three.isidentifier())


# isalpha() checks if the string is alpha petaal
# isalnum() checks if string contains both numbers and characters

v = 'asdasda'
b = 'safa2324'
print(v.isalpha()) # true
print(b.isalpha()) # false
