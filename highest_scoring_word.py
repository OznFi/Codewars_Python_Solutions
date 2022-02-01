def high(x):
    word_cont=x.split(); words=[]
    for id0,val0 in enumerate(word_cont):
        new_word={'index':id0}
        score=0;
        for id,val in enumerate(val0):
            score+=(ord(val)-96)
        new_word['score']=score
        words.append(new_word)
    highest_score_obj={'index':0, 'score':0}
    for id,val in enumerate(words):
        if(val['score']>highest_score_obj['score']):
            highest_score_obj=val
        elif(val['score']==highest_score_obj['score'] and val['index']<highest_score_obj['index']):
            highest_score_obj=val
    return word_cont[highest_score_obj['index']]    