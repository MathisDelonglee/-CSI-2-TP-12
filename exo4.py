def listSum(l):
    if len(l) == 0:
        return 0
    return listSum(l[1:])+l[0]

print(listSum([])) # 0
print(listSum([42])) # 42
print(listSum([3,1,5,2])) # 11
