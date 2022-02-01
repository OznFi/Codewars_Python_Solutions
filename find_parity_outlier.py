def find_outlier(integers):
    odd_one = 0
    even_count=0;even_index=0
    odd_count=0;odd_index=0
    for id,valu in enumerate(integers):
        
            if(valu % 2 == 0):
                even_count+=1
                even_index=id
            else:
                odd_count+=1
                odd_index=id
    if(odd_count>even_count):
        odd_one=integers[even_index]
    else:
        odd_one=integers[odd_index]
    return odd_one