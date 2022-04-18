
def arithmetic_arranger(problems, solutions = False): # da capire perchè non va il true
    

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




# separo gli elementi in operatori sopra, segno e operatori sotto
    op1 = []
    sign = []
    op2 = []

    for element in problems:
        cut = element.split()
        op1.append(cut[0])
        sign.append(cut[1])
        op2.append(cut[2])






#errori

    if len(problems) > 5:
        print('Error: Too many problems.')
        quit()
    else:
        None

    for x in op1:
        if len(x) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
        try:
            x = int(x)
        except ValueError:
            print('Error: Numbers must only contain digits.')
            quit()
    for x in op2:
        if len(x) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
        try:
            x = int(x)
        except ValueError:
            print('Error: Numbers must only contain digits.')
            quit()

    for a in sign:
        if a == '*' or a == '/':
            print('Error: Operator must be "+" or "-".')
            quit()








# creo la lunghezzza delle basi (controllare quanti trattini)
    try:
        base1 ='-' * len(operazione1max) + '--'
        base2 = '-' * len(operazione2max) + '--'
        base3 ='-' * len(operazione3max) + '--'
        base4 ='-' * len(operazione4max) + '--'
        base5 ='-' * len(operazione5max) + '--'
    except:
        pass


#operatori sopra (controllare gli spazi)
    try:
        if len(problems) == 1:
            print(' ' * (len(base1) - len(op1[0])) + op1[0])
        elif len(problems) == 2:
            print(' ' * (len(base1) - len(op1[0])) + op1[0] + '    ' +' ' * (len(base2) - len(op1[1])) + op1[1])
        elif len(problems) == 3:
            print(' ' * (len(base1) - len(op1[0])) + op1[0] + '    ' + ' ' * (len(base2) - len(op1[1])) + op1[1] + '    ' + ' ' * (len(base3) - len(op1[2])) + op1[2])
        elif len(problems) == 4:
            print(' ' * (len(base1) - len(op1[0])) + op1[0] + '    ' + ' ' * (len(base2) - len(op1[1])) + op1[1] + '    ' + ' ' * (len(base3) - len(op1[2])) + op1[2] + '    ' + ' ' * (len(base4) - len(op1[3])) + op1[3])
        elif len(problems) == 5:
            print(' ' * (len(base1) - len(op1[0])) + op1[0] + '    ' + ' ' * (len(base2) - len(op1[1])) + op1[1] + '    ' + ' ' * (len(base3) - len(op1[2])) + op1[2] + '    ' + ' ' * (len(base4) - len(op1[3])) + op1[3] + '    ' + ' ' * (len(base5) - len(op1[4])) + op1[4])
    except:
        pass



# OP SOTTO manca il segno

    try:
        if len(problems) == 1:
            print(sign[0] + ' ' * (int(len(base1) - len(op2[0]) - 1)) + op2[0])
        elif len(problems) == 2:
            print(sign[0] + ' ' * (int(len(base1) - len(op2[0]) - 1)) + op2[0] + '    ' + sign[1] +  ' ' * (int(len(base2) - len(op2[1]) -1)) + op2[1])
        elif len(problems) == 3:
            print(sign[0] + ' ' * (int(len(base1) - len(op2[0]) - 1)) + op2[0] + '    ' + sign[1] + ' ' * (int(len(base2) - len(op2[1]) -1 )) + op2[1] + '    ' + sign[2] + ' ' * (int(len(base3) - len(op2[2]) -1 )) + op2[2])
        elif len(problems) == 4:
            print(sign[0] + ' ' * (int(len(base1) - len(op2[0]) -1 )) + op2[0] + '    ' + sign[1] + ' ' * (int(len(base2) - len(op2[1]) -1 )) + op2[1] + '    ' + sign[2] + ' ' * (int(len(base3) - len(op2[2]) -1 )) + op2[2] + '    ' + sign[3] + ' ' * (int(len(base4) - len(op2[3]) -1 )) + op2[3])
        elif len(problems) == 5:
            print(sign[0] + ' ' * (int(len(base1) - len(op2[0]) -1 )) + op2[0] + '    ' + sign[1] + ' ' * (int(len(base2) - len(op2[1]) -1 )) + op2[1] + '    ' + sign[2] + ' ' * (int(len(base3) - len(op2[2]) -1 )) + op2[2] + '    ' + sign[3] + ' ' * (int(len(base4) - len(op2[3]) -1 )) + op2[3] + '    ' + sign[4] + ' ' * (int(len(base5) - len(op2[4]) -1 )) + op2[4])
    except:
        pass

    
  
    # stampo la base (da controllare gli spazi)
    try:
        if len(problems) == 1:
            print(base1)
        elif len(problems) == 2:
            print(base1 + '    ' + base2)
        elif len(problems) == 3:
            print(base1 + '    ' + base2 + '    ' + base3)
        elif len(problems) == 4:
            print(base1 + '    ' + base2 + '    ' + base3 + '    ' + base4)
        elif len(problems) == 5:
            print(base1 + '    ' + base2 + '    ' + base3 + '    ' + base4 + '    ' + base5)
    except:
        pass

    
#soluzioni se True

    sol1 = ''
    sol2 = ''
    sol3 = ''
    sol4 = ''
    sol5 = ''

    try:
        if solutions == True:
            if '+' in operazione1:
                sol1 += str(int(operazione1[0]) + int(operazione1[2]))
            else:
                sol1 += str(int(operazione1[0]) - int(operazione1[2]))
            if '+' in operazione2:
                sol2 += str((int(operazione2[0]) + int(operazione2[2])))
            else:
                sol2 += str(int(operazione2[0]) - int(operazione2[2]))
            if '+' in operazione3:
                sol3 += str((int(operazione3[0]) + int(operazione3[2])))
            else:
                sol3 += str(int(operazione3[0]) - int(operazione3[2]))
            if '+' in operazione4:
                sol4 += str((int(operazione4[0]) + int(operazione4[2])))
            else:
                sol4 += str(int(operazione4[0]) - int(operazione4[2]))
            if '+' in operazione5:
                sol5 += str((int(operazione5[0]) + int(operazione5[2])))
            else:
                sol5 += str(int(operazione5[0]) - int(operazione5[2]))
    except:
        pass




    if len(problems) == 1:
        print((len(base1) - len(sol1)) * ' ' + sol1)
    elif len(problems) == 2:
        print((len(base1) - len(sol1)) * ' ' + sol1 + '    ' + (len(base2) - len(sol2)) * ' ' + sol2)
    elif len(problems) == 3:
        print((len(base1) - len(sol1)) * ' ' + sol1 + '    ' + (len(base2) - len(sol2)) * ' ' + sol2 + '    ' + (len(base3) - len(sol3)) * ' ' + sol3)
    elif len(problems) == 4:
        print((len(base1) - len(sol1)) * ' ' + sol1 + '    ' + (len(base2) - len(sol2)) * ' ' + sol2 + '    ' + (len(base3) - len(sol3)) * ' ' + sol3 + '    ' + (len(base4) - len(sol4)) * ' ' + sol4)
    elif len(problems) == 5:
        print((len(base1) - len(sol1)) * ' ' + sol1 + '    ' + (len(base2) - len(sol2)) * ' ' + sol2 + '    ' + (len(base3) - len(sol3)) * ' ' + sol3 + '    ' + (len(base4) - len(sol4)) * ' ' + sol4 + '    ' + (len(base5) - len(sol5)) * ' ' + sol5)


    #return arranged_problems

print(arithmetic_arranger(["32 + 698", '10 + 10', '1000 - 34', '10 + 1', '200 - 59',], True))