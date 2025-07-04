students=[{'name':'alice','score':90},{'name':'rob','score':80},{'name':'rin','score':70},{'name':'man','score':61},{'name':'guy','score':50}]
for st in students:
    if st['score']>=90:
        print(f'{st['name']} got an A')
    elif 80<=st['score']<=89:
        print(f'{st['name']} got a B')
    elif 70<=st['score']<=79:
        print(f'{st['name']} got a C')
    elif 60<=st['score']<=69:
        print(f'{st['name']} got a D')
    elif st['score']<60:
        print(f'{st['name']} got a F')
            

