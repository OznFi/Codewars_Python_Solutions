def solution(args):
    ordered_list=[]
    sequence=False;i=0
    while (i<len(args)):
        if (i+2<len(args)and((abs(args[i]-args[i+1])==1) and abs(args[i+1]-args[i+2])==1)):
            sequence=True
            start=i
            while sequence:
                if(i+1<len(args)):
                    i+=1
                    if(i+2<len(args) and abs(args[i+1]-args[i+2])==1):
                        pass
                    else:
                        stri=str(args[start])+str("-")+str(args[i+1])
                        ordered_list.append(stri)
                        sequence=False
                        i+=2
                else:
                    i+=1
                    sequence=False
        else:
            ordered_list.append(str(args[i]))
            i+=1
    print(",".join(ordered_list))
    return ",".join(ordered_list) 