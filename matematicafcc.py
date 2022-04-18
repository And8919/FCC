

from ssl import OP_NO_TLSv1_1


def arithmetic_arranger(problems, solutions = False):
    
# divido le singole operazioni (utili per le sommealla fine)
    operazione1 = []
    operazione2 = []
    operazione3 = []
    operazione4 = []
    operazione5 = []

    if len(problems) == 1:
        operazione1 = problems[0].split()
    elif len(problems) == 2:
        operazione1 = problems[0].split()
        operazione2 = problems[1].split()
    elif len(problems) == 3:
        operazione1 = problems[0].split()
        operazione2 = problems[1].split()
        operazione3 = problems[2].split()
    elif len(problems) == 4:
        operazione1 = problems[0].split()
        operazione2 = problems[1].split()
        operazione3 = problems[2].split()
        operazione4 = problems[3].split()
    elif len(problems) == 5:
        operazione1 = problems[0].split()
        operazione2 = problems[1].split()
        operazione3 = problems[2].split()
        operazione4 = problems[3].split()
        operazione5 = problems[4].split()


#ricerca del max
    try:
        operazione1max= max(operazione1[0], operazione1[2])
        operazione2max = max(operazione2[0], operazione2[2])
        operazione3max = max(operazione3[0], operazione3[2])
        operazione4max = max(operazione4[0], operazione4[2])
        operazione5max = max(operazione5[0], operazione5[2])
    except:
        pass




# separo gli elementi in peratori sopra, segno e operatori sotto
    op1 = []
    sign = []
    op2 = []

    for element in problems:
        cut = element.split()
        op1.append(cut[0])
        sign.append(cut[1])
        op2.append(cut[2])


    
# zona stampa
    try:
        base1 ='-' * len(operazione1max) + '-'
        base2 = '-' * len(operazione2max) + '-' # tets per lunghezza base (lunghezza del n max + 1)
        base3 ='-' * len(operazione3max) + '-'
        base4 ='-' * len(operazione4max) + '-'
        base5 ='-' * len(operazione5max) + '-' ### da sbloccare
    except:
        pass
    
  
    #idea possibile
    try:
        if len(problems) == 1:
            print(base1)
        elif len(problems) == 2:
            print(base1 + '  ' + base2)
        elif len(problems) == 3:
            print(base1 + '  ' + base2 + '  ' + base3)
        elif len(problems) == 4:
            print(base1 + '  ' + base2 + '  ' + base3 + '  ' + base4)
        elif len(problems) == 5:
            print(base1 + '  ' + base2 + '  ' + base3 + '  ' + base4 + '  ' + base5)
    except:
        pass
















    #return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
