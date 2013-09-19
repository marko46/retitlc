import numpy as np
import random as rnd
#funzione che conta gli archi nella matrice
def arc_count(matrix,dim):
    n_arch=0
    for row in range(dim):
        for col in range(dim):
            if (matrix[row,col]==1):
                n_arch=n_arch+1
    return (n_arch-dim)/2  
#genera una matrice con un 1 se c'e la connessione 0 se non c'e
def converted_m(matrix,dim):
    conv_mat=np.zeros((dim,dim),dtype=int)
    for row in range(dim):
        for col in range(dim):
            if matrix[row,col]!=10000:
                conv_mat[row,col]=1
    return conv_mat
#trova uno zero nella matrice
def found_zero(matrix,dim):
    for row in range(dim):
        for col in range(dim):
            if(matrix[row,col]==0):
                return 1
    return 0
if __name__ == '__main__':
    pass
n_nodi=5#int(rnd.uniform(5,100))
print("il grafo ha %d nodi"%n_nodi)
m_adiacenze=np.zeros((n_nodi,n_nodi),dtype=int)#inizializzo matrice di zeri (tipo int)
connected=0
while connected==0:
    for row in range(n_nodi):
        for col in range(n_nodi):
            if col==row:
                m_adiacenze[row,col]=0  #diagonale principale
            else:
                peso=0#inizializzo il peso da assegnare all'arco con 0
                while peso==0:
                    peso=int(rnd.uniform(-10,10))   #arrivo fino a 10 perche il peso max e 10
                    if peso<0:
                        m_adiacenze[row,col]=10000  #faccio due azsegnamenti perche la matrice e simmetrica
                        m_adiacenze[col,row]=10000
                    if peso>0:
                        m_adiacenze[row,col]=peso   #faccio due azsegnamenti perche la matrice e simmetrica
                        m_adiacenze[col,row]=peso
    print("la matrice delle adiacenze e:\n\n")
    print(m_adiacenze)
    m_connect=converted_m(m_adiacenze,n_nodi)
    print("\nLa matrice delle connessioni e:\n")
    print(m_connect)
    n_arch=arc_count(m_connect,n_nodi)
    print("\nIl numero di archi e %d"%n_arch)
    print("\n\n")
    m_appoggio=m_connect
    for expo in range(int(n_arch-1)):
        m_appoggio=m_appoggio.dot(m_connect)
    print("la matrice per testare le connessioni e:\n")
    print(m_appoggio)
    print("\n\n")
    connected=not found_zero(m_appoggio,n_nodi)
print("\n Il grafo risulta connesso!\n")
begin=eval(input('Inserisci il nodo di partenza: '))
print("\n")
end=eval(input('Inserisci il nodo di arrivo: '))
print("\n calcolo il percorso da %d a %d:\n"%(begin,end))
distanze=np.zeros(n_nodi)
for i in range(n_nodi):
    distanze[i]=10000
provenienze=np.zeros(n_nodi)
for i in range(n_nodi):
    provenienze[i]=-1
visitato=np.zeros(n_nodi)
distanze[begin]=0
nodo_attuale=begin
min_dist=0
while (nodo_attuale!=end) and (min_dist!=10000):
    min_dist=10000
    for i in range(n_nodi):
        if (visitato[i]==0) and (distanze[i]<min_dist):
            min_dist=distanze[i]
            nodo_attuale=i
    visitato[nodo_attuale]=1
    for i in range(n_nodi):
        if (m_adiacenze[nodo_attuale,i]!=10000) and (distanze[i]>distanze[nodo_attuale]+m_adiacenze[nodo_attuale,i]):
            distanze[i]=distanze[nodo_attuale]+m_adiacenze[nodo_attuale,i]
            provenienze[i]=nodo_attuale
if(visitato[end]==0):
    print("non esiste un cammino tra i due nodi")
else:
    print("il cammino pesa: %d\n"%distanze[end])
    i=end
    print("il percorso a ritroso e:\n")
    while i!=begin:
        print(int(i))
        i=provenienze[i]
    print(int(i))