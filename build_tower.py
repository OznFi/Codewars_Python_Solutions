def tower_builder(n_floors):
    star_list=[];it=0;n_floor_count=n_floors
    while(it<n_floors):
        star="*"*((2*it)+1)
        if(it<n_floors-1):
            star_text=" "*(n_floor_count-1)
            star_text+=star
            star_text+=" "*(n_floor_count-1)
            star_list.append(star_text)
        else:
            star_text=star
            star_list.append(star_text)
        it+=1
        n_floor_count-=1
    return star_list    