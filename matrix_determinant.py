import copy
def determinant(matrix):
    list=[]
    if(len(matrix)==1):
        return matrix[0][0]
    elif(len(matrix)==2):
        #print(matrix)
        first=matrix[0][0]*matrix[1][1]
        second=matrix[0][1]*matrix[1][0]
        #print('succ')
        return first-second
    elif(len(matrix)>2):
        for id,val in enumerate(matrix[0]):
            print(val)
            newmatrix=copy.deepcopy(matrix[1:])
            for id2,val2 in enumerate(newmatrix):
                newmatrix[id2].pop(id)
            #print(newmatrix)
            va=val*determinant(newmatrix)
            list.append(va)
    one=list[0];i=1
    while i<len(list):
        if(i%2):
            one=one-list[i]
        else:
            one=one+list[i]
        i+=1
    #print(list)    
    return one 