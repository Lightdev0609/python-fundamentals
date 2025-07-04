def ta (S):
    wordnum={}
    word_count=S.split()
    print(f'there are {len(word_count)} words in here')
    for word in word_count:
        if word in wordnum:
            wordnum[word]+=1
        else:
            wordnum[word]=1
    print(wordnum)
    unique_num=[]
    for w in wordnum:
        if wordnum[w]==1:
            unique_num.append(w)
    print(f'there are {len(unique_num)} words in the text')
    cha=S.replace(' ','')
    print(f'there are {len(cha)} charachters in here')
    chanum=len(cha)
    avgwrd=round(chanum/len(word_count),2)
    vowel_count=0
    vowels=['a','e','i','o','u']
    for c in cha:
        if c in vowels:
            vowel_count+=1
    print(f'there are {vowel_count} vowels')
text='a person who thinks lal the time has nopthing to think about execpt thoughts'
ta(text)

        

    
