def iq_test(numbers):
    even_index=0;even_number=0;odd_index=0;odd_number=0
    new_nums=numbers.split()
    for id,val in enumerate(new_nums):
        if(int(val)%2==0):
            even_index=id;even_number+=1
        else:
            odd_index=id;odd_number+=1
    if(odd_number>even_number):
        return even_index+1
    else:
        return odd_index+1