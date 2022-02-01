def same_structure_as(original,other):
    #assuming nested array dont contain more nested arrays
   
    nest=0;normal=0
    if(not isinstance(original, list)):
        if(isinstance(other, list)):
            return False
        else:
            if(original==other):
                return True
            else:
                return False
    if(isinstance(original, list)):
        if(not isinstance(other, list)):
            return False
    if(len(original)!=len(other)):
        return False
    for id,val in enumerate(original):
        if(isinstance(val, list)):
            #print(len(val));print(len(other[id]))
            if(not isinstance(other[id], list)):
                return False
            if(len(val)!=len(other[id])):
                return False
            return(same_structure_as(val, other[id]))
        else:
            if(isinstance(other[id], list)):
                return False
    return True 