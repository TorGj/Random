import random     # Random ting
import json       # Eksporterings ting
# import time
# import numpy

r = 0
#navn = input('Navn: ')
n = int(input('Fra nr! '))
m = 1+int(input('Til nr! '))


p=[0]*(m-n)    #Hver posisjon settes til verdien 0, og lengden settes

def lage():
    tilfeldig = random.randrange(n,m,1) # trekk: (fra,til,trinnstørrelse)
    #print(tilfeldig)
    t = m-(tilfeldig+1)
    p[t] = p[t]+1         # her legges 1 til antall utfall av verdien 
    return tilfeldig

 
while not (r==10000):   # Her bestemmes hvor mange trekk som skal gjøres
    lage()
    r = r+1
    
print(p)




def skriv_til_fil():
    fil_nr_1 = open('myfile.txt', 'w') # åpner for skriving til fil..
    global m
    c = 0
    #i = 0
    for i in p:
        print('Antall ', m-1 ,'-tall er: ', p[c])
        fil_nr_1.write('Antall ' + str(m-1) + '-tall er: ' + str(p[c])+ '\n')
        c=c+1
        
        m = m-1
    fil_nr_1.close()
    

def skriv_til_fil_2():
    # Skriver til en fil til, men med et mer standard format...
    with open('myfile2.txt', 'w') as filehandle:
        json.dump(p, filehandle)


skriv_til_fil()
skriv_til_fil_2()