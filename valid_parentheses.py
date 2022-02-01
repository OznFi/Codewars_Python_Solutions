def valid_parentheses(string):
    left_count=0;right_count=0;case=False
    order_case=True
    for id,val in enumerate(string):
        if val=="(":
            left_count+=1
        if(val==")"):
            right_count+=1
            if(right_count>left_count):
                order_case=False
    if(left_count==right_count and order_case):
        case=True
    return case    