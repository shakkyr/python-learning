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