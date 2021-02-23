x = [1,2,3]
mylists = ['streintakf',1,2,3,4,23.4,True, 'asr',[1,2,3] ]
mylists.append(["new item"])
list2 = ["x","y","z"]
mylists.extend(list2)
##print(mylists)
item = mylists.pop(0)
print(mylists)
print(item)
mylists.reverse()
print(mylists)
list3 = [3,4,2,1,67,8,5]
list3.sort()
print(list3)
matrix = [[1,2,3],[4,5,6],[7,8,9]]
#list comprehension
first_col = [row[0] for row in matrix]
print(first_col)
