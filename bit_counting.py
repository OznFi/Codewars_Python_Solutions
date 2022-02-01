def count_bits(n):
    bin_rep=bin(n);count=0
    for i in str(bin_rep):
        if (i=="1"):
            count+=1
    return count    