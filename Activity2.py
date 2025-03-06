def match(words):
    count=0
    list1=[]
    for i in words:
        if len(i)>2 and i[0]==i[-1]:
            count=count+1
    return count
print(match(["aea","Vivienne", "Hello" , "121"]))
