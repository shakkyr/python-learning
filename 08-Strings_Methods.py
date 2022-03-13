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

b = 'shadi is learning python and react native and'

