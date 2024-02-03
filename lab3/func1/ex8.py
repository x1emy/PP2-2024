def spy_game(nums): 
    index=0
    for a in nums:
        if a==0 and index<2:
            index+=1
        elif a==7 and index==2:
            return True
    return False
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))
