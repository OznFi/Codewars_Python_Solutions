def pig_it(text):
    words=text.split();added='';puncs=[",",".","!",";",":","?"]
    for id,val in enumerate(words):
        str1=''
        print(val)
        if(not(val in puncs)):
            str1=val[1:]+val[0]+"ay"
        else:
            str1=val
        if(id != len(words)-1):
            str1+=" "
        added+=str1
    return added     