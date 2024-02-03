def uniq(nums):
    mylist=[]
    for i in nums:
        if i not in mylist:
            mylist.append(i)
    return mylist
print(uniq([1,2,3,4,4,4,4,6]))