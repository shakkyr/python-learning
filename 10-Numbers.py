# lists

myArr = ["One", "Two", "One", 1, 100.3, True]

print(myArr[-1])  # last item

print(myArr[1:5]) # 'Two', 'One', 1, 100.3  slice

print(myArr[::2])  # ['One', 'One', 100.3]

myArr[0:3] = []  # cleans the first 3 elements of the list

print(myArr)

#! ============== append() =================

myNewArr = [1, 2 ,3 ,4 ,5 ,6 ]
myOldArr = [100, 33 , 43, 23, 456]

myNewArr.append(myOldArr)  #  [1, 2, 3, 4, 5, 6, [100, 33, 43, 23, 456]]
print(myNewArr.append(myOldArr))

#!======= extend() ===========

myNewArr = [1, 2 ,3 ,4 ,5 ,6 ]
myOldArr = [100, 33 , 43, 23, 456] # [1, 2, 3, 4, 5, 6, 100, 33, '', 23, 456]
myNewArr.extend(myOldArr)
print(myNewArr)

#! ============ sort() =============
y= [1, -1, 2, 13, 14, -22, 3434, 233]

y.sort()
print(y)  # [-22, -1, 1, 2, 13, 14, 233, 3434]
y.sort(reverse=True)
print(y)  # [3434, 233, 14, 13, 2, 1, -1, -22]


#! ========= copy =========
a = ["shadi", "Mays"]
b = a.copy()

#! ======count() ============
d = [1,2,3,1,1,3,4,5]
print(d.count(1)) # 3

#! index() ==========
e = ["Shadi", "Mays" , "Aws"]
print(e.index("Aws")) # 2

#!+++++ insert()  =======
f = [1, 2, 3,"A", "B"]
f.insert(4,"c")  # [1, 2, 3, 'A', 'c', 'B']
print(f)


#! ========= pop() ============

g = [1,2,3,4,5,"A"]
print(g.pop(-1)) #prints A
