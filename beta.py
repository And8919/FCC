# len max valore operando1 o operando 2 per poi moltiplicarlo a '-' per otteneere la tabellina giusta

'''
Matteo Comisso, [25 mar 2022, 22:47:53]:
Te consigliassi de far sempre le operazioni, e usar el true solo per stampar o meno l’ultima riga

Invece de usarlo per far o meno le operazioni + stampe
'''


math = ['10 + 1', '3 - 224', '300 + 6', ' 28 - 5']

# creo le scatole
operazione1 = []
operazione2 = []
operazione3 = []
operazione4 = []
operazione5 = []

ad1 = []
ad2 = []
op = []
ris = []



# funzione che mette nelle scatole operazione tutti i singoli calcoli della lista

def sep(math):
    try:
        operazione1.append(math[0])
        operazione2.append(math[1])
        operazione3.append(math[2])
        operazione4.append(math[3])
        operazione5.append(math[4])
    except IndexError:
        pass
    finally:
        #print(operazione1, operazione2, operazione3, operazione4)
        pass


# Funzione che taglia l'operazione (che deve essere specificata) e la salva in cut.
# Poi metto gli elementi con un determinato indice nelle varie scatole

def taglio(operazione):
    for x in operazione:
        cut = x.split()
        
    ad1.append(cut[0])
    op.append(cut[1])
    ad2.append(cut[2])
    #print(cut)
    #print(ad1)
    #print(ad2)
    #print(op)

    # risultati
    if cut[1] == '+':
        ris.append(int(cut[0]) + int(cut[2]))
    elif cut[1] == '-':
        ris.append(int(cut[0]) - int(cut[2]))

# funzione per errori
def err():
    if len(math) > 5:
        print('Error: Too many problems.')
        quit()
    else:
        None

    for x in ad1:
        if len(x) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
        try:
            x = int(x)
        except ValueError:
            print('Error: Numbers must only contain digits.')
            quit()
    for x in ad2:
        if len(x) > 4:
            print('Error: Numbers cannot be more than four digits.')
            quit()
        try:
            x = int(x)
        except ValueError:
            print('Error: Numbers must only contain digits.')
            quit()

    for a in op:
        if a == '*' or a == '/':
            print('Error: Operator must be "+" or "-".')
            quit()


# test per la messa in colonna ATTENZIONE, MANCA LE OPERAZIONI 4 E 5. AGGIUNGERE TRY

def graph(a):
    print(' ' *(5-len(a[0])) + a[0] + '    ' + ' ' *(5-len(a[1])) + a[1] + '    ' + ' ' *(5-len(a[2])) + a[2] +  '    ' + ' ' *(5-len(a[3])) + a[3])

def graph2(a, b):
    print(a[0] + ' ' *(4-len(b[0])) + b[0] + '    ' + a[1] + ' ' *(4-len(b[1]))+ b[1] + '    ' + a[2] + ' ' *(4-len(b[2]))+ b[2] + '    ' + a[3] + ' ' *(4-len(b[3]))+ b[3] + '    ' )

def linea():
    print('-' * 5 + ' ' * 4 + '-' * 5 + ' ' * 4 + '-' * 5 + ' ' * 4 + '-' * 5 + ' ' * 4)

def tot():
    print(' ' *(5-len(str(ris[0]))) + str(ris[0]) + '    ' + ' ' *(5-len(str(ris[1]))) + str(ris[1]) + '    ' + ' ' *(5-len(str(ris[2]))) + str(ris[2]) + '    ' + ' ' *(5-len(str(ris[3]))) + str(ris[3]))
   

# eseguo le varie funzioni

sep(math)


taglio(operazione1)
taglio(operazione2)
taglio(operazione3)
taglio(operazione4)
err()

graph(ad1)
graph2(op,ad2)
linea()
tot()
