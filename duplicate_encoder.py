def duplicate_encode(word):
    char_counts=""
    word0=word.lower()
    for id,val in enumerate(word0):
        if (word0.count(val)>1):
            char_counts=char_counts+")"
        elif(word0.count(val)==1):
            char_counts=char_counts+"("
    return char_counts 