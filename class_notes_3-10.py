count = 0 
names = ['sally', 'george','bob','bob','lenny','tom']
list = ['']*10
listsize = len(list)
for DATA in names:    
    FOUND = False 
    for POS in range(listsize):
        if list[POS] == DATA:
            FOUND = True 
            print('Dupliate'+list[POS]+ 'found')
    if FOUND == False: 
        list[count] = DATA 
        count += 1 
    print(list)