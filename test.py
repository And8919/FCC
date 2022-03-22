def my_function(food): # food serve per far capire che ci sarà un argomento
    for x in food: # food indica a x di andare a cercare nell'argomento che verrà indicato dopo(vedi variabile problems)
        cut = x.split()
        print(' ' *(5-len(cut[0])) + cut[0])
        print(cut[1] + ' ' *(4-len(cut[2])) + cut[2])
        print('-----')
        print('\n')
        
    
    

problems = [input('scrivi: '),input('scrivi: ') ]

my_function(problems)
