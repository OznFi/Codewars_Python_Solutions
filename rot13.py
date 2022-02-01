def rot13(message):
    lowers=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    uppers=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ind=None;empstr=""
    for id,val in enumerate(message):
        if(val==" "):
            empstr+=""
        if(val.isupper()):
            ind=uppers.index(val)+13
            ind=ind%len(uppers)
            tt=uppers[ind]
            empstr+=tt
        elif(val.islower()):
            ind=lowers.index(val)+13
            ind=ind%len(lowers)
            ta=lowers[ind]
            empstr+=ta
        else:
            empstr+=val
    return empstr