def get_count(sentence):
    count = 0
    for i in sentence:
        if(i in ['a','e','i','o','u']):
            count+=1
    return count  