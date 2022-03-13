# whe can't concatenate string with digit

name = "shadi"
age = 35
rank = 10

print("my name is: " + name) # my name is: shadi
# print("my name is: " + name + "my age is:" + age ) # TypeError: can only concatenate str (not "int") to str

print("my name is: %s" % "shadi" )
print("my name is: %s" % name )
print("my name is: %s and my age is: %d" % (name, age) )
print("my name is: %s and my age is: %d and my rank is: %f" % (name, age, rank) )

# %s =>String
# %d =>Number
# %f =>Float

n = 'shadi'
l =  'python'
y = 10

print("my name is %s and im learning %s have %d experince" % (n,l,y))

num  = 10

print('my num is: %d' % num)  # my num is: 10
print('my num is: %f' % num)  # my num is: 10.000000
print('my num is: %.3f' % num) # my num is: 10.000

w = "shadi rada is here"

print('my saying is: %s' % w)
print('my saying is: %.6s' % w)

#! new ways

print("my name is: {}" .format(n) )
print("my name is: {:s} and my age is: {:.3f}" .format(n, y) )

a, b, c = "one", 'two', 'three'

print("hello {} {} {}".format(a,b,c))  # hello one two three
print("hello {1} {2} {0}".format(a,b,c)) # hello two three one
print("hello {2} {0} {1}".format(a,b,c)) # hello three one two

x, y, z = 10, 20 ,30

print("hello {} {} {}".format(x,y,z))  # hello 10 20 30
print("hello {1} {2} {0}".format(x,y,z)) # hello 20 30 10
print("hello {0:.3f} {0:f} {1:f}".format(x,y,z)) # hello 10.000 10.000000 20.000000


#! version 3.6+

myName = "shadi"
age = 35

print("my name is: {myName} and my age is: {age}")  # my name is: {myName} and my age is: {age}
print(f"my name is: {myName} and my age is: {age}") # my name is: shadi and my age is: 35