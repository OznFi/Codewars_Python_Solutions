def order(sentence):
    indexes=[];strin=sentence.split();final="";number_text="123456789";number=[None]*(len(strin)+1)
    for id0,val0 in enumerate(strin):
        for id,val in enumerate(val0):
            #print(val)
            if(val in number_text):
                #print(int(val))
                number[int(val)]=val0
    number.pop(0)
    for y in number:
        if(y==number[len(number)-1]):
            final+=str(y)
        else:
            final+=str(y)
            final+=" "
    print(number)
    return final    