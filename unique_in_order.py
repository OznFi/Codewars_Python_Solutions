def unique_in_order(iterable):
    list=[]
    for id,val in enumerate(iterable):
        if(id==0):
            list.append(val)
        elif(val != iterable[id-1]):
            list.append(val)
    return list      