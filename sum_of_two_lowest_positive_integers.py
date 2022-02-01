def sum_two_smallest_numbers(numbers):
    low_1=numbers[0];low_2=numbers[1];
    for id,val in enumerate(numbers):   
      if(id>1):  
        if(low_2<low_1):
            low_temp=low_1
            low_1=low_2
            low_2=low_temp    
        if(val<low_1):
            temp_low=low_1
            low_1=val
            low_2=temp_low
        else:
            if(val<low_2):
                low_2=val
    print(low_1);print(low_2)
    return low_1+low_2 