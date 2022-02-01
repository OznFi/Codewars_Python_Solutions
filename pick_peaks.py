def pick_peaks(arr):
    pos=[];peaks=[];obj={'pos':[],'peaks':[]};increase=0;
    if(len(arr)<=2):
        return obj
    for id,val in enumerate(arr):
        if(id!=0 and id!=len(arr)-1):
            if(val-arr[id-1]>0 and val-arr[id+1]>0):
                obj['pos'].append(id);obj['peaks'].append(val)
            if(val-arr[id-1]>0 and val-arr[id+1]==0):
                i=1
                while(id+i<len(arr)):
                    if(arr[id+i]<val):
                        obj['pos'].append(id);obj['peaks'].append(val)
                        break
                    elif(arr[id+i]>val):
                        break
                    i+=1    
    return obj